#!/usr/bin/env python3
"""Summarize subtitle corpus length, languages, markers, and openings."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path


LANG_RE = re.compile(r"\.ai-([a-z]{2})\.txt$")
MARKERS = ("这就是", "核心", "本质", "所以", "恰恰", "说白了", "问题是", "但问题是", "换句话说")


def clean_lines(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser(description="Profile a multilingual subtitle corpus.")
    parser.add_argument("root")
    parser.add_argument("--samples", type=int, default=12)
    args = parser.parse_args()

    root = Path(args.root)
    files = [p for p in root.rglob("*.txt") if p.is_file()]
    languages: Counter[str] = Counter()
    categories: Counter[str] = Counter()
    zh_rows: list[tuple[int, str, Path, list[str]]] = []
    marker_counts: Counter[str] = Counter()

    for path in files:
        match = LANG_RE.search(path.name)
        lang = match.group(1) if match else "unknown"
        languages[lang] += 1
        try:
            rel = path.relative_to(root)
        except ValueError:
            rel = path
        categories[rel.parts[0] if len(rel.parts) > 1 else root.name] += 1
        if lang != "zh":
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        lines = clean_lines(text)
        char_count = sum(len(line) for line in lines)
        for marker in MARKERS:
            marker_counts[marker] += text.count(marker)
        title = path.name.split(".字幕", 1)[0]
        zh_rows.append((char_count, title, rel, lines[:10]))

    print(f"root={root}")
    print(f"files={len(files)}")
    print("languages:")
    for lang, count in languages.most_common():
        print(f"- {lang}: {count}")
    print("categories:")
    for cat, count in categories.most_common():
        print(f"- {cat}: {count}")
    if zh_rows:
        lengths = [row[0] for row in zh_rows]
        print(f"zh_count={len(zh_rows)} min={min(lengths)} avg={sum(lengths)//len(lengths)} max={max(lengths)}")
    print("markers:")
    for marker, count in marker_counts.most_common():
        print(f"- {marker}: {count}")
    print("top_long:")
    for char_count, title, rel, _ in sorted(zh_rows, reverse=True)[: args.samples]:
        print(f"- {char_count}: {rel.parent.as_posix()}/{title}")
    print("opening_samples:")
    for char_count, title, rel, lines in zh_rows[: args.samples]:
        print(f"- [{rel.parent.as_posix()}] {title} ({char_count}) :: {' / '.join(lines[:8])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
