#!/usr/bin/env python3
"""Generate index.html from dated HTML files in the current directory."""

from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUTPUT_FILE = ROOT / "index.html"
MATCH_RE = re.compile(r"^\d{4}.*\.html$")
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)


def extract_title(path: Path) -> str:
    """Return the file title or a fallback based on filename."""
    try:
        content = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return path.stem.replace("_", " ")

    match = TITLE_RE.search(content)
    if not match:
        return path.stem.replace("_", " ")

    title = " ".join(match.group(1).split())
    if not title:
        return path.stem.replace("_", " ")
    return title


def build_index_html(entries: list[tuple[str, str]]) -> str:
    items = []
    for filename, title in entries:
        safe_filename = html.escape(filename)
        safe_title = html.escape(title)
        items.append(
            f'    <li><a href="{safe_filename}">{safe_title}</a> '
            f'<span class="filename">- {safe_filename}</span></li>'
        )

    items_html = "\n".join(items) if items else "    <li>No matching files found.</li>"

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Trip Photo Maps</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      margin: 2rem;
      line-height: 1.5;
      color: #222;
    }}
    h1 {{
      margin-top: 0;
    }}
    ul {{
      padding-left: 1.25rem;
    }}
    li {{
      margin: 0.35rem 0;
    }}
    .filename {{
      color: #666;
      font-size: 0.92em;
    }}
  </style>
</head>
<body>
  <h1>Trip Photo Maps</h1>
  <p>
    This website contains maps of where photos were taken on various trips. For trips that are blogged in
    <a href="https://www.garrettblog.com" target="_blank" rel="noopener noreferrer">garrettblog.com</a>,
    the photos link to the blog with a brief summary of that day's activities.
  </p>
  <ul>
{items_html}
  </ul>
</body>
</html>
"""


def main() -> None:
    files = sorted(p for p in ROOT.iterdir() if p.is_file() and MATCH_RE.match(p.name))
    entries = [(path.name, extract_title(path)) for path in files]
    OUTPUT_FILE.write_text(build_index_html(entries), encoding="utf-8")
    print(f"Wrote {OUTPUT_FILE.name} with {len(entries)} entries.")


if __name__ == "__main__":
    main()
