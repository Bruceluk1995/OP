---
name: jp-isekai
description: "Japanese male-audience isekai writing suite router for traditional web-novel prose or anime-recap/push narration copy, each supporting first-person or third-person narration. Use when the user wants 日式RPG异世界, 男频异世界推文/动漫解说文案, なろう系, カクヨム男性向け, battle leveling, dungeon bosses, OP/龙傲天, exile reversal, status/rank growth, slow life, or Chinese-to-Japanese isekai adaptation."
metadata: {"openclaw":{"source":"https://github.com/worldwonderer/oh-story-claudecode"}}
---

# JP Isekai

## 数字交互契约

- 凡需用户在有限选项中决定，必须在普通对话中列出数字编号，并以“请只回复数字；可多选时用 +，如 1+3”收尾。
- 禁止用开放式问题代替可枚举选项；禁止依赖 AskUserQuestion、request_user_input 或自由文本选项完成有限选择。
- “自定义 / 其他 / 提供素材”也必须编为数字选项。用户选中后，下一轮只索取一个必要内容（如关键词、书名、路径、链接或正文）；这类实际内容不强行数字化。
- 是非确认统一写成 1. 是 / 2. 否，并要求只回复数字。

Use this as the router for Japanese male-audience isekai work. Prefer the dedicated sub-skills:

Before proposing any premise, hotspot, title, or angle, read `../story/references/global-topic-history.md` and enforce the project-wide burned-topic ledger. A topic used or merely displayed by any other story or explainer skill must not be shown again unless the user explicitly requests reuse.

Before proposing or finalizing character names, read `../story/references/character-name-policy.md`, import the shared name ledger, check every new name, and record names actually used. A continuing work may reuse its own cast; a new work may not reuse an existing fantasy given name by changing only the surname or kana form.

- `$jp-isekai-plan`: premise, world rules, protagonist, cheat design, first arc, episode outline.
- `$jp-isekai-write`: Japanese first-person episode drafting, usually 8k-20k Japanese characters.
- `$jp-isekai-oneshot`: standalone 14,500-16,500 character Japanese male-audience isekai short stories that fully resolve in one file, not serial episodes or 6-episode seasons.
- `$jp-isekai-review`: localization, Japanese readability, genre-fit, and Chinese-term leakage checks.

## Core Contract

- Before any long or short male-isekai planning or drafting, read `references/presentation-modes.md` and present its numbered 1-4 format menu unless the combination is already explicit. Allow multiple selections; treat them as separate comparison versions by default. Length, YouTube use, or `一口气看完` decides neither mode nor person.
- For either push option, read `../story/references/flan-push-strict-mode.md`; first/third person must share the same recap surface and saved bodies must pass its validator.
- Reject literary prose in drafted or rewritten fiction: avoid long environment description and long psychology description; use colloquial, direct everyday language to advance plot through action, dialogue, choices, and consequences.
- Keep important women easy to hear in narration: prefer 2-6 character everyday names and use `--style jp-female-fantasy`; do not default to long aristocratic names.

Always localize toward Japanese web novel / light-novel expectations:

- Use `魔力`, `スキル`, `ステータス`, `ランク`, `冒険者ギルド`, `貴族`, `商会`, `ダンジョン`, `魔物`, `使い魔`, `従魔`, `装備枠`.
- Avoid Chinese xianxia/wuxia and Chinese webnovel defaults unless the user explicitly asks for Chinese style.
- Keep the protagonist readable for male-audience isekai: practical self-interest, survival pressure, comic inner commentary, visible growth, and a cheat that creates repeatable plot engines.
- Favor familiar low-cost fantasy objects and domestic animals when adapting a grassroots slow-life setup: chicken, goat, donkey, sheep, dog, cow, cart, tools, feed, old gear, herb, guild scraps.
- Do not default male-audience爽文 to slow life. If the user chooses cheat survival, zamaa, dungeon, battle, leveling, monster, or "爽", offer a battle-progression route before shopkeeping, farming, or quiet base-building.
- For battle-progression routes, each episode should usually contain: monster/problem -> skill test -> tactical adjustment -> visible win/drop/rank/level result -> stronger next threat.
- Also support OP dominance / ruler fantasy. When the user wants 龙傲天, 开局无敌, 魔王/统治者 fantasy, or references works like "骨王" as a vibe, treat the protagonist as already overwhelming. The progression becomes reputation, territory, subordinates, information control, enemy misread, and larger-stage consequences, not stat growth.
- For OP routes, each episode should usually contain: enemy/world misread -> pressure or insult -> restrained decision -> overwhelming reveal or strategic command -> witness/subordinate reaction -> reputation/territory/faction consequence -> stronger stage hook.
- Use famous works only as functional references. Do not copy named characters, guilds, kingdoms, scenes, dialogue, or plot turns.
- Do not copy prose or long summaries from ranking works. Extract market patterns only.

