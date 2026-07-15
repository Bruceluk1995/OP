#!/usr/bin/env python3
"""Project-wide character-name ledger and Japanese name-style validator."""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

import company_dedup


LEDGER = Path("角色名历史") / "character-name-history.jsonl"
SEPARATORS_RE = re.compile(r"[・･·\s]+")
PARENS_RE = re.compile(r"\s*[（(【\[].*?[）)】\]]\s*$")
GENERIC_HEADINGS = {
    "角色提示词",
    "角色设定",
    "character prompts",
    "characters",
    "主要角色",
}
GENERIC_TOKENS = {
    "档案",
    "信息",
    "分析",
    "风格",
    "记录",
    "关系",
    "速览",
    "关键",
    "画风",
    "禁用",
    "情节",
    "别名",
    "表现",
    "提示词",
}
ROLE_PREFIXES = ("国王", "王太后", "王妃", "皇帝", "魔将", "魔砲獣", "深海竜")
ROLE_SUFFIXES = (
    "第二王子",
    "第一王子",
    "王太子",
    "王弟殿下",
    "辺境伯",
    "公爵令嬢",
    "侯爵令嬢",
    "伯爵令嬢",
    "子爵令嬢",
    "男爵令嬢",
    "公爵",
    "侯爵",
    "伯爵",
    "子爵",
    "男爵",
    "殿下",
    "陛下",
    "商会長",
    "队长",
)
ROLE_ONLY_TOKENS = (
    "査定官",
    "槍使い",
    "墓守騎士",
    "呪詛箱",
    "方舟都市",
    "関係",
    "关系",
)


def configure_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def ledger_path(root: str) -> Path:
    return Path(root).resolve() / LEDGER


def kata(text: str) -> str:
    out: list[str] = []
    for char in text:
        code = ord(char)
        if 0x3041 <= code <= 0x3096:
            out.append(chr(code + 0x60))
        else:
            out.append(char)
    return "".join(out)


def clean_name(name: str) -> str:
    name = unicodedata.normalize("NFKC", name).strip().strip("#*- ")
    name = re.split(r"[|｜/]", name, maxsplit=1)[0].strip()
    name = PARENS_RE.sub("", name)
    for prefix in ROLE_PREFIXES:
        if name.startswith(prefix):
            name = name[len(prefix) :]
    changed = True
    while changed:
        changed = False
        for suffix in ROLE_SUFFIXES:
            if name.endswith(suffix):
                name = name[: -len(suffix)].strip()
                changed = True
                break
    return name.strip("：:。.")


def name_keys(name: str) -> tuple[str, str]:
    cleaned = clean_name(name)
    parts = [kata(part) for part in SEPARATORS_RE.split(cleaned) if part]
    full_key = "".join(parts).casefold()
    fantasy_given_key = parts[0].casefold() if len(parts) >= 2 else full_key
    return full_key, fantasy_given_key


def load(path: Path) -> list[dict]:
    if not path.exists():
        return []
    records: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError:
            records.append({"_invalid": line})
    return records


def compact_len(name: str) -> int:
    return len(SEPARATORS_RE.sub("", clean_name(name)))


def style_findings(name: str, style: str) -> list[tuple[str, str]]:
    cleaned = clean_name(name)
    parts = [part for part in SEPARATORS_RE.split(cleaned) if part]
    findings: list[tuple[str, str]] = []
    if style == "jp-female-fantasy":
        if len(parts) > 2:
            findings.append(("BLOCK", "female fantasy names may have at most two segments"))
        if parts and len(parts[0]) > 6:
            findings.append(("BLOCK", "female fantasy given name exceeds 6 characters"))
        if compact_len(cleaned) > 10:
            findings.append(("BLOCK", "female fantasy display name exceeds 10 characters"))
        if len(parts) == 2 and len(parts[1]) > 5:
            findings.append(("WARN", "shorten the house name to 3-5 characters when possible"))
    elif style == "jp-male-fantasy":
        if len(parts) > 2:
            findings.append(("WARN", "male fantasy display names should normally use at most two segments"))
        if parts and len(parts[0]) > 7:
            findings.append(("WARN", "male fantasy given name is long for repeated narration"))
        if compact_len(cleaned) > 13:
            findings.append(("WARN", "use a shorter everyday call name"))
    elif style == "jp-modern":
        if "・" in cleaned:
            findings.append(("WARN", "modern Japanese names normally use kanji/kana without a middle dot"))
    return findings


