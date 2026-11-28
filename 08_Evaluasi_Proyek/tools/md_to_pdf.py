#!/usr/bin/env python3
"""Export a Markdown file to `<stem>_tmp.html` and `<name>.md.pdf` next to it.

- Python-Markdown with tables, so pipe tables render.
- Relative image paths are kept, and the HTML is opened from its own folder,
  so images resolve without absolute file:// paths.
- Waits until every <img> is loaded, then prints A4 with backgrounds.

Usage (from the repo root):
  uv run --python 3.13 --with markdown --with playwright==1.63.0 \
      python 08_Evaluasi_Proyek/tools/md_to_pdf.py <file.md> [<file.md> ...]
"""
import sys
from html import escape
from pathlib import Path

import markdown
from playwright.sync_api import sync_playwright

CSS = """
@page { size: A4; margin: 14mm 12mm 16mm 12mm; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: "Open Sans", "Segoe UI", "DejaVu Sans", Arial, sans-serif; font-size: 10.5pt;
       line-height: 1.5; color: #0F172A; margin: 0; }
h1 { font-size: 19pt; line-height: 1.25; margin: 0 0 10pt; }
h2 { font-size: 15pt; margin: 18pt 0 8pt; border-bottom: 1.5px solid #CBD5E1; padding-bottom: 3pt; }
h3 { font-size: 12.5pt; margin: 14pt 0 6pt; }
h4 { font-size: 11pt; margin: 12pt 0 5pt; }
h1, h2, h3, h4 { page-break-after: avoid; break-after: avoid; }
p, li { orphans: 3; widows: 3; }
a { color: #1D4ED8; text-decoration: none; word-break: break-word; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 9pt; background: #F1F5F9;
       padding: 0 2px; border-radius: 3px; }
pre { background: #F8FAFC; border: 1px solid #E2E8F0; padding: 6pt; white-space: pre-wrap; font-size: 8.5pt; }
blockquote { margin: 8pt 0; padding: 4pt 10pt; border-left: 4px solid #94A3B8; background: #F8FAFC; color: #334155; }
table { border-collapse: collapse; width: 100%; margin: 8pt 0; font-size: 8.6pt; page-break-inside: auto; }
tr { page-break-inside: avoid; break-inside: avoid; }
th, td { border: 1px solid #CBD5E1; padding: 3pt 4pt; vertical-align: top; text-align: left; }
th { background: #E2E8F0; }
img { max-width: 100%; height: auto; display: block; margin: 6pt auto; page-break-inside: avoid; break-inside: avoid; }
hr { border: none; border-top: 1px solid #CBD5E1; margin: 12pt 0; }
"""


def export(md_path: Path) -> None:
    md_path = md_path.resolve()
    text = md_path.read_text(encoding="utf-8")
    body = markdown.markdown(text, extensions=["tables", "fenced_code", "sane_lists"])
    html = (f"<!DOCTYPE html>\n<html lang=\"id\">\n<head>\n<meta charset=\"utf-8\">\n"
            f"<title>{escape(md_path.name)}</title>\n<style>{CSS}</style>\n</head>\n<body>\n{body}\n</body>\n</html>\n")
    html_path = md_path.with_name(md_path.stem + "_tmp.html")
    pdf_path = md_path.with_name(md_path.name + ".pdf")
    html_path.write_text(html, encoding="utf-8")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(html_path.as_uri(), wait_until="load")
        page.wait_for_function(
            "Array.from(document.images).every(i => i.complete)", timeout=120_000)
        stats = page.evaluate(
            "(() => { const im = Array.from(document.images);"
            " return {total: im.length, ok: im.filter(i => i.naturalWidth > 0).length,"
            " broken: im.filter(i => i.naturalWidth === 0).map(i => i.getAttribute('src'))}; })()")
        page.pdf(path=str(pdf_path), format="A4", print_background=True,
                 margin={"top": "14mm", "bottom": "16mm", "left": "12mm", "right": "12mm"})
        browser.close()
    print(f"{md_path.name}: images {stats['ok']}/{stats['total']} loaded -> {html_path.name}, {pdf_path.name}")
    if stats["broken"]:
        print("  BROKEN:", stats["broken"])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    for arg in sys.argv[1:]:
        export(Path(arg))
