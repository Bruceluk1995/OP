---
name: jp-isekai-review
description: "Review Japanese male-audience isekai drafts for genre fit, localization, readability, and presentation compliance. Use when checking 日文推文口播、动漫解说、なろう系/カクヨム風 prose, Japanese first-person isekai episodes, battle leveling, dungeon boss fights, OP/龙傲天, exile reversal, RPG terminology, male-audience hooks, Japanese naturalness, or whether a declared push script has drifted into first-person web-novel prose."
metadata: {"openclaw":{"source":"https://github.com/worldwonderer/oh-story-claudecode"}}
---

# JP Isekai Review

Required global read: `../story/references/audience-comprehension-floor.md`. Treat RPG-jargon-first openings and abstract skill proof as structural failures, not localization polish.

Review drafts for Japanese male-audience isekai fit and localization quality.

## Native Blind-Reader Gate

- Read the body once before validator, package, blueprint, and intended explanation. Mark the earliest point where the promised battle, OP, exile, dungeon, identity, or slow-life desire stops pulling forward.
- Require a protagonist-caused chain and a middle mechanism change. Repeated skill tests, guild witnesses, contracts, audits, inventory, travel, and larger public proof cannot substitute for escalation.
- For first person, review knowledge boundary, selected details, practical judgment, and narrator mouth; pronoun correctness alone has no value.
- Return the draft to `core / structure / scene / Japanese line` rather than compensating a structural failure with localization quality.
- Surface lint is mandatory format evidence for saved push bodies and never a story-quality verdict. Never require hooks at fixed 6-10-line intervals or call a metric pass quality approval.

## Required Reads

- Read `references/review-checklist.md` before a full review.
- Read `references/terminology.md` whenever checking Chinese-to-Japanese adaptation leakage.
- Read `../jp-isekai-write/references/self-check.md` when reviewing saved episodes, project-bound output, per-episode folders, continuity, plot bugs, package completeness, RPG-rule consistency, or Chinese leakage.
- For every declared push draft, read `../story/references/flan-push-strict-mode.md` and `../jp-isekai-write/references/push-narration-protocol.md`; for first person also read `../story-first-person-script/SKILL.md` and `../story-first-person-script/references/push-first-person-benchmark.md`.
- Read `../jp-short-fiction-studio/references/dynamic-market-learning.md` when auditing topic selection or claims of Japanese-market validation.
- Treat personality-free flowchart narration as blocking through the blind-reader/state-change audit, not a fixed line interval.
- If the draft or outline declares a subtype lane, read the loaded project benchmark card or `对标/{lane}/` report first when available, then the matching `../jp-isekai-plan/references/type-packs/{lane}.md` as fallback, and review against that lane's required payoff loop.

## Review Workflow

1. Identify the target:
   - Japanese-market male-audience isekai.
   - Traditional web-novel prose or anime-recap/push narration.
   - First-person or third-person.
   - Episode length target, if any.
   - If the project house format is Japanese-market push narration, do not reopen platform or presentation selection.
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
   - Declared push narration is actually first-person web-novel scene prose, a dialogue transcript, diary narration, or ordinary prose split into short lines.
   - Consecutive major modules lack a new problem, choice, tactic, consequence, relationship/status change, or audience question.
- A 12,000-character episode uses length to pad mood, scenery, travel, explanation, or adjectives; long stretches can be deleted without changing plot, pressure, relationship, cost, reward, setup, aftershock, or next choice.
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
   - For every saved push body, run the Flan validator. Treat `surface_fail` as a blocking presentation finding and `surface_pass` as surface-only evidence.

## Review Stance

Be strict about localization and reader experience. Do not preserve source terms just because they were in the Chinese premise. Preserve plot function; localize surface.