def distance(a: str, b: str) -> int:
    if a == b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)
    previous = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        current = [i]
        for j, cb in enumerate(b, 1):
            current.append(min(current[-1] + 1, previous[j] + 1, previous[j - 1] + (ca != cb)))
        previous = current
    return previous[-1]


def check_name(records: list[dict], name: str, work: str, style: str, root: Path) -> int:
    cleaned = clean_name(name)
    full_key, given_key = name_keys(cleaned)
    same_work = [
        record
        for record in records
        if record.get("work") == work
        and (record.get("full_key") == full_key or record.get("given_key") == given_key)
    ]
    if same_work:
        print(f"name={cleaned} full_key={full_key} given_key={given_key} style={style or '-'}")
        print("OK: existing character in the same work; continuation reuse is allowed.")
        return 0
    blocked: list[dict] = []
    warnings: list[dict] = []
    for record in records:
        prior_full = record.get("full_key", "")
        prior_given = record.get("given_key", "")
        if full_key and (full_key == prior_full or given_key == prior_given):
            blocked.append(record)
        elif len(given_key) >= 3 and prior_given and distance(given_key, prior_given) <= 1:
            warnings.append(record)
    style_items = style_findings(cleaned, style)
    print(f"name={cleaned} full_key={full_key} given_key={given_key} style={style or '-'}")
    for level, message in style_items:
        print(f"{level}: {message}")
    for record in blocked:
        print(
            "BLOCK: reused by another work: "
            f"{record.get('name')} | {record.get('work')} | {record.get('role')}"
        )
    for record in warnings[:5]:
        print(
            "WARN: near-duplicate sound/spelling: "
            f"{record.get('name')} | {record.get('work')} | {record.get('role')}"
        )
    if blocked or any(level == "BLOCK" for level, _ in style_items):
        return 2
    company = company_dedup.reserve(
        kind="character",
        fingerprint="character|" + given_key,
        work_id=company_dedup.work_id_for(root, work),
        label=cleaned,
        tags=[style] if style else [],
        source="story-character-names",
        metadata={"full_key": full_key, "given_key": given_key},
        status="presented",
    )
    if not company.get("reserved"):
        print(
            "BLOCK: reused by another company work: "
            f"{company.get('existing_work_id', '?')} | {company.get('existing_status', '?')}"
        )
        return 2
    if company.get("provisional"):
        print("WARN: company server unavailable; name is provisionally reserved in the offline queue.")
    print("OK: name is available.")
    return 0


def infer_work(path: Path, root: Path) -> str:
    relative = path.relative_to(root)
    parts = relative.parts
    if "oneshots" in parts:
        index = parts.index("oneshots")
        if index + 1 < len(parts):
            return parts[index + 1]
    if "episodes" in parts:
        index = parts.index("episodes")
        if index + 1 < len(parts):
            return parts[index + 1]
    stem = path.stem
    for suffix in ("_角色提示词", "-character-prompts", "_character_prompts"):
        if stem.endswith(suffix):
            return stem[: -len(suffix)]
    return path.parent.name or root.name


def extract_prompt_names(path: Path) -> list[str]:
    names: list[str] = []
    text = path.read_text(encoding="utf-8", errors="replace")
    for line in text.splitlines():
        match = re.match(r"^##\s+(.+?)\s*$", line)
        if not match:
            continue
        name = clean_name(match.group(1))
        if (
            not name
            or name.casefold() in GENERIC_HEADINGS
            or any(token in name for token in GENERIC_TOKENS)
            or len(name) > 20
            or re.fullmatch(r"[A-Za-z0-9 _.-]+", name)
        ):
            continue
        names.append(name)
    return names


def valid_import_name(name: str) -> bool:
    return bool(
        name
        and not any(token in name for token in GENERIC_TOKENS)
        and not any(token in name for token in ROLE_ONLY_TOKENS)
        and len(name) <= 20
    )


