#!/usr/bin/env python3
"""Preview Google Trends RSS items for JP josei fantasy romance ideation."""

from __future__ import annotations

import argparse
import html
import sys
import urllib.request
import xml.etree.ElementTree as ET


def configure_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def fetch(url: str) -> bytes:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; CodexSkill/1.0; +https://trends.google.com/)"
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read()


def text_of(item: ET.Element, tag: str) -> str:
    found = item.find(tag)
    return html.unescape((found.text or "").strip()) if found is not None else ""


def main() -> int:
    configure_stdio()
    parser = argparse.ArgumentParser(description="Preview Google Trends RSS items.")
    parser.add_argument("--geo", default="JP", help="Google Trends geo code, default JP.")
    parser.add_argument("--limit", type=int, default=30)
    args = parser.parse_args()

    url = f"https://trends.google.com/trending/rss?geo={args.geo}"
    try:
        data = fetch(url)
    except Exception as exc:  # pragma: no cover - network dependent
        print(f"ERROR fetching {url}: {exc}", file=sys.stderr)
        return 2

    root = ET.fromstring(data)
    channel = root.find("channel")
    if channel is None:
        print("No RSS channel found.", file=sys.stderr)
        return 1

    print(f"source={url}")
    for index, item in enumerate(channel.findall("item")[: args.limit], start=1):
        title = text_of(item, "title")
        traffic = text_of(item, "{https://trends.google.com/trending/rss}approx_traffic")
        pub_date = text_of(item, "pubDate")
        description = text_of(item, "description")
        print(f"{index}. {title}")
        if traffic:
            print(f"   traffic={traffic}")
        if pub_date:
            print(f"   pubDate={pub_date}")
        if description:
            print(f"   description={description[:180]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
