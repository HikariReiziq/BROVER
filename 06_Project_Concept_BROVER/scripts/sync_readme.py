#!/usr/bin/env python3
"""Synchronize root README.md from 06_Project_Concept_BROVER/PROJECT_CONCEPT_BROVER.md
while remapping all relative asset and cross-folder markdown links so GitHub renders 100% cleanly.
"""

import os
import re

ROOT = "/home/reiziqzip/Programmer/Hackathon-UNJ"
SRC = os.path.join(ROOT, "06_Project_Concept_BROVER", "PROJECT_CONCEPT_BROVER.md")
DST = os.path.join(ROOT, "README.md")


def sync() -> None:
    with open(SRC, "r", encoding="utf-8") as f:
        text = f.read()

    # Remap relative links from 06_Project_Concept_BROVER/ to repository root
    text = text.replace("](./assets/", "](./06_Project_Concept_BROVER/assets/")
    text = text.replace("](../", "](./")

    with open(DST, "w", encoding="utf-8") as f:
        f.write(text)

    # Verify all local links from root
    links = re.findall(r"\]\((?!https?://|mailto:|#)([^)#]+)", text)
    broken = [l for l in links if not os.path.exists(os.path.normpath(os.path.join(ROOT, l)))]
    print(f"SYNCED README.md ({len(text)} chars) | Local links: {len(links)} total, {len(broken)} broken")
    if broken:
        raise SystemExit(f"BROKEN LINKS IN README.md: {broken}")


if __name__ == "__main__":
    sync()
