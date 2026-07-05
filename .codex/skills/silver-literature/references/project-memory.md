# Project Memory Protocol

Use this protocol whenever `$silver-literature` is working inside a project, continuing an existing serial, saving story files, or generating multiple similar concepts.

## Directory Contract

Treat silver literature as a specialization of the common story project layout:

```text
设定/
  题材定位.md
  角色/{角色名}.md
  家族/{家族名}.md
  世界观/{主题}.md
大纲/
  大纲.md
  卷纲_第1卷.md
  细纲_第001章.md
追踪/
  上下文.md
  伏笔.md
  时间线.md
  角色状态.md
episodes/
银发文学知识库/
  generated-ledger.jsonl
  type-packs/{lane}.md
对标/
  {lane}/{work}/拆文报告.md
  {lane}/_live-benchmark-{YYYYMMDD}.md
拆文库/
```

Do not use chat memory as the source of truth when these files exist. Read the smallest set of files needed for the current story, but keep the project state on disk.

## Scale Contract

This suite writes novel/narration prose, not screenplay format.

- Single story: use `小节大纲.md`, `正文.md`, and `银发文学知识库/generated-ledger.jsonl`.
- Short-season serial: use fixed 6 episodes/chapters with `大纲/细纲_第XXX章.md`, `episodes/`, and `追踪/`.
- Treat the first season as a complete dignity/reversal/recovery arc, not a hundred-chapter roadmap.
- Do not plan beyond the first season unless the user explicitly asks for a long webnovel or future seasons.

## Planning Responsibilities

When creating a new story or arc:

1. Create or update `设定/题材定位.md` with target reader, lane, emotional promise, proof engine, dignity payoff, and banned sensationalism.
2. Create or update protagonist, antagonist, witness, family/company/facility, and reusable legal/medical/financial rule files.
3. Create `大纲/大纲.md`, `大纲/卷纲_第1卷.md`, and the first rolling batch of `大纲/细纲_第XXX章.md` for serialized work.
4. Create `追踪/伏笔.md`, `追踪/时间线.md`, `追踪/角色状态.md`, and `追踪/上下文.md` if they do not exist.
5. For subtype work, load the best available benchmark first: project拆文 under `对标/{lane}/` or `拆文库/`, then fresh website benchmark cards if requested/needed, then project-specific `银发文学知识库/type-packs/{lane}.md` notes, and bundled type packs only as fallback.

Each `细纲_第XXX章.md` should include: target emotion, first bomb, old debt, proof movement, protagonist choice, reversal venue, public consequence, dense/sparse beat budget, cost/status change, recovery image, involved characters, and next hook.

## Writing Preflight

Before drafting a saved story or episode:

1. Identify the active project root. Prefer the directory containing `追踪/` or `设定/`; otherwise use the current working directory.
2. Read the current outline: `小节大纲.md` for single story or `大纲/细纲_第XXX章.md` for serialized work. If missing, stop and create the outline before prose.
3. Read the previous episode/chapter tail or full file when continuing.
4. Read `追踪/上下文.md`, `追踪/伏笔.md`, `追踪/时间线.md`, and the relevant slice of `追踪/角色状态.md`.
5. Read only the involved protagonist, family, company, facility, legal, medical, and financial setting files.
6. Run the ledger summary and check the candidate engine before writing.

## After Writing

After saving prose or a packaged episode:

1. Update `追踪/伏笔.md` with new, advanced, or resolved hooks.
2. Update `追踪/时间线.md` with the episode's event order.
3. Update `追踪/角色状态.md` for legal status, money/property, care responsibility, health, housing, family relation, public image, job, pension, or emotional boundary changes.
4. Update `追踪/上下文.md` with last completed story/episode, saved path, next outline status, and continuation risks.
5. Add one compact record to `银发文学知识库/generated-ledger.jsonl`.

## Benchmark Protocol

Each subtype may use a hot work only as a structural benchmark. Prefer dynamic拆书 over fixed bundled outlines:

- Prefer a project-owned analysis report under `对标/{lane}/{work}/拆文报告.md` or `拆文库/{work}/`.
- If no analysis exists and the user asks for current popular references, or if the lane has no strong project benchmark, browse public channel/video/ranking/tag pages and create a dynamic benchmark card.
- Do not copy titles, character names, houses, companies, scene order, dialogue, or detailed proprietary outlines from any live work.
- Save source-specific dynamic benchmark cards as `对标/{lane}/_live-benchmark-{YYYYMMDD}.md`.
- Save project-specific benchmark notes as `银发文学知识库/type-packs/{lane}.md` when they will affect future generation.
- If no benchmark is available, use the bundled type pack as the fallback and clearly mark it as a generic structural scaffold.
