#!/usr/bin/env python3
"""Merge garrettblog trip maps into a single all_maps.html file."""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT_NAME = "all_maps.html"
OUTPUT_TITLE = "All Trips Photo Map"

IGNORE_HTML_FILES = [
    "index.html",
    "2024-05_eastern_europe.html",
    "uwc_f_n_f.html",
    "2023-04_japan_trip-initial_map.html",
    "2024-02-14_valentines_day_map.html",
    OUTPUT_NAME,
]

MAP_CENTER_LAT = 37.7749
MAP_CENTER_LON = -122.4194
MAP_ZOOM = 2
COORD_ROUND = 6

BLOG_PREFIX = "https://www.garrettblog.com"
API_KEY_RE = re.compile(
    r"maps/api/js\?[^\"]*\bkey=([^\"&]+)",
    re.IGNORECASE,
)
MARKER_ICON_RE = re.compile(
    r"(var marker_icon_FF0000 = \{.*?\n        \};)",
    re.DOTALL,
)
MARKER_BLOCK_RE = re.compile(
    r"var info_marker_(\d+) = new google\.maps\.Marker\(\{\s*"
    r"position: new google\.maps\.LatLng\(([-\d.]+),\s*([-\d.]+)\),.*?"
    r"var info_window_\1 = new google\.maps\.InfoWindow\(\{\s*"
    r"content: '((?:\\'|[^'])*)'",
    re.DOTALL,
)
HREF_RE = re.compile(r'href="(https://www\.garrettblog\.com/[^"]+)"', re.IGNORECASE)
IMG_RE = re.compile(r"<img\b", re.IGNORECASE)


def js_unescape_single_quoted(s: str) -> str:
    out: list[str] = []
    i = 0
    while i < len(s):
        if s[i] == "\\" and i + 1 < len(s):
            n = s[i + 1]
            if n == "'":
                out.append("'")
                i += 2
                continue
            if n == "n":
                out.append("\n")
                i += 2
                continue
            if n == "r":
                out.append("\r")
                i += 2
                continue
            if n == "\\":
                out.append("\\")
                i += 2
                continue
            out.append(s[i])
            i += 1
            continue
        out.append(s[i])
        i += 1
    return "".join(out)


def js_escape_single_quoted(s: str) -> str:
    return (
        s.replace("\\", "\\\\")
        .replace("'", "\\'")
        .replace("\n", "\\n")
        .replace("\r", "\\r")
    )


def extract_api_key(sample_html: str) -> str:
    match = API_KEY_RE.search(sample_html)
    if not match:
        raise ValueError("Could not find Google Maps API key in sample HTML.")
    return match.group(1)


def extract_marker_icon(sample_html: str) -> str:
    match = MARKER_ICON_RE.search(sample_html)
    if not match:
        raise ValueError("Could not find marker_icon_FF0000 block in sample HTML.")
    return match.group(1)


def is_garrettblog_map(path: Path) -> bool:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    return (
        "new google.maps.InfoWindow" in text
        and BLOG_PREFIX in text
    )


def collect_entries(root: Path) -> tuple[dict[str, tuple[float, float, str]], dict]:
    seen_urls: dict[str, tuple[float, float, str]] = {}
    stats = {
        "files_scanned": 0,
        "files_used": 0,
        "segments_total": 0,
        "segments_no_img": 0,
        "segments_no_href": 0,
        "duplicates_skipped": 0,
    }

    for path in sorted(root.glob("*.html")):
        if path.name in IGNORE_HTML_FILES:
            continue
        stats["files_scanned"] += 1
        if not is_garrettblog_map(path):
            continue
        stats["files_used"] += 1
        text = path.read_text(encoding="utf-8", errors="replace")
        for block in MARKER_BLOCK_RE.finditer(text):
            lat = float(block.group(2))
            lon = float(block.group(3))
            content = js_unescape_single_quoted(block.group(4))
            for part in re.split(r"<BR>", content, flags=re.IGNORECASE):
                stats["segments_total"] += 1
                if not IMG_RE.search(part):
                    stats["segments_no_img"] += 1
                    continue
                hrefs = HREF_RE.findall(part)
                if not hrefs:
                    stats["segments_no_href"] += 1
                    continue
                url = hrefs[0]
                if url in seen_urls:
                    stats["duplicates_skipped"] += 1
                    continue
                seen_urls[url] = (lat, lon, part.strip())

    return seen_urls, stats


