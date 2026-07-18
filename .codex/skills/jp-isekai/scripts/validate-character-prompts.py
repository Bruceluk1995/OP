#!/usr/bin/env python3
"""Validate Japanese male-isekai character mother prompts."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ASCII_RE = re.compile(r"[A-Za-z]")
HEADING_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
AGE_RE = re.compile(r"(?:\d+|[一二三四五六七八九十百]+)歳|年齢不詳")
HAIR_RE = re.compile(r"髪|毛並み|鬣|鱗")
EYE_RE = re.compile(r"瞳|眼|複眼")
HELD_PROP_PATTERNS = {
    "symbolic possession": re.compile(r"象徴的な(?:持ち物|道具|武器)|持ち物は"),
    "held object": re.compile(r"(?:手に|両手で|片手で).{0,16}(?:持|握|掲|構)"),
    "carried object": re.compile(r"(?:携える|携帯している|背負っている|腰に.{0,12}(?:剣|刀|杖|弓|斧|槍|道具))"),
    "temporary effect": re.compile(r"(?:発動時|魔法効果|オーラ|光輪|光粒|同心円状の音波|炎を灯した)"),
    "scene direction": re.compile(r"(?:カメラ|構図|背景場面|画面の中|本集重点姿態|封面構図|適合封面姿態)"),
}


def sections(text: str) -> list[tuple[str, str]]:
    matches = list(HEADING_RE.finditer(text))
    result: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        name = match.group(1).strip()
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        if name not in {"使用ルール", "共通画風", "複数人物を同時に描く場合の統一条件"}:
            result.append((name, body))
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Japanese character mother prompts")
    parser.add_argument("prompt_file", type=Path)
    args = parser.parse_args()

    path = args.prompt_file.resolve()
    if not path.exists():
        print(f"ERROR missing prompt file: {path}")
        return 1

    text = path.read_text(encoding="utf-8")
    findings: list[str] = []

    if "## 共通画風" not in text:
        findings.append("missing shared ## 共通画風 section")
    if ASCII_RE.search(text):
        findings.append("ASCII letters found; prompt asset must be Japanese-only")

    character_sections = sections(text)
    if not character_sections:
        findings.append("no character sections found")

    for name, body in character_sections:
        paragraphs = [part for part in re.split(r"\n\s*\n", body) if part.strip()]
        if len(paragraphs) != 1:
            findings.append(f"{name}: expected one copyable paragraph, found {len(paragraphs)}")
        if not AGE_RE.search(body):
            findings.append(f"{name}: missing age or 年齢不詳")
        if not HAIR_RE.search(body):
            findings.append(f"{name}: missing hair/fur/scale identity")
        if not EYE_RE.search(body):
            findings.append(f"{name}: missing eye identity")
        for label, pattern in HELD_PROP_PATTERNS.items():
            if pattern.search(body):
                findings.append(f"{name}: {label} must move to a scene or cover prompt")

    if findings:
        for finding in findings:
            print(f"ERROR {finding}")
        print(f"character_prompt_contract=fail findings={len(findings)}")
        return 1

    print(f"character_prompt_contract=pass characters={len(character_sections)} file={path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
