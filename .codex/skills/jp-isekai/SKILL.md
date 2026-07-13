---
name: jp-isekai
description: "Japanese male-audience isekai writing suite router. Use when the user wants 日式RPG异世界, なろう系, カクヨム男性向け, male-protagonist Japanese fantasy, battle leveling, monster grinding, dungeon boss fights, overpowered protagonist, OP ruler fantasy, 龙傲天, demon-lord/kingdom domination, drops, status/rank growth, cheat skill, adventurer guild, slow life, harem-adjacent,ざまぁ, or when adapting Chinese webnovel settings into Japanese-style isekai without Chinese xianxia/wuxia terms."
metadata: {"openclaw":{"source":"https://github.com/worldwonderer/oh-story-claudecode"}}
---

# JP Isekai

Use this as the router for Japanese male-audience isekai work. Prefer the dedicated sub-skills:

Before proposing any premise, hotspot, title, or angle, read `../story/references/global-topic-history.md` and enforce the project-wide burned-topic ledger. A topic used or merely displayed by any other story or explainer skill must not be shown again unless the user explicitly requests reuse.

- `$jp-isekai-plan`: premise, world rules, protagonist, cheat design, first arc, episode outline.
- `$jp-isekai-write`: Japanese first-person episode drafting, usually 8k-20k Japanese characters.
- `$jp-isekai-oneshot`: standalone 14,500-16,500 character Japanese male-audience isekai short stories that fully resolve in one file, not serial episodes or 6-episode seasons.
- `$jp-isekai-review`: localization, Japanese readability, genre-fit, and Chinese-term leakage checks.

## Core Contract

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

1. Determine the task:
   - Standalone short story, one-shot, 一发完结, 15000字短篇, or "不是连续剧" -> use `$jp-isekai-oneshot`.
   - Explicit one-shot/一发完结 wins even when the prompt also mentions YouTube, thumbnail, 15,000 characters, or a hot topic. Explicit 6-episode/serial/第N話 wins over one-shot and routes through plan/write.
   - New concept or Chinese-to-Japanese adaptation -> use `$jp-isekai-plan`.
   - Write a full episode or rewrite draft in Japanese -> use `$jp-isekai-write`.
   - Check an existing draft -> use `$jp-isekai-review`.
2. If the task references an existing project, continuing episode, saved output, or anti-homogenization need, load the project memory protocol before planning or drafting.
3. If the task references current market/ranking trends, browse current source pages before making market claims.
4. If adapting from Chinese fantasy, first create a localization map: names, power system, institutions, creatures, currency, places, and plot functions.
5. Keep the output in the user-requested language. For Japanese prose, write the prose in Japanese and keep meta notes in Chinese unless the user requests all-Japanese delivery.

## Resources

Read `references/market-snapshot.md` when the task needs current-ish genre signals from 小説家になろう / カクヨム. Refresh by browsing if the user asks for "latest", "现在热门", ranking, or market direction.
Read `references/project-memory.md` when routing project-bound work or explaining the suite's engineering model.