def merge_colocated(
    seen_urls: dict[str, tuple[float, float, str]],
) -> list[tuple[float, float, str]]:
    """Group by rounded lat/lon; return one marker per location."""
    groups: dict[tuple[float, float], list[str]] = defaultdict(list)
    coords: dict[tuple[float, float], tuple[float, float]] = {}

    for _url, (lat, lon, part) in seen_urls.items():
        key = (round(lat, COORD_ROUND), round(lon, COORD_ROUND))
        groups[key].append(part)
        coords[key] = (lat, lon)

    markers: list[tuple[float, float, str]] = []
    for key in sorted(groups.keys()):
        lat, lon = coords[key]
        content = "<BR>".join(groups[key])
        markers.append((lat, lon, content))

    return markers


def render_markers_js(markers: list[tuple[float, float, str]]) -> str:
    lines: list[str] = []
    for idx, (lat, lon, content) in enumerate(markers):
        esc = js_escape_single_quoted(content)
        lines.append(f"""        var info_marker_{idx} = new google.maps.Marker({{
            position: new google.maps.LatLng({lat}, {lon}),
            label: "I",
            icon: marker_icon_FF0000,
            map: map
        }});

        var info_window_{idx} = new google.maps.InfoWindow({{
            content: '{esc}'
        }});

        info_marker_{idx}.addListener('click', function() {{
            info_window_{idx}.open(map, info_marker_{idx});
        }});
""")
    return "\n".join(lines)


def build_html(api_key: str, marker_icon_block: str, markers: list) -> str:
    markers_js = render_markers_js(markers)
    return f"""<html>
<head>
<meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
<meta http-equiv="content-type" content="text/html; charset=UTF-8" />
<title>{OUTPUT_TITLE}</title>
<script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?key={api_key}"></script>
<script type="text/javascript">
    function initialize() {{
        var map = new google.maps.Map(document.getElementById("map_canvas"), {{
            zoom: {MAP_ZOOM},
            center: new google.maps.LatLng({MAP_CENTER_LAT}, {MAP_CENTER_LON})
        }});

        {marker_icon_block}

{markers_js}

    }}
</script>
</head>
<body style="margin:0px; padding:0px;" onload="initialize()">
    <div id="map_canvas" style="width: 100%; height: 100%;" />
</body>
</html>
"""


def find_sample_html(root: Path) -> Path:
    for path in sorted(root.glob("*.html")):
        if path.name in IGNORE_HTML_FILES:
            continue
        if is_garrettblog_map(path):
            return path
    raise FileNotFoundError("No garrettblog map HTML found to copy API key and marker icon.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Merge trip maps into all_maps.html")
    parser.add_argument(
        "directory",
        nargs="?",
        default=str(ROOT),
        help="Directory containing map HTML files (default: script directory)",
    )
    args = parser.parse_args()
    root = Path(args.directory).resolve()

    sample_path = find_sample_html(root)
    sample_html = sample_path.read_text(encoding="utf-8", errors="replace")
    api_key = extract_api_key(sample_html)
    marker_icon = extract_marker_icon(sample_html)

    seen_urls, stats = collect_entries(root)
    markers = merge_colocated(seen_urls)

    out_path = root / OUTPUT_NAME
    out_path.write_text(build_html(api_key, marker_icon, markers), encoding="utf-8")

    print(f"Sample template: {sample_path.name}")
    print(f"Files scanned: {stats['files_scanned']}")
    print(f"Source map files used: {stats['files_used']}")
    print(f"Segments seen: {stats['segments_total']}")
    print(f"  skipped (no img): {stats['segments_no_img']}")
    print(f"  skipped (no href): {stats['segments_no_href']}")
    print(f"  duplicates skipped: {stats['duplicates_skipped']}")
    print(f"Unique photos: {len(seen_urls)}")
    print(f"Markers after co-locate merge: {len(markers)}")
    print(f"Wrote {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
