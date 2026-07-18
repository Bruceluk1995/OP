---
name: jp-isekai
description: Router for Japanese male-audience isekai in traditional prose or anime-recap/push narration, first or third person. Use for 日式RPG异世界、なろう系、カクヨム男性向け、battle leveling、dungeon、OP、追放ざまぁ、slow life, Japanese-market one-shots or serial work, localization, current trends, Chinese novel-site inspiration, writing, and review.
metadata: {"openclaw":{"source":"https://github.com/worldwonderer/oh-story-claudecode"}}
---

# JP Isekai Router

Mandatory topic gate: before this route invents, shows, selects, or generates
any new premise, title, hot/evergreen seed, or episode angle, read
`../story/references/global-topic-history.md` and obtain the company-wide online
reservation. This applies to automatic and unattended selection too; local
recent history cannot replace it, and an unavailable online gate stops new
topic generation.

Route quickly. Do not stack every male-isekai skill and reference on one request.

## Routes

- Standalone short / one-shot / 一发完结 / 不是连续剧 -> `$jp-isekai-oneshot`, which uses `$jp-short-fiction-studio` plus the male lane.
- New serial concept, world, cheat, arc, or outline -> `$jp-isekai-plan`.
- Write or genuinely rewrite a serial episode/chapter -> `$jp-isekai-write`.
- Review an existing Japanese draft -> `$jp-isekai-review`.

Explicit one-shot beats a generic “12,000字” or “YouTube” keyword. Explicit episode/serial beats one-shot.

## Fast Routing

If presentation, viewpoint, premise, and length are already clear, route immediately. Do not show a format or topic menu. Ask one compact question only when an essential choice would materially change the product.

Accept only the normalized handoff `presentation=<traditional|push>` and `viewpoint=<first|third>` from an upstream menu; raw menu code is not a downstream mode. If the user or project has fixed Japanese-market anime-recap/push narration, propagate `presentation=push` plus the selected viewpoint to every downstream plan, write, one-shot, and review route. Push is sticky until the user explicitly changes it. Do not ask the presentation question again, consult traditional mode as a competing authority, or let first person imply traditional web-novel prose. If the handoff is missing or ambiguous, ask instead of defaulting to traditional.

For one-shots, the only required creative chain is:

`jp-short-fiction-studio + male-isekai lane`

Opening decks, random draws, trend routers, ledgers, delivery packages, surface lint, and cover generation are optional functions. Do not load or run them by default.

## Japanese Male-Isekai Contract

- Audience-facing prose is natural Japanese; planning notes may be Chinese.
- Use Japanese RPG/fantasy mechanisms and social institutions, not translated xianxia/sect/court defaults. Any light-novel benchmark is genre/localization evidence only; it cannot override `presentation=push` or authorize traditional scene prose.
- Match the promised lane: battle and OP stories need tactical/identity/faction consequences; slow-life stories need tangible comfort/relationship/safety change.
- The protagonist's choices cause the plot. Enemies learn; allies are not applause devices.
- A one-shot changes problem after first proof and closes in one file.

## Current-Market Work

Browse only when the user asks for current rankings, trends, news, YouTube/TikTok signals, or a live seed. Present dated candidates when the concrete seed is not delegated. Do not browse merely because the story targets Japan.

Chinese male-audience novel rankings, category pages, tags, and public synopsis-level metadata may be used as an optional cross-market mechanism pool. Read `references/chinese-novel-inspiration.md` when that source is requested or selected. Label it as Chinese-market inspiration, never as proof of Japanese demand; rebuild the mechanism for Japanese RPG/fantasy institutions and cross-check it against current Japanese signals before claiming Japanese-market fit.

## Project Work

Load project memory only for an existing project, serial continuity, or explicit anti-homogenization request. Normal chat generation does not require a ledger, package tree, or deployment setup.

## Character Prompt Companion

Read `references/character-prompt-contract.md` whenever this route or any downstream male-isekai route invents named characters, outputs a cast, drafts a script with named characters, or saves a plan/episode/one-shot. Character prompts are part of the male-isekai character handoff, not optional cover packaging. Create Japanese-only neutral reference prompts with empty hands and no symbolic object, weapon, tool, skill effect, action, or scene composition. Apply the contract's distinct Japanese harem-anime heroine design by default unless the user or premise explicitly selects another visual lane.

## Hard Rules

- One router selects one downstream route; do not run plan, write, one-shot, and review as simultaneous authorities.
- Do not use a random opening card or fixed character count as a quality gate.
- Do not copy ranking works, source IP, dialogue, scene order, or named plots.
- Do not call a copied body plus appended ending a rewrite.
- Do not deliver a newly created named male-isekai cast without its character-prompt companion unless the user explicitly requests body-only output.
