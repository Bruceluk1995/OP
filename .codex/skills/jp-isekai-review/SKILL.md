---
name: jp-isekai-review
description: "Review Japanese male-audience isekai drafts for genre fit, localization, and readability. Use when checking なろう系/カクヨム風 prose, Japanese first-person isekai episodes, battle leveling, monster grinding, dungeon boss fights, overpowered protagonist, OP ruler fantasy, 龙傲天, demon-lord/kingdom domination, drops/rank/status growth, Chinese-to-Japanese adaptation drafts, banned Chinese fantasy term leakage, RPG terminology consistency, male-audience hooks, humor, slow-life payoff, and Japanese naturalness."
metadata: {"openclaw":{"source":"https://github.com/worldwonderer/oh-story-claudecode"}}
---

# JP Isekai Review

Review drafts for Japanese male-audience isekai fit and localization quality.

## Required Reads

- Read `references/review-checklist.md` before a full review.
- Read `references/terminology.md` whenever checking Chinese-to-Japanese adaptation leakage.
- Read `../jp-isekai-write/references/self-check.md` when reviewing saved episodes, project-bound output, per-episode folders, continuity, plot bugs, package completeness, RPG-rule consistency, or Chinese leakage.
- Read `../story/references/flan-push-strict-mode.md` for every push review and run its validator. Treat first-person novelization as blocking, not a viewpoint preference.
- If the draft or outline declares a subtype lane, read the loaded project benchmark card or `对标/{lane}/` report first when available, then the matching `../jp-isekai-plan/references/type-packs/{lane}.md` as fallback, and review against that lane's required payoff loop.

## Review Workflow

1. Identify the target:
   - JP webnovel / なろう系 / カクヨム男性向け.
   - First-person or third-person.
   - Episode length target, if any.
2. Check blocking issues first:
   - Two or more consecutive major scenes end with the same material state: no new skill knowledge, combat position, drop/resource, rank, reputation, territory, faction relation, risk, or objective. Mark the exact stagnant span and recommend merge/compression or a concrete state-changing beat.
   - The episode advertises a monster/skill/OP/zamaa promise but only postpones it; a cliffhanger is not a substitute for visible proof, result, or consequence.
   - Project-bound draft has no matching `大纲/细纲_第XXX章.md`, or the prose clearly ignores the available outline.
   - Project-bound continuation did not read/update `追踪/上下文.md`, `追踪/伏笔.md`, `追踪/时间线.md`, or relevant `追踪/角色状态.md`.
   - New concept/episode repeats a recent `男频异世界知识库/generated-ledger.jsonl` combination without changing at least two key fields.
   - Chinese fantasy terms or institutions leaking into a Japanese RPG fantasy setting.
   - Chinese court-drama institutions or social logic leaking through literal translation: emperor/harem/cold-palace/concubine/嫡庶/夺嫡 logic remains instead of Japanese RPG/fantasy royal, guild, noble, territory, or faction systems.
   - Japanese prose that reads like machine translation or Chinese sentence order.
   - Literary-prose drift: long environment description, long psychology description, decorative mood, or essay-like inner monologue replaces colloquial action, dialogue, choices, and consequences.
   - Cheat rules unclear or not repeatable.
   - Episode lacks opening hook, practical payoff, or next hook.
   - Project-bound outline names a subtype lane but uses only generic isekai rules when a project拆文, dynamic benchmark card, project subtype note, or matching type pack should have been loaded.
   - OP premise is only instant victory with no enemy misread, restraint, information gap, subordinate/faction pressure, public identity issue, reputation consequence, or larger-stage hook.
   - Battle-upgrade premise drifts into only commerce, herbs, shopkeeping, travel, or comfort scenes without a monster/combat problem, tactical skill use, visible win/loss, or drop/rank/level/status consequence.
   - Episode has no full episode blueprint logic: unclear target emotion, episode position, core payoff, cost/risk, dense/sparse beat split, or ending hook.
   - Episode 2+ opens as a reset instead of continuing the previous episode's unresolved hook.
   - First sentence is atmosphere, abstract emotion, destiny, scenery, or generic inner monologue instead of a concrete plot bomb.
   - Mid-episode has two or more 800-1200 character stretches without concrete problem, skill experiment, public reaction, cost/reward/status consequence, comic reversal, object/monster behavior, or meaningful choice.
   - A 15,000-character episode uses length to pad mood, scenery, travel, explanation, or adjectives; long stretches can be deleted without changing plot, pressure, relationship, cost, reward, setup, aftershock, or next choice.
   - Dense beats are not denser than transitions; the prose spends similar weight on travel/mood and payoff.
   - Prose is padded with vague AI-flavored adjectives or summary paragraphs instead of scene-level objects, choices, witnesses, and consequences.
   - Draft fails JP anti-AI gates: generic destiny/light/silence texture, author explanation, stock summary ending, uniform rhythm, over-polished dialogue, or emotional lines without object/action/consequence.
   - Saved file or episode folder has not received a Codex AI self-check over outline, tracking files, previous episode tail, current body, and package assets.
   - Codex AI self-check fails: continuity reset, character-state contradiction, RPG rule contradiction, unexplained reward/drop/rank-up, unused extra character prompt, missing package file, cover not actual 16:9 image, or unresolved Chinese leakage.
3. Check genre fit:
   - Male-audience protagonist agency.
   - Social unfairness or pressure.
   - OP dominance loop if that is the chosen flavor: enemy/world misread, restrained decision, overwhelming reveal/command, witness/subordinate reaction, reputation/territory/faction consequence, stronger stage hook.
   - Battle/progression loop if that is the chosen flavor: monster problem, skill under pressure, tactical adjustment, drop/rank/level/status result, stronger next threat.
   - Exile/academy/Earth-commute/tamer/dungeon-master loops when chosen: each must have its own visible engine, not generic slow-life filler.
   - Optimization/crafting/status/guild/dungeon loop.
   - Comic inner commentary and reactions.
   - Slow-life desire vs escalating trouble if that is the chosen flavor.
4. Return:
   - Findings ordered by severity.
   - Concrete line/phrase examples if a draft file is available.
   - Project-memory gaps: missing outline, stale tracking, missing ledger record, or repeated engine.
   - Density gaps: paragraphs or stretches that can be deleted without changing plot state.
   - A concise fix plan.
   - Optional rewritten sample only for the affected paragraph unless the user asks for a full rewrite.

## Review Stance

Be strict about localization and reader experience. Do not preserve source terms just because they were in the Chinese premise. Preserve plot function; localize surface.