def append_record(path: Path, record: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def import_existing(root: Path, path: Path, records: list[dict], rebuild: bool) -> None:
    if rebuild and path.exists():
        preserved = [item for item in records if item.get("domain") != "imported-existing"]
        path.parent.mkdir(parents=True, exist_ok=True)
        content = "".join(json.dumps(item, ensure_ascii=False) + "\n" for item in preserved)
        path.write_text(content, encoding="utf-8", newline="\n")
        records = preserved
    known = {(item.get("work"), item.get("full_key")) for item in records}
    imported = 0
    candidates: set[Path] = set()
    for markdown in root.rglob("*.md"):
        lowered = markdown.name.casefold()
        parent = markdown.parent.name
        if "角色提示词" in markdown.as_posix() or "character_prompt" in lowered or parent in {"角色", "characters"}:
            candidates.add(markdown)
    for markdown in sorted(candidates):
        work = infer_work(markdown, root)
        if markdown.parent.name in {"角色", "characters"}:
            names = [clean_name(markdown.stem)]
        else:
            names = extract_prompt_names(markdown)
        for name in names:
            if not valid_import_name(name):
                continue
            full_key, given_key = name_keys(name)
            if not full_key or (work, full_key) in known:
                continue
            append_record(
                path,
                {
                    "date": date.today().isoformat(),
                    "domain": "imported-existing",
                    "work": work,
                    "role": "unknown",
                    "name": name,
                    "full_key": full_key,
                    "given_key": given_key,
                    "source": str(markdown.relative_to(root)),
                },
            )
            known.add((work, full_key))
            imported += 1
    print(f"imported={imported} ledger={path}")


def sync_company(records: list[dict], root: Path) -> int:
    synced = 0
    conflicts = 0
    for record in records:
        name = str(record.get("name", "")).strip()
        work = str(record.get("work", "")).strip()
        if not name or not work:
            continue
        _, given_key = name_keys(name)
        result = company_dedup.reserve(
            kind="character",
            fingerprint="character|" + given_key,
            work_id=company_dedup.work_id_for(root, work),
            label=name,
            source=str(record.get("source", "history-import")),
            metadata={"role": record.get("role", ""), "domain": record.get("domain", "")},
            status="generated",
        )
        if result.get("reserved"):
            synced += 1
        else:
            conflicts += 1
    print(f"company_sync={synced} conflicts={conflicts}")
    return 2 if conflicts else 0


def main() -> int:
    configure_stdio()
    parser = argparse.ArgumentParser(description="Manage the project-wide character-name ledger")
    parser.add_argument("--root", default=".")
    sub = parser.add_subparsers(dest="command", required=True)

    p_import = sub.add_parser("import-existing")
    p_import.add_argument("--rebuild", action="store_true")
    p_summary = sub.add_parser("summary")
    p_summary.add_argument("--limit", type=int, default=30)
    sub.add_parser("sync-company")

    p_check = sub.add_parser("check")
    p_check.add_argument("--work", required=True)
    p_check.add_argument("--name", required=True)
    p_check.add_argument("--style", choices=("", "jp-female-fantasy", "jp-male-fantasy", "jp-modern"), default="")

    p_add = sub.add_parser("add")
    p_add.add_argument("--domain", required=True)
    p_add.add_argument("--work", required=True)
    p_add.add_argument("--role", required=True)
    p_add.add_argument("--name", required=True)
    p_add.add_argument("--source", default="generated")
    p_add.add_argument("--force", action="store_true")

    args = parser.parse_args()
    root = Path(args.root).resolve()
    path = ledger_path(args.root)
    records = load(path)

    if args.command == "import-existing":
        import_existing(root, path, records, args.rebuild)
        return 0
    if args.command == "summary":
        recent = records[-args.limit :]
        print(f"ledger_records={len(records)} recent={len(recent)}")
        for item in recent:
            print(f"- {item.get('name')} | {item.get('work')} | {item.get('role')} | {item.get('domain')}")
        return 0
    if args.command == "sync-company":
        return sync_company(records, root)
    if args.command == "check":
        return check_name(records, args.name, args.work, args.style, root)
    if args.command == "add":
        if not args.force:
            result = check_name(records, args.name, args.work, "", root)
            if result:
                return result
        full_key, given_key = name_keys(args.name)
        if any(item.get("work") == args.work and item.get("full_key") == full_key for item in records):
            print("OK: already recorded for this work.")
            return 0
        append_record(
            path,
            {
                "date": date.today().isoformat(),
                "domain": args.domain,
                "work": args.work,
                "role": args.role,
                "name": clean_name(args.name),
                "full_key": full_key,
                "given_key": given_key,
                "source": args.source,
            },
        )
        sync_result = company_dedup.commit(
            kind="character",
            fingerprint="character|" + given_key,
            work_id=company_dedup.work_id_for(root, args.work),
            status="selected",
        )
        print(f"added: {path}")
        if not sync_result.get("synced"):
            print("WARN: company status update queued for later sync.")
        return 0
    raise AssertionError(args.command)


if __name__ == "__main__":
    raise SystemExit(main())
