import concurrent.futures as cf
import json
import re
import subprocess
import sys
import urllib.parse

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
LINK = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")


def extract(path):
    text = open(path, encoding="utf-8").read()
    order, seen = [], set()
    for m in LINK.finditer(text):
        url = m.group(2)
        if url not in seen:
            seen.add(url)
            order.append((m.group(1), url))
    return order


def http_status(url):
    try:
        out = subprocess.run(
            ["curl", "-sS", "-L", "--max-time", "45", "-o", "/dev/null", "-A", UA,
             "-w", "%{http_code}\t%{url_effective}", url],
            capture_output=True, text=True, timeout=60).stdout
        code, eff = (out.split("\t") + [""])[:2]
        return code or "ERR", eff
    except Exception:
        return "ERR", ""


def crossref_title(url):
    doi = urllib.parse.unquote(url.split("doi.org/", 1)[1])
    try:
        raw = subprocess.run(
            ["curl", "-sS", "-L", "--max-time", "40", "https://api.crossref.org/works/" + doi],
            capture_output=True, text=True, timeout=50).stdout
        title = (json.loads(raw)["message"].get("title") or [""])[0]
        return title[:90]
    except Exception:
        pass
    try:
        raw = subprocess.run(
            ["curl", "-sS", "-L", "--max-time", "40", "https://api.datacite.org/dois/" + doi],
            capture_output=True, text=True, timeout=50).stdout
        title = json.loads(raw)["data"]["attributes"]["titles"][0]["title"]
        return "DataCite: " + title[:80]
    except Exception:
        return ""


def check(item):
    text, url = item
    code, eff = http_status(url)
    title = crossref_title(url) if "doi.org/" in url and "api.datacite.org" not in url else ""
    return {"text": text, "url": url, "code": code, "effective": eff, "registry_title": title}


if __name__ == "__main__":
    src, out = sys.argv[1], sys.argv[2]
    items = extract(src)
    with cf.ThreadPoolExecutor(10) as ex:
        results = list(ex.map(check, items))
    json.dump(results, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    codes = {}
    for r in results:
        codes[r["code"]] = codes.get(r["code"], 0) + 1
    print("urls:", len(results), "codes:", codes)
    for r in results:
        if r["code"] != "200":
            print(r["code"], r["url"], "| registry:", r["registry_title"][:60])
