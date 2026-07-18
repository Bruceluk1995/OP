---
name: jp-isekai-oneshot
description: Fast Japanese male-audience isekai one-shot entry for traditional web-novel prose or anime-recap/push narration, first or third person. Use for 日式男频异世界短篇、男频异世界推文、动漫解说文案、一发完结、Chinese novel-site inspiration、battle leveling、OP、追放ざまぁ、dungeon, or a complete Japanese isekai short that must resolve in one file.
metadata: {"openclaw":{"source":"https://github.com/worldwonderer/oh-story-claudecode"}}
---

# JP Isekai One-Shot — Thin Entry

Mandatory topic gate: before inventing, showing, selecting, or generating any
premise, title, hot/evergreen seed, or angle, read
`../story/references/global-topic-history.md` and obtain the company-wide online
reservation. Automatic selection and a user-delegated choice do not bypass the
gate; local recent history cannot replace it.

This skill selects the male-isekai lane. The single production workflow lives in `../jp-short-fiction-studio/SKILL.md`.

## Required Read

Read:

1. `../jp-short-fiction-studio/SKILL.md`
2. `../jp-short-fiction-studio/references/male-isekai.md`
3. `../jp-short-fiction-studio/references/dynamic-market-learning.md` for push production or current Japanese-market premise discovery
4. `../jp-isekai/references/topic-menu.md` when the user has not supplied a concrete premise

When push narration is selected, also read:

5. `../story/references/push-prompt-architecture.md`
6. `../story/references/push-entertainment-gate.md`
7. `../story/references/push-retention-chain.md`
8. `../jp-isekai-write/references/push-narration-protocol.md`
9. `../story/references/flan-push-strict-mode.md`
10. `../story-first-person-script/SKILL.md`, `../story-first-person-script/references/push-first-person-benchmark.md`, and `../story-first-person-script/references/push-quality-gate.md` for first person
11. `../story-third-person-script/SKILL.md`, `../story-third-person-script/references/push-third-person-benchmark.md`, and `../story-third-person-script/references/push-quality-gate.md` for third person

When the Chinese novel-site source is selected, also read `../jp-isekai/references/chinese-novel-inspiration.md`. Do not load it for unrelated requests.

Do not load unrelated old blueprints, opening decks, package guides, or ledgers unless the task needs them. Push contracts are not optional when push presentation is selected.

## Fast Intake

Infer from the prompt whenever possible:

- traditional prose or push narration;
- first or third person;
- subtype and main male-audience payoff;
- user/platform length requirement.

If the user or project has already fixed the house format as Japanese-market push narration, set presentation to push without asking again.

Accept the upstream normalized handoff, never its raw menu code. When `presentation=push`, freeze `writer_branch=flan_push` and the selected `viewpoint=<first|third>` before planning. This sticky branch lock forbids traditional scene-writing rules from becoming an authority later in the run; only an explicit user change may unlock it. If the viewpoint is missing, ask for it instead of defaulting to traditional prose.

Do not present a menu when these are already clear. If only one essential choice is missing, ask one compact question or make a safe stated assumption.

When the premise is missing, resolve or infer presentation and viewpoint, then present the Level 1 creation-entry menu from `../jp-isekai/references/topic-menu.md`. This gate is required: do not jump directly to a free-form synopsis request, auto-invent the premise, or start the studio fast path. Browse only after the user selects the live-hot-topic route; classic, fresh, keyword, and automatic-recommendation routes do not require live browsing.

## Defaults

- Audience-facing body: natural Japanese; meta notes: Chinese unless requested otherwise.
- Default complete one-shot budget: approximately 12,000 Japanese characters in either presentation mode.
- Treat 12,000 as a target, not a minimum gate or permission to pad.
- Complete the opening promise, main conflict, reward/consequence, and changed social/emotional state in this file.
- Treat ability cost as optional. OP, production, commerce, and slow-life premises default to benefit-first abilities; create story pressure outside the power unless the user explicitly chooses a curse, exchange, backlash, or sacrifice engine.

## Execution

Complete the progressive topic gate and obtain a concrete user-selected or explicitly delegated premise before production.

Run the studio path once: Market Basis -> Producer -> Story Core -> High-Value Event Scan -> Entertainment Editor -> Change Structure -> the already locked Japanese writer branch -> Oral Rewrite -> Blind Editor -> Surface Lint. Restart from the earliest failed stage. Push narration must keep `writer_branch=flan_push`, lock the entertainment/retention chain before prose, draft natural spoken sentences before subtitle splitting, and complete the adversarial entertainment read, saved-body evidence map, and selected viewpoint's editorial release gate before surface lint.

Browse for current Japanese-market rankings, trends, news, live-source requests, or an explicitly selected Chinese novel-site inspiration pass and follow the dynamic-market contract plus the source-specific contract. Chinese novel-site popularity is cross-market inspiration only; require a current Japanese cross-check before calling the premise Japanese-market validated. Story-market evidence selects the premise and modules; the Flan contract always owns push delivery. Opening cards, package files, cover prompts, character prompts, and ledgers remain optional.

For a saved push body, run `../story/scripts/validate-flan-push.py`. A `surface_fail` blocks delivery under the label “anime recap/push narration”; it does not reject the story core. A `surface_pass` is format evidence only and never quality approval.

For project-bound work, save the Japanese body and one compact decision card. Create a full package only when requested.

## Male-Isekai Closure

- The promised skill, tactic, OP position, exile function, dungeon rule, or territory choice produces a visible result.
- After first proof, the story changes problem instead of testing the same rule again.
- The middle contains battle, tactical, social, identity, resource, or faction escalation appropriate to the selected promise.
- The climax depends on the protagonist's earlier choice.
- The ending resolves the one-shot; no previous/next-episode bridge.

## Hard Rules

- Do not drift from battle/OP/adventure into bakery, contracts, audits, training, or inventory unless that is the user's chosen promise.
- Do not translate Chinese xianxia, sect, court, or son-in-law systems literally.
- Do not weaken an OP protagonist randomly; use information, restraint, identity, protection duties, collateral risk, or faction consequence.
- Do not auto-balance every cheat with backlash, lifespan/memory loss, debt, loss of control, or punishment. Ability boundaries and narrative pressure are separate design decisions.
- Do not call length, opening-card, or surface-lint results quality approval.
- Do not deliver first-person web-novel scenes broken into short lines as push narration.
- Do not deliver third-person web-novel scenes or neutral chronology broken into short lines as push narration.
- Do not call a premise market-validated when it has only one work or one list snapshot as evidence.
- Do not present Chinese novel-site popularity as Japanese-market validation or copy its titles, systems, scene order, or named plot.
