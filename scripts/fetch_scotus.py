"""Download one Supreme Court term's slip opinions (PDFs) for the stage 2 corpus.

US Supreme Court opinions are works of the US federal government, so they are public domain
(17 U.S.C. 105). The PDFs go outside this repo, as the brief asks; `p2 ingest` reads them from there.

Usage, from the repo root (work/p2-rag):
    uv run python scripts/fetch_scotus.py 22 ../p2-raw/scotus-2022

The first argument is the term's two-digit year: 22 is the October 2022 term, listed at
https://www.supremecourt.gov/opinions/slipopinion/22. Files already downloaded are skipped.
"""

from __future__ import annotations

import re
import sys
import time
import urllib.request
from pathlib import Path

BASE = "https://www.supremecourt.gov"
HEADERS = {"User-Agent": "Mozilla/5.0 (course project: CSCI 498E P2 corpus)"}
PAUSE_S = 1.0  # one request a second, to be polite to the court's server


def get(url: str) -> bytes:
    request = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read()


def main(term: str, out: Path) -> None:
    page = get(f"{BASE}/opinions/slipopinion/{term}").decode("utf-8", errors="replace")
    links = sorted(set(re.findall(rf"/opinions/{term}pdf/[^\"' ]+\.pdf", page)))
    if not links:
        sys.exit(f"No opinion PDFs found for term {term}; check the page by hand.")
    out.mkdir(parents=True, exist_ok=True)
    print(f"Term {term}: {len(links)} opinion PDFs -> {out}")
    for n, link in enumerate(links, 1):
        target = out / link.rsplit("/", 1)[1]
        if target.exists() and target.stat().st_size > 0:
            print(f"  [{n}/{len(links)}] {target.name} already here")
            continue
        target.write_bytes(get(BASE + link))
        print(f"  [{n}/{len(links)}] {target.name} {target.stat().st_size // 1024} KB")
        time.sleep(PAUSE_S)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], Path(sys.argv[2]))
