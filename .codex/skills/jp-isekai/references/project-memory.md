# Project Memory Protocol

Use this protocol whenever `$jp-isekai-plan` or `$jp-isekai-write` is working inside a project, continuing an existing serial, saving episode files, or generating multiple similar concepts.

## Directory Contract

Treat the Japanese male-audience isekai suite as a specialization of the common story project layout:

```text
设定/
  题材定位.md
  角色/{角色名}.md
  势力/{势力名}.md
  世界观/{主题}.md
大纲/
  大纲.md
  卷纲_第X卷.md
  细纲_第XXX章.md
追踪/
  上下文.md
  伏笔.md
  时间线.md
  角色状态.md
episodes/
  第XXX話_<short-title>/
男频异世界知识库/
  generated-ledger.jsonl
  topic-history.jsonl
  type-packs/{lane}.md
对标/
  {lane}/{work}/拆文报告.md
拆文库/
```

Do not use chat memory as the source of truth when these files exist. Read the smallest set of files needed for the current chapter, but keep the project state on disk.

## Scale Contract

This suite still writes novel prose, not screenplay format. For YouTube narration, push-style serials, or user requests that say `短季`, `分集`, `每集`, or `6集`, use a bounded short-season novel scale:

- Use 6 episodes/chapters as the fixed first-season standard.
- Keep short-season planning at exactly 6 episodes/chapters.
- Use the same novel files: `大纲/细纲_第XXX章.md`, `episodes/第XXX話_<short-title>/`, and `追踪/`.
- Treat `第一卷` as `首季`; create a complete first-season arc, not a hundred-chapter webnovel roadmap.
- Do not plan beyond the first season unless the user explicitly asks for a long webnovel or future seasons.

## Planning Responsibilities

When creating a new serial or a new arc:

1. Create or update `设定/题材定位.md` with the target reader, subtype, emotional promise, core engine, and banned Chinese leakage.
2. Create or update `设定/角色/{主角}.md`, major companion files, major antagonist files, and reusable faction/world files.
3. Create `大纲/大纲.md`, `大纲/卷纲_第X卷.md`, and the first rolling batch of `大纲/细纲_第XXX章.md`.
4. Create `追踪/伏笔.md`, `追踪/时间线.md`, `追踪/角色状态.md`, and `追踪/上下文.md` if they do not exist.
5. After each outline batch, scan new recurring characters, factions, cheat rules, guild rules, dungeon rules, or economy rules and add only reusable ones to `设定/`.
6. For subtype work, load the best available benchmark first: project拆文 under `对标/{lane}/` or `拆文库/`, then fresh website benchmark cards if requested/needed, then project-specific `男频异世界知识库/type-packs/{lane}.md` notes, and bundled type packs only as fallback.

Each `细纲_第XXX章.md` should include: target emotion, episode promise, cause/development/turn/climax/ending state, dense/sparse beat budget, cheat experiment or public proof, cost/reward/status change, involved characters, and next hook.

## Benchmark Protocol

Each subtype may use a hot work only as a structural benchmark. Prefer dynamic拆书 over fixed bundled outlines:

- Prefer a project-owned analysis report under `对标/{lane}/{work}/拆文报告.md` or `拆文库/{work}/`.
- If no analysis exists and the user asks for current popular references, or if the lane has no strong project benchmark, browse public ranking/tag pages and create a dynamic benchmark card: premise lane, visible tags, payoff engine, opening pressure, progression/reward pattern, episode promise, and audience expectation.
- Do not copy titles, character names, factions, scene order, dialogue, or detailed proprietary outlines from any live work.
- Save source-specific dynamic benchmark cards as `对标/{lane}/_live-benchmark-{YYYYMMDD}.md`.
- Save project-specific benchmark notes as `男频异世界知识库/type-packs/{lane}.md` when they will affect future generation.
- If no benchmark is available, use the bundled type pack as the fallback and clearly mark it as a generic structural scaffold.

## Writing Preflight

Before drafting a saved episode/chapter:

1. Identify the active project root. Prefer the directory containing `追踪/` or `设定/`; otherwise use the current working directory.
2. Read the current chapter outline: `大纲/细纲_第XXX章.md`. If missing, stop and create the outline before prose.
3. Read the previous episode/chapter tail or full file when continuing.
4. Read `追踪/上下文.md`, `追踪/伏笔.md`, `追踪/时间线.md`, and the relevant slice of `追踪/角色状态.md`.
5. Read only the involved `设定/角色/`, `设定/势力/`, and `设定/世界观/` files.
6. Run the ledger summary and check the candidate engine before writing.

## After Writing

After saving prose or a packaged episode:

1. Update `追踪/伏笔.md` with new, advanced, or resolved hooks.
2. Update `追踪/时间线.md` with the episode's event order.
3. Update `追踪/角色状态.md` for identity, skill, relationship, money, public image, base, companion, or injury changes.
4. Update `追踪/上下文.md` with last completed episode/chapter, saved path, cover/package status, next outline status, and any continuation risk.
5. Add one compact record to `男频异世界知识库/generated-ledger.jsonl`.

## Anti-Homogenization Ledger

Use the project-wide `选题历史/global-topic-history.jsonl` as the first gate;
it tracks every dynamic seed shown by any story or explainer skill, including
rejected or unselected candidates. Use the male-isekai generated ledger as the
second, genre-specific engine check. Once a candidate is displayed, append it
to global topic history immediately. Prior topics remain burned by default
across sessions and domains.

Before generating a new concept, outline, title batch, or full episode, inspect the recent ledger:

```powershell
python .codex/skills/jp-isekai/scripts/ledger.py --root . summary
```

Check a candidate combination:

```powershell
python .codex/skills/jp-isekai/scripts/ledger.py --root . check --protagonist "追放された荷運び" --cheat "鑑定+修復" --pressure "ギルドの買い叩き" --payoff "薬草畑の価値証明" --venue "冒険者ギルド" --aftertaste "小さな拠点を得る"
```

After generation, append a record:

```powershell
python .codex/skills/jp-isekai/scripts/ledger.py --root . add --title "{title}" --protagonist "{protagonist}" --cheat "{cheat}" --pressure "{pressure}" --payoff "{payoff}" --venue "{venue}" --aftertaste "{aftertaste}" --path "{output_path}"
```

Avoid repeating three or more recent fields from the same record. If blocked, change at least two of: protagonist role, cheat engine, pressure source, payoff object, scene venue, aftertaste.
