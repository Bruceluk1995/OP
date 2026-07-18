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
FIXED_STORY_ROUTER_START = "<!-- FIXED_STORY_ROUTER_V1_START -->"
FIXED_STORY_ROUTER_END = "<!-- FIXED_STORY_ROUTER_V1_END -->"
FIXED_STORY_ROUTER_V1 = """```text
你想做哪种内容？

1. 长篇网文／持续连载
2. 短季分集小说／连续剧（默认首季6集）
3. 单篇短篇／一发完结
4. 视频讲解稿／知识科普
5. 已有作品处理：续写、改写、审查、去AI味、封面
6. 拆文／对标／扫榜／热点选题
7. 不确定，帮我选择

请回复数字。
```"""
TOPIC_GENERATING_SKILLS = {
    "story",
    "jp-isekai", "jp-isekai-plan", "jp-isekai-write", "jp-isekai-oneshot",
    "jp-josei-fantasy", "jp-josei-fantasy-plan", "jp-josei-fantasy-write", "jp-josei-fantasy-oneshot",
    "jp-short-fiction-studio", "silver-literature", "shanhe-explainer", "econ-finance-explainer",
    "story-long-write", "story-short-write", "story-long-scan", "story-short-scan",
    "story-first-person-script", "story-third-person-script",
}
PUSH_RETENTION_SKILLS = {
    "story",
    "jp-short-fiction-studio",
    "jp-isekai-oneshot", "jp-josei-fantasy-oneshot",
    "jp-isekai-write", "jp-josei-fantasy-write",
    "jp-isekai-review", "jp-josei-fantasy-review",
    "story-first-person-script", "story-third-person-script",
}
PUSH_ROUTE_LOCK_REQUIREMENTS = {
    "story": ("presentation=<traditional|push>", "raw menu code", "sticky state"),
    "jp-isekai": ("normalized handoff", "raw menu code", "Push is sticky", "cannot override `presentation=push`"),
    "jp-josei-fantasy": ("normalized handoff", "raw menu code", "Push is sticky"),
    "jp-isekai-oneshot": ("writer_branch=flan_push", "raw menu code", "sticky branch lock"),
    "jp-josei-fantasy-oneshot": ("writer_branch=flan_push", "raw menu code", "sticky branch lock"),
    "jp-short-fiction-studio": ("writer_branch=<traditional_scene|flan_push>", "raw menu code", "writer_branch=flan_push"),
}
PUSH_MODE_REFERENCE_REQUIREMENTS = {
    "jp-isekai": ("push-prompt-architecture.md", "push-entertainment-gate.md", "push-retention-chain.md", "A raw menu code has no meaning", "never a pronoun swap"),
    "jp-josei-fantasy": ("push-prompt-architecture.md", "push-entertainment-gate.md", "push-retention-chain.md", "A raw menu code has no meaning", "never a pronoun swap"),
}
LEGACY_PUSH_DRIFT_PATTERNS = (
    "First person changes only pronouns and knowledge boundaries",
    "intimacy changes pronouns and knowledge only",
    "Push mode uses the fixed-template random draw",
    "select exactly one branch: Traditional Scene Writer or Flan-Style Push Narrator",
    "turn/causal connector density is below one per 12 lines",
    "每300字至少一次自我拆台",
    "一句一段≥70%",
)
PUSH_GLOBAL_CHAIN_REQUIREMENTS = (
    "Global Production Prompt Contract",
    "Push Prompt Architecture",
    "Speaker and Listener Contract",
    "Audience Emotional Contract",
    "one-listener test",
    "neutral event-log version",
    "emotional job",
    "Push Entertainment Gate",
    "expand / one-line bridge / cut",
    "first low-value event expanded too far",
    "post-final-payoff share",
    "spoken_units_per_1000_chars",
    "Hide the production process",
    "high_value_event_selection_verdict",
)
PUSH_VIEWPOINT_GATE_REQUIREMENTS = (
    "Selection pass",
    "Uniform-depth test",
    "High-point rotation test",
    "Production-leak test",
    "Speaker/listener test",
    "Emotional-job test",
    "Human-heat test",
    "Flowchart/procedure-run test",
    "Decisive-voice test",
    "Payoff-placement test",
    "Post-payoff-tail test",
    "Audio-only test",
    "Over-fragmentation test",
    "Connector-stuffing test",
)


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