## Project Memory Contract

When the task is project-bound, treat this suite as a genre layer on top of the common story project architecture:

- Use `设定/`, `大纲/`, `追踪/`, `episodes/`, `对标/`, and `拆文库/` as long-term memory.
- Use `男频异世界知识库/generated-ledger.jsonl` to remember generated concepts, outlines, titles, and episodes so future work does not repeat the same engine.
- `$jp-isekai-plan` owns settings, outlines, first rolling chapter blueprints, and initial tracking files.
- `$jp-isekai-write` must read the current outline and tracking files before prose, then update tracking and ledger after saving.
- `$jp-isekai-review` should flag project-bound drafts that bypass the outline/tracking/ledger loop.

Detailed protocol: `references/project-memory.md`.

## Workflow

1. If the user only says "男频异世界" or "なろう系" without a concrete lane, display: `1 开局无敌/势力经营`、`2 打怪升级/地下城`、`3 追放ざまぁ/辅助职业逆袭`、`4 学园/游戏知识`、`5 日本往返/现代物资`、`6 驯兽/従魔`、`7 地下城主/领地经营`、`8 秘密组织/部下脑补`、`9 生产经营/慢生活`、`10 热点选题`、`11 自定义`; require a numeric reply. Option 11 may request one keyword in the next turn.
2. Resolve the presentation-mode gate from `references/presentation-modes.md`.
3. Determine the task:
   - Standalone short story, one-shot, 一发完结, 15000字短篇, or "不是连续剧" -> use `$jp-isekai-oneshot`.
   - Explicit one-shot/一发完结 wins even when the prompt also mentions YouTube, thumbnail, 15,000 characters, or a hot topic. Explicit 6-episode/serial/第N話 wins over one-shot and routes through plan/write.
   - New concept or Chinese-to-Japanese adaptation -> use `$jp-isekai-plan`.
   - Write a full episode or rewrite draft in Japanese -> use `$jp-isekai-write`.
   - Check an existing draft -> use `$jp-isekai-review`.
4. If the task references an existing project, continuing episode, saved output, or anti-homogenization need, load the project memory protocol before planning or drafting.
5. If the task references current market/ranking trends, browse current source pages before making market claims.
6. If adapting from Chinese fantasy, first create a localization map: names, power system, institutions, creatures, currency, places, and plot functions.
7. Keep the output in the user-requested language. For Japanese prose, write the prose in Japanese and keep meta notes in Chinese unless the user requests all-Japanese delivery.

## Resources

Read `references/market-snapshot.md` when the task needs current-ish genre signals from 小説家になろう / カクヨム. Refresh by browsing if the user asks for "latest", "现在热门", ranking, or market direction.
Read `references/project-memory.md` when routing project-bound work or explaining the suite's engineering model.
Read `references/presentation-modes.md` before all male-isekai planning or drafting.
Read `references/topic-menu.md` after the format choice when the user has not supplied a concrete premise; present the full grouped menu with multi-select, auto-pick, custom, and refresh controls.
Read `references/opening-innovation-engine.md` after the premise and mode are locked and before drafting a push opening. Filter by the selected male-isekai lane, run its random draw script, fill only the compatible screenshot-derived card, and record the card ID. Exclude recent IDs when project history exists.
