#!/usr/bin/env python3
"""
Automated URL & Open-Source Artifact Verifier for 04_OpenSource_Solution_Discovery/.
Checks every unique markdown URL across 01–05_*.md, verifies HTTP status codes,
detects dead/404/empty GitHub repos, verifies Kaggle datasets via Kaggle's official
public REST API (no CAPTCHA bypass), and writes raw audit results to verification_log.json.
"""

import json
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import requests

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_PATH = Path(__file__).resolve().parent / "verification_log.json"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

URL_RE = re.compile(r"\]\((https?://[^)\s]+)\)")


def collect_urls():
    """Extract all unique markdown link URLs and their source files."""
    url_sources = {}
    for md in sorted(BASE_DIR.glob("0[1-5]_*.md")):
        text = md.read_text(encoding="utf-8")
        # Ignore anything inside a dedicated transparency/excluded section if marked <!-- UNVERIFIED_REF_START -->
        cleaned = re.sub(
            r"<!--\s*UNVERIFIED_REF_START\s*-->.*?<!--\s*UNVERIFIED_REF_END\s*-->",
            "",
            text,
            flags=re.S,
        )
        for m in URL_RE.finditer(cleaned):
            u = m.group(1).strip()
            url_sources.setdefault(u, set()).add(md.name)
    return {u: sorted(files) for u, files in sorted(url_sources.items())}


def verify_one(item):
    url, files = item
    ts = datetime.now(timezone.utc).isoformat()
    record = {
        "url": url,
        "files": files,
        "status_code": None,
        "final_url": None,
        "method": "HTTP_GET",
        "ok": False,
        "note": "",
        "timestamp": ts,
    }

    # 1. Kaggle datasets -> verify via official public REST API (no CAPTCHA bypass)
    m_kag = re.match(r"^https?://(?:www\.)?kaggle\.com/datasets/([^/?#]+/[^/?#]+)/?$", url)
    if m_kag:
        slug = m_kag.group(1)
        api_url = f"https://www.kaggle.com/api/v1/datasets/view/{slug}"
        try:
            r = requests.get(api_url, headers={"Accept": "application/json"}, timeout=15)
            record["method"] = "KAGGLE_PUBLIC_API"
            record["status_code"] = r.status_code
            record["final_url"] = url
            if r.status_code == 200:
                data = r.json()
                title = data.get("titleNullable") or data.get("title") or ""
                if data.get("id") or title:
                    record["ok"] = True
                    record["note"] = (
                        f"Kaggle API HTTP 200 (title={title}, "
                        f"votes={data.get('voteCountNullable') or data.get('voteCount', 0)})"
                    )
                else:
                    record["note"] = "Kaggle API returned empty dataset object"
            else:
                record["note"] = f"Kaggle API returned {r.status_code}"
        except Exception as e:
            record["note"] = f"Error: {str(e)[:120]}"
        return record

    # 1b. YouTube watch/short links -> verify via official YouTube oEmbed API (returns 200 JSON for live videos, 404/401 for dead/private)
    if "youtube.com/watch" in url or "youtu.be/" in url:
        try:
            r = requests.get(
                "https://www.youtube.com/oembed",
                params={"url": url, "format": "json"},
                headers=HEADERS,
                timeout=15,
            )
            record["method"] = "YOUTUBE_OEMBED_API"
            record["status_code"] = r.status_code
            record["final_url"] = url
            if r.status_code == 200:
                data = r.json()
                record["ok"] = True
                record["note"] = f"YouTube oEmbed HTTP 200 (title={data.get('title','')[:70]}, author={data.get('author_name','')})"
            else:
                record["note"] = f"YouTube oEmbed returned HTTP {r.status_code}"
        except Exception as e:
            record["note"] = f"Error: {str(e)[:120]}"
        return record

    # 2. GitHub repo root -> verify HTTP 200 + non-empty via gh api if available
    m_gh = re.match(r"^https?://(?:www\.)?github\.com/([^/?#]+/[^/?#]+?)(?:\.git)?/?$", url)
    if m_gh:
        slug = m_gh.group(1)
        try:
            r = requests.get(url, headers=HEADERS, timeout=15, allow_redirects=True)
            record["status_code"] = r.status_code
            record["final_url"] = r.url
            if r.status_code == 200:
                # Confirm non-empty repo via gh api (fast authenticated check)
                res = subprocess.run(
                    ["gh", "api", f"repos/{slug}/contents"],
                    capture_output=True,
                    text=True,
                    timeout=15,
                )
                if res.returncode == 0:
                    try:
                        items = json.loads(res.stdout)
                        names = [x.get("name", "") for x in items] if isinstance(items, list) else []
                        non_empty = len(names) >= 2 or (len(names) == 1 and names[0].lower() != "readme.md")
                        record["ok"] = non_empty
                        record["note"] = f"GitHub HTTP 200, root_items={len(names)}" + ("" if non_empty else " [EMPTY_REPO]")
                    except Exception:
                        record["ok"] = True
                        record["note"] = "GitHub HTTP 200"
                else:
                    record["ok"] = True
                    record["note"] = "GitHub HTTP 200 (contents check skipped)"
            else:
                record["note"] = f"HTTP {r.status_code}"
        except Exception as e:
            record["note"] = f"Error: {str(e)[:120]}"
        return record

    # 3. Standard HTTP GET check for all other platforms
    try:
        r = requests.get(url, headers=HEADERS, timeout=18, allow_redirects=True)
        record["status_code"] = r.status_code
        record["final_url"] = r.url
        body_low = r.text[:25000].lower()

        if r.status_code == 200:
            # Soft-404 & anti-bot detection
            if "just a moment..." in body_low and "cloudflare" in body_low:
                record["ok"] = False
                record["note"] = "Cloudflare challenge page (not bypassed)"
            elif ("youtube.com/watch" in url or "youtu.be/" in url) and '"status":"error"' in body_low:
                record["ok"] = False
                record["note"] = "YouTube video unavailable"
            elif "vercel.app" in url and ("deployment_not_found" in body_low or "404: not_found" in body_low):
                record["ok"] = False
                record["note"] = "Vercel deployment not found"
            elif "netlify.app" in url and "page not found" in body_low and "netlify" in body_low:
                record["ok"] = False
                record["note"] = "Netlify page not found"
            elif "drive.google.com" in url and "sorry, the file you have requested does not exist" in body_low:
                record["ok"] = False
                record["note"] = "Google Drive file does not exist"
            else:
                record["ok"] = True
                record["note"] = "HTTP 200 OK"
        else:
            record["note"] = f"HTTP {r.status_code}"
    except Exception as e:
        record["note"] = f"Error: {str(e)[:120]}"
    return record


def main():
    url_map = collect_urls()
    print(f"Found {len(url_map)} unique URLs across 01–05_*.md. Verifying...")
    with ThreadPoolExecutor(max_workers=12) as ex:
        results = list(ex.map(verify_one, list(url_map.items())))

    passed = [r for r in results if r["ok"]]
    failed = [r for r in results if not r["ok"]]

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_unique_urls": len(results),
        "passed_count": len(passed),
        "failed_count": len(failed),
        "results": results,
    }
    LOG_PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\nVerification Complete: {len(passed)}/{len(results)} PASSED, {len(failed)} FAILED.")
    if failed:
        print("\n=== FAILED URLS ===")
        for f in failed:
            print(f"  [{f['status_code']}] {f['url']}  ({', '.join(f['files'])}) -> {f['note']}")
        sys.exit(1)
    else:
        print("All URLs verified clean!")


if __name__ == "__main__":
    main()