def fixed_story_router_problem(text: str) -> str | None:
    """Return a blocking reason when the user-owned story entry contract drifts."""
    if text.count(FIXED_STORY_ROUTER_START) != 1 or text.count(FIXED_STORY_ROUTER_END) != 1:
        return "story router must contain exactly one frozen v1 marker pair"
    start = text.index(FIXED_STORY_ROUTER_START) + len(FIXED_STORY_ROUTER_START)
    end = text.index(FIXED_STORY_ROUTER_END, start)
    actual = text[start:end].strip()
    if actual != FIXED_STORY_ROUTER_V1:
        return "frozen story entry menu changed; user authorization is required to alter names, order, or options"
    return None


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
    if skill == "story":
        router_problem = fixed_story_router_problem(text)
        if router_problem:
            add(findings, "ERROR", skill, "fixed_router_drift", router_problem)
        prompt_architecture_file = skill_dir / "references" / "push-prompt-architecture.md"
        retention_file = skill_dir / "references" / "push-retention-chain.md"
        entertainment_file = skill_dir / "references" / "push-entertainment-gate.md"
        validator_file = skill_dir / "scripts" / "validate-flan-push.py"
        combined = ""
        for required_file in (prompt_architecture_file, entertainment_file, retention_file, validator_file):
            if not required_file.exists():
                add(findings, "ERROR", skill, "push_global_chain_file_missing", str(required_file))
                continue
            combined += required_file.read_text(encoding="utf-8")
        for required in PUSH_GLOBAL_CHAIN_REQUIREMENTS:
            if required not in combined:
                add(
                    findings,
                    "ERROR",
                    skill,
                    "push_global_chain_contract_missing",
                    f"shared push production chain must preserve token: {required}",
                )
    if skill == "jp-short-fiction-studio" and "High-Value Event Scanner" not in text:
        add(
            findings,
            "ERROR",
            skill,
            "push_high_value_scanner_missing",
            "studio push chain must include the High-Value Event Scanner role",
        )
    if skill == "jp-short-fiction-studio" and "Entertainment Editor" not in text:
        add(
            findings,
            "ERROR",
            skill,
            "push_entertainment_editor_missing",
            "studio push chain must include the Entertainment Editor role",
        )
    if skill in {"story-first-person-script", "story-third-person-script"}:
        gate_file = skill_dir / "references" / "push-quality-gate.md"
        if not gate_file.exists():
            add(findings, "ERROR", skill, "push_viewpoint_gate_missing", str(gate_file))
        else:
            gate_text = gate_file.read_text(encoding="utf-8")
            for required in PUSH_VIEWPOINT_GATE_REQUIREMENTS:
                if required not in gate_text:
                    add(
                        findings,
                        "ERROR",
                        skill,
                        "push_viewpoint_gate_contract_missing",
                        f"viewpoint release gate must preserve token: {required}",
                    )
    if skill in TOPIC_GENERATING_SKILLS and "global-topic-history.md" not in text:
        add(
            findings,
            "ERROR",
            skill,
            "global_topic_dedup_missing",
            "topic-generating skills must link the mandatory company-wide online topic gate",
        )
    if skill in PUSH_RETENTION_SKILLS and "push-retention-chain.md" not in text:
        add(
            findings,
            "ERROR",
            skill,
            "push_retention_chain_missing",
            "push entry, writing, viewpoint, and review skills must link the shared retention gate",
        )
    if skill in PUSH_RETENTION_SKILLS and "push-entertainment-gate.md" not in text:
        add(
            findings,
            "ERROR",
            skill,
            "push_entertainment_gate_missing",
            "push entry, writing, viewpoint, and review skills must link the shared entertainment gate",
        )
    if skill in PUSH_RETENTION_SKILLS and "push-prompt-architecture.md" not in text:
        add(
            findings,
            "ERROR",
            skill,
            "push_prompt_architecture_missing",
            "push entry, writing, viewpoint, and review skills must link the shared speaker/emotion prompt architecture",
        )
    for required in PUSH_ROUTE_LOCK_REQUIREMENTS.get(skill, ()):
        if required.lower() not in text.lower():
            add(
                findings,
                "ERROR",
                skill,
                "push_route_lock_missing",
                f"SKILL.md must preserve normalized sticky push routing token: {required}",
            )

    mode_requirements = PUSH_MODE_REFERENCE_REQUIREMENTS.get(skill, ())
    if mode_requirements:
        mode_file = skill_dir / "references" / "presentation-modes.md"
        if not mode_file.exists():
            add(findings, "ERROR", skill, "presentation_modes_missing", "references/presentation-modes.md is required")
        else:
            mode_text = mode_file.read_text(encoding="utf-8")
            for required in mode_requirements:
                if required.lower() not in mode_text.lower():
                    add(
                        findings,
                        "ERROR",
                        skill,
                        "push_mode_lock_missing",
                        f"presentation-modes.md must preserve push lock token: {required}",
                    )

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
        for pattern in LEGACY_PUSH_DRIFT_PATTERNS:
            if pattern in markdown_text:
                add(findings, "ERROR", skill, "legacy_push_drift", f"{source} contains legacy push drift: {pattern}")
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
