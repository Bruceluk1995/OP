#!/usr/bin/env python3
"""Audit a Codex skill bundle using only the Python standard library."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)
FIELD_RE = re.compile(r"^([A-Za-z0-9_-]+):\s*(.*)$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


@dataclass(frozen=True)
class Finding:
    severity: str
    skill: str
    code: str
    message: str


def scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        value = value[1:-1]
    return value


def parse_frontmatter(text: str) -> dict[str, str] | None:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        item = FIELD_RE.match(line)
        if item:
            fields[item.group(1)] = scalar(item.group(2))
    return fields


def add(findings: list[Finding], severity: str, skill: str, code: str, message: str) -> None:
    findings.append(Finding(severity, skill, code, message))


def audit_skill(skill_dir: Path) -> list[Finding]:
    findings: list[Finding] = []
    skill = skill_dir.name
    skill_md = skill_dir / "SKILL.md"
    try:
        text = skill_md.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        add(findings, "ERROR", skill, "invalid_utf8", str(exc))
        return findings

    fields = parse_frontmatter(text)
    if fields is None:
        add(findings, "ERROR", skill, "frontmatter_missing", "SKILL.md must start with YAML frontmatter")
        return findings

    name = fields.get("name", "")
    description = fields.get("description", "")
    if not name:
        add(findings, "ERROR", skill, "name_missing", "frontmatter is missing name")
    elif name != skill:
        add(findings, "ERROR", skill, "name_mismatch", f"frontmatter name is {name!r}")
    if not description:
        add(findings, "ERROR", skill, "description_missing", "frontmatter is missing description")
    elif len(description) > 600:
        add(findings, "WARN", skill, "description_long", f"description is {len(description)} characters")
    metadata = fields.get("metadata", "")
    if not metadata or '"openclaw"' not in metadata:
        add(findings, "WARN", skill, "openclaw_metadata_missing", "cross-platform bundle requires single-line metadata.openclaw")

    line_count = len(text.splitlines())
    if line_count > 500:
        add(findings, "WARN", skill, "skill_md_long", f"SKILL.md has {line_count} lines; move details to references")
    if "\ufffd" in text:
        add(findings, "ERROR", skill, "replacement_character", "SKILL.md contains Unicode replacement characters")
    if re.search(r"\b(?:TODO|FIXME)\b", text):
        add(findings, "WARN", skill, "unfinished_marker", "SKILL.md contains TODO/FIXME")

    for markdown in sorted(skill_dir.rglob("*.md")):
        if markdown == skill_md:
            markdown_text = text
        else:
            try:
                markdown_text = markdown.read_text(encoding="utf-8")
            except UnicodeDecodeError as exc:
                source = markdown.relative_to(skill_dir).as_posix()
                add(findings, "ERROR", skill, "invalid_utf8", f"{source}: {exc}")
                continue
        source = markdown.relative_to(skill_dir).as_posix()
        if "\ufffd" in markdown_text:
            add(findings, "ERROR", skill, "replacement_character", f"{source} contains Unicode replacement characters")
        for target in LINK_RE.findall(markdown_text):
            target = target.strip().strip("<>").split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if any(mark in target for mark in ("{", "}", "*")):
                continue
            linked = (markdown.parent / target).resolve()
            if not linked.exists():
                add(findings, "ERROR", skill, "broken_link", f"{source}: missing linked resource {target}")

    openai_yaml = skill_dir / "agents" / "openai.yaml"
    if not openai_yaml.exists():
        add(findings, "WARN", skill, "openai_yaml_missing", "agents/openai.yaml is missing")
    else:
        yaml_text = openai_yaml.read_text(encoding="utf-8")
        display_match = re.search(r'^\s*display_name:\s*["\'](.*)["\']\s*$', yaml_text, re.MULTILINE)
        short_match = re.search(r'^\s*short_description:\s*["\'](.*)["\']\s*$', yaml_text, re.MULTILINE)
        prompt_match = re.search(r'^\s*default_prompt:\s*["\'](.*)["\']\s*$', yaml_text, re.MULTILINE)
        if not display_match or not display_match.group(1).strip():
            add(findings, "ERROR", skill, "display_name_missing", "openai.yaml lacks a quoted display_name")
        if not short_match:
            add(findings, "ERROR", skill, "short_description_missing", "openai.yaml lacks a quoted short_description")
        elif not 25 <= len(short_match.group(1)) <= 64:
            add(findings, "WARN", skill, "short_description_length", f"short_description is {len(short_match.group(1))} characters; expected 25-64")
        if not prompt_match:
            add(findings, "ERROR", skill, "default_prompt_missing", "openai.yaml lacks a quoted default_prompt")
        elif f"${skill}" not in prompt_match.group(1):
            add(findings, "ERROR", skill, "default_prompt_skill_missing", f"default_prompt must mention ${skill}")
        if "\ufffd" in yaml_text:
            add(findings, "ERROR", skill, "openai_yaml_replacement_character", "openai.yaml contains Unicode replacement characters")

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit every immediate child skill folder")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--strict", action="store_true", help="Return non-zero when warnings exist")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    args = parser.parse_args()

    root = args.root.resolve()
    skill_dirs = sorted(path for path in root.iterdir() if path.is_dir() and (path / "SKILL.md").exists())
    findings = [finding for path in skill_dirs for finding in audit_skill(path)]

    if args.json:
        print(json.dumps({"root": str(root), "skills": len(skill_dirs), "findings": [asdict(f) for f in findings]}, ensure_ascii=False, indent=2))
    else:
        for finding in findings:
            print(f"{finding.severity:<5} {finding.skill:<28} {finding.code}: {finding.message}")
        errors = sum(f.severity == "ERROR" for f in findings)
        warnings = sum(f.severity == "WARN" for f in findings)
        print(f"Audited {len(skill_dirs)} skills: {errors} error(s), {warnings} warning(s).")

    has_errors = any(f.severity == "ERROR" for f in findings)
    has_warnings = any(f.severity == "WARN" for f in findings)
    return 1 if has_errors or (args.strict and has_warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
