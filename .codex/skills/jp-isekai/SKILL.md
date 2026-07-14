---
name: jp-isekai
description: "Japanese male-audience isekai writing suite router for traditional web-novel prose or anime-recap/push narration copy, each supporting first-person or third-person narration. Use when the user wants 日式RPG异世界, 男频异世界推文/动漫解说文案, なろう系, カクヨム男性向け, battle leveling, dungeon bosses, OP/龙傲天, exile reversal, status/rank growth, slow life, Google Trends JP, YouTube/TikTok trends, Japanese news or hot-topic conversion, or Chinese-to-Japanese isekai adaptation."
metadata: {"openclaw":{"source":"https://github.com/worldwonderer/oh-story-claudecode"}}
---

# JP Isekai

Use this as the router for Japanese male-audience isekai work. Prefer the dedicated sub-skills:

- `$jp-isekai-plan`: premise, world rules, protagonist, cheat design, first arc, episode outline.
- `$jp-isekai-write`: Japanese first-person episode drafting, usually 8k-20k Japanese characters.
- `$jp-isekai-oneshot`: standalone 14,500-16,500 character Japanese male-audience isekai short stories that fully resolve in one file, not serial episodes or 6-episode seasons.
- `$jp-isekai-review`: localization, Japanese readability, genre-fit, and Chinese-term leakage checks.

## Core Contract

- Before any long or short male-isekai planning or drafting, read `references/presentation-modes.md` and present its numbered 1-4 format menu unless the combination is already explicit. Allow multiple selections; treat them as separate comparison versions by default. Length, YouTube use, or `一口气看完` decides neither mode nor person.
- For either push option, read `../story/references/flan-push-strict-mode.md`; first/third person must share the same recap surface and saved bodies must pass its validator.
- After the presentation mode is fixed and no concrete premise was supplied, read `references/topic-menu.md` and use its progressive topic gate. Present only the first-level entry menu; never dump the complete topic pool on the first screen. Keep `实时热点搜索／热点转译` visible as a first-level choice.
- When the user selects the hot-topic entry (or legacy option `40`), show the numbered source menu from `references/topic-menu.md`, browse current sources, and present dated candidate seeds before choosing a genre lane. Treat source choice and concrete seed choice as separate decisions.
- For hot-topic discovery, follow the lifestyle-first default in `references/topic-menu.md`: prioritize current pressures in ordinary Japanese life and use event, celebrity, sports, disaster, crime, or novelty news only when the user explicitly requests them.
- Reject literary prose in drafted or rewritten fiction: avoid long environment description and long psychology description; use colloquial, direct everyday language to advance plot through action, dialogue, choices, and consequences.

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

1. Resolve the presentation-mode gate from `references/presentation-modes.md`.
2. If no concrete premise is supplied, resolve the progressive topic gate from `references/topic-menu.md`: entry route -> category or source -> compact candidates. Selecting the hot-topic entry (or legacy `40`) starts live multi-source hot-topic discovery and conversion; do not collapse it into auto-pick or a static genre lane.
3. Determine the task:
   - Standalone short story, one-shot, 一发完结, 15000字短篇, or "不是连续剧" -> use `$jp-isekai-oneshot`.
   - Explicit one-shot/一发完结 wins even when the prompt also mentions YouTube, thumbnail, 15,000 characters, or a hot topic. Explicit 6-episode/serial/第N話 wins over one-shot and routes through plan/write.
   - New concept or Chinese-to-Japanese adaptation -> use `$jp-isekai-plan`.
   - Write a full episode or rewrite draft in Japanese -> use `$jp-isekai-write`.
   - Check an existing draft -> use `$jp-isekai-review`.
4. If the task references an existing project, continuing episode, saved output, or anti-homogenization need, load the project memory protocol before planning or drafting.
5. If the task references current market/ranking trends or came through the hot-topic entry, browse current source pages before making market claims.
6. If adapting from Chinese fantasy, first create a localization map: names, power system, institutions, creatures, currency, places, and plot functions.
7. Keep the output in the user-requested language. For Japanese prose, write the prose in Japanese and keep meta notes in Chinese unless the user requests all-Japanese delivery.

## Resources

Read `references/market-snapshot.md` when the task needs current-ish genre signals from 小説家になろう / カクヨム. Refresh by browsing if the user asks for "latest", "现在热门", ranking, or market direction.
Read `references/project-memory.md` when routing project-bound work or explaining the suite's engineering model.
Read `references/presentation-modes.md` before all male-isekai planning or drafting.
Read `references/topic-menu.md` after the format choice when the user has not supplied a concrete premise; follow its progressive menus and per-screen option limit. Load the full topic pool for internal selection, but show only the branch relevant to the user's latest choice.
Read `references/opening-innovation-engine.md` after the premise and mode are locked and before drafting a push opening. Filter by the selected male-isekai lane, run its random draw script, fill only the compatible screenshot-derived card, and record the card ID. Exclude recent IDs when project history exists.
