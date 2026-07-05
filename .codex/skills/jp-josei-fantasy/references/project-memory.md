# Project Memory Protocol

Use this protocol whenever `$jp-josei-fantasy-plan` or `$jp-josei-fantasy-write` is working inside a project, continuing an existing serial, saving episode files, or generating multiple similar concepts.

## Directory Contract

Treat the Japanese female-audience fantasy romance suite as a specialization of the common story project layout:

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
  第XXX話_<short-title>/ or josei_epXX/
女频幻想恋爱知识库/
  generated-ledger.jsonl
  type-packs/{lane}.md
对标/
拆文库/
```

Benchmark files may also live under `瀵规爣/{lane}/{work}/鎷嗘枃鎶ュ憡.md` or `瀵规爣/{lane}/_live-benchmark-{YYYYMMDD}.md`.

Do not use chat memory as the source of truth when these files exist. Read the smallest set of files needed for the current chapter, but keep the project state on disk.

## Scale Contract

This suite still writes novel prose, not screenplay format. For YouTube narration, push-style serials, or user requests that say `短季`, `分集`, `每集`, or `6集`, use a bounded short-season novel scale:

- Use 6 episodes/chapters as the fixed first-season standard.
- Keep short-season planning at exactly 6 episodes/chapters.
- Use the same novel files: `大纲/细纲_第XXX章.md`, `episodes/第XXX話_<short-title>/` or `episodes/josei_epXX/`, and `追踪/`.
- Treat `第一卷` as `首季`; create a complete first-season romance/zamaa arc, not a hundred-chapter webnovel roadmap.
- Do not plan beyond the first season unless the user explicitly asks for a long webnovel or future seasons.

## Planning Responsibilities

When creating a new serial or a new arc:

1. Create or update `设定/题材定位.md` with tag cluster, reader promise, heroine wound, romance promise, zamaa promise, and banned leakage.
2. Create or update `设定/角色/{女主}.md`, `设定/角色/{男主}.md`, major antagonist files, house/faction files, and reusable church/court/world rules.
3. Create `大纲/大纲.md`, `大纲/卷纲_第X卷.md`, and the first rolling batch of `大纲/细纲_第XXX章.md`.
4. Create `追踪/伏笔.md`, `追踪/时间线.md`, `追踪/角色状态.md`, and `追踪/上下文.md` if they do not exist.
5. After each outline batch, scan new recurring characters, noble houses, contracts, church rules, inheritance rules, curse rules, evidence chains, and romance promises and add only reusable ones to `设定/`.

Each `细纲_第XXX章.md` should include: target emotion, social/emotional bomb, heroine choice, romance movement, zamaa/evidence movement, dense/sparse beat budget, cost/status consequence, involved characters, and next hook.

## Benchmark Protocol

Each subtype may use a hot work only as a structural benchmark. Prefer dynamic拆书 over fixed bundled outlines:

- Before creating a new subtype plan, load the best available benchmark first: project拆文 under `瀵规爣/{lane}/` or `鎷嗘枃搴?`, then fresh website benchmark cards if requested/needed, then project-specific `濂抽骞绘兂鎭嬬埍鐭ヨ瘑搴?/type-packs/{lane}.md` notes, and bundled type packs only as fallback.
- Prefer a project-owned analysis report under `瀵规爣/{lane}/{work}/鎷嗘枃鎶ュ憡.md` or `鎷嗘枃搴?{work}/`.
- If no analysis exists and the user asks for current popular references, or if the lane has no strong project benchmark, browse public ranking/tag pages and create a dynamic benchmark card: heroine wound, visible tags, romance engine, evidence/zamaa engine, social venue, male-lead recognition mode, episode promise, and audience expectation.
- Do not copy titles, character names, houses, factions, scene order, dialogue, or detailed proprietary outlines from any live work.
- Save source-specific dynamic benchmark cards as `瀵规爣/{lane}/_live-benchmark-{YYYYMMDD}.md`.
- Save project-specific benchmark notes as `濂抽骞绘兂鎭嬬埍鐭ヨ瘑搴?/type-packs/{lane}.md` when they will affect future generation.
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
3. Update `追踪/角色状态.md` for reputation, legal status, engagement, contract, family relation, romance progress, public image, injury, curse, or magic changes.
4. Update `追踪/上下文.md` with last completed episode/chapter, saved path, cover/package status, next outline status, and any continuation risk.
5. Add one compact record to `女频幻想恋爱知识库/generated-ledger.jsonl`.

## Anti-Homogenization Ledger

Before generating a new concept, outline, title batch, or full episode, inspect the recent ledger:

```powershell
python .codex/skills/jp-josei-fantasy/scripts/ledger.py --root . summary
```

Check a candidate combination:

```powershell
python .codex/skills/jp-josei-fantasy/scripts/ledger.py --root . check --heroine "偽聖女扱いの伯爵令嬢" --wound "婚約破棄" --romance "辺境伯の公的保護" --pressure "教会の証言操作" --proof "治癒記録" --venue "王宮審問" --aftertaste "名誉回復と新しい居場所"
```

After generation, append a record:

```powershell
python .codex/skills/jp-josei-fantasy/scripts/ledger.py --root . add --title "{title}" --heroine "{heroine}" --wound "{wound}" --romance "{romance}" --pressure "{pressure}" --proof "{proof}" --venue "{venue}" --aftertaste "{aftertaste}" --path "{output_path}"
```

Avoid repeating four or more recent fields from the same record. If blocked, change at least two of: heroine role, wound, romance engine, pressure source, proof object, reversal venue, aftertaste.
