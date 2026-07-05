#!/usr/bin/env python3
"""Profile subtitle folders for shanhe-explainer style work."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path


SUFFIX_RE = re.compile(r"\.字幕\.ai-([a-z]+)\.txt$", re.IGNORECASE)
MARKERS = (
    "所以",
    "核心",
    "这就是",
    "本质",
    "问题是",
    "但问题是",
    "恰恰",
    "你会发现",
    "换句话说",
    "说白了",
)


def read_text(path: Path) -> str:
    for encoding in ("utf-8-sig", "utf-8", "gb18030"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    return path.read_text(errors="ignore")


def main() -> int:
    parser = argparse.ArgumentParser(description="Profile a subtitle corpus.")
    parser.add_argument("root", help="Folder containing subtitle files.")
    parser.add_argument("--lang", default="zh", help="Subtitle language suffix to sample.")
    parser.add_argument("--samples", type=int, default=12)
    args = parser.parse_args()

    root = Path(args.root).resolve()
    files = [p for p in root.rglob("*.txt") if p.is_file()]
    by_lang: Counter[str] = Counter()
    by_category: Counter[str] = Counter()
    lengths: list[tuple[int, Path]] = []
    marker_counts: Counter[str] = Counter()
    samples: list[tuple[str, str, int, str]] = []

    for path in files:
        match = SUFFIX_RE.search(path.name)
        if not match:
            continue
        lang = match.group(1).lower()
        by_lang[lang] += 1
        by_category[path.parent.name] += 1
        if lang != args.lang:
            continue
        text = read_text(path)
        lengths.append((len(text), path))
        for marker in MARKERS:
            marker_counts[marker] += text.count(marker)
        first_lines = [line.strip() for line in text.splitlines() if line.strip()][:8]
        title = SUFFIX_RE.sub("", path.name)
        samples.append((path.parent.name, title, len(text), " / ".join(first_lines)))

    print(f"root={root}")
    print(f"files={len(files)}")
    print("languages:")
    for key, count in by_lang.most_common():
        print(f"- {key}: {count}")
    print("categories:")
    for key, count in by_category.most_common():
        print(f"- {key}: {count}")
    if lengths:
        values = sorted(length for length, _ in lengths)
        avg = sum(values) / len(values)
        print(f"{args.lang}_count={len(values)} min={values[0]} avg={avg:.0f} max={values[-1]}")
    print("markers:")
    for key, count in marker_counts.most_common():
        print(f"- {key}: {count}")
    print("top_long:")
    for length, path in sorted(lengths, key=lambda item: item[0], reverse=True)[: args.samples]:
        print(f"- {length}: {path.parent.name}/{SUFFIX_RE.sub('', path.name)}")
    print("opening_samples:")
    for category, title, length, first in samples[: args.samples]:
        print(f"- [{category}] {title} ({length}) :: {first}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
