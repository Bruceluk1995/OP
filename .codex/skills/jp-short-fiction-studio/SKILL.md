---
name: jp-short-fiction-studio
description: Fast end-to-end Japanese commercial short-fiction studio for male-audience isekai and female-audience fantasy romance, in traditional prose or anime-recap/push narration and first or third person. Use for 日本市场异世界短篇、女性向け異世界恋愛、男频/女频一发完结、日文推文口播、爆款重构、真重写、作品不好看、留存差、流程稿、重复证明, or when the old Japanese fiction skills conflict or run too slowly.
metadata: {"openclaw":{"source":"https://github.com/worldwonderer/oh-story-claudecode"}}
---

# 日本商业短篇总编辑部

Mandatory topic gate: before inventing, showing, selecting, or generating any
new premise, title, hot/evergreen seed, or angle in either lane, read
`../story/references/global-topic-history.md` and obtain the company-wide online
reservation. Automatic or unattended production cannot bypass it; local recent
history cannot replace it.

One fast production chain owns concept, structure, drafting, and rejection. Genre entry skills only select a lane. Optional tools never run unless the task needs them.

## Minimal Read Set

Read exactly one lane file:

- male isekai: `references/male-isekai.md`
- female fantasy romance: `references/female-romance.md`

Read `references/dynamic-market-learning.md` for push production or current Japanese-market premise discovery.

When push narration is selected, also read `../jp-isekai-write/references/push-narration-protocol.md` and `../story/references/flan-push-strict-mode.md`. For first-person push, read `../story-first-person-script/SKILL.md` and its two push references. For third-person push, read `../story-third-person-script/SKILL.md` and its two push references. Do not load unrelated opening decks, ledgers, packaging guides, or old blueprint files unless the task needs them.

## Market-Basis Gate — Lao Liu Dynamic Learning

Before the Producer pass, choose exactly one evidence mode from `references/dynamic-market-learning.md`:

- `current evidence`: browse and validate current signals when the user asks what is hot, requests live sources, or delegates commercial premise discovery;
- `provided evidence`: use a fresh user/project benchmark or decision card and record its scope;
- `hypothesis only`: when the user gives a fixed premise or explicitly skips research, proceed without pretending it is market-validated and attach a small-test plan.

For this Japanese push workflow, the target market and presentation are fixed. Lao Liu evidence selects topic, promise, story engine, emotional payoff, and saturation risk; the Flan contract selects opening delivery, oral cadence, quote density, narrator role, and subtitle shape. Do not reopen platform selection.

## Fast Path — Default

If the user already gave lane, premise, viewpoint, and presentation, do not ask a menu. Run six passes:

1. **Market-basis editor**: record evidence mode, validated Japanese-market story functions, unvalidated assumptions, saturation/negative signal, and the smallest next test.
2. **Producer**: lock reader promise, emotion, protagonist desire, and the concrete event the audience is waiting for.
3. **Story-core editor**: choose a causal core where the protagonist makes an unusual choice, gets a visible result, and that result creates a new kind of trouble.
4. **Structure editor**: plan 6-10 flexible change modules; one decisive proof per conclusion; switch the middle mechanism.
5. **Japanese writer**: select exactly one branch: Traditional Scene Writer or Flan-Style Push Narrator. For push, lock an oral spine before drafting.
6. **Blind editor**: read the saved body without metrics, apply the editorial release gate, identify the earliest boring point or presentation drift, then rewrite from the earliest failed stage.

Planning remains compact and in memory. For chat-only work, output only the requested artifact. For project work, save the body plus one compact `作品决策卡.md`; do not create evidence, ledger, cover, character prompt, and audit files unless requested.

## Deep Path — Only When Needed

Use extra passes only when the user requests market research, multi-comparable fusion, a full production package, or rescue of a failed long draft:

- current Japanese market research;
- benchmark-function extraction;
- multiple opening candidates;
- detailed character voice sheet;
- full scene-change/debt table;
- rewrite-integrity comparison;
- packaging, cover, or ledger.

“做到最好” permits a deep editorial pass, not automatic browsing, ten files, or repeated validators when they add no value.

## Roles and Handoffs

Roles are independent passes, not simultaneous rule stacks. A later role may reject an earlier artifact.

### Producer

Outputs five lines: lane/platform, reader promise, dominant emotion, protagonist desire, generic-risk warning.

### Story-Core Editor

Generate up to three genuinely different cores, then choose one:

`ordinary trouble -> unusual protagonist choice -> visible result -> new-kind trouble -> decisive climax choice -> changed ending`

Reject luck-only, procedure-only, witness-only, repeated-proof, and “wait for a powerful person/institution to solve it” cores.

For male isekai, do not equate tension with a taxed ability. A cheat may be free, stable, and overwhelmingly useful. Generate pressure through opposition, scale, timing, protection, identity, competition, incomplete information, or the consequences of success unless the user explicitly selects a cost-driven power.

### Structure Editor

For each module record only:

`entering state -> event/choice -> exiting state -> live audience question`

Every module changes fact, problem, tactic, choice, relationship, status, resource, cost, danger, reversal, or payoff. Two consecutive preparation/explanation/travel/test/audit/sadness modules are forbidden.

### Traditional Scene Writer

Enter scenes near pressure, give the viewpoint character a current want, let action/dialogue force a choice or new interpretation, select character-specific details, and exit on the strongest changed fact or decision. Do not explain a punch after it lands.

Use this branch only for traditional prose. Do not reuse it for push narration by inserting extra line breaks.

### Flan-Style Push Narrator

Use this branch whenever presentation is anime recap/push narration:

- open result-first: abnormal outcome -> ordinary cause/choice -> immediate pressure, changed status, or live question;
- compress around cause and consequence rather than acting out every beat in real time;
- keep direct quotation sparse and retain only the line whose wording changes conflict, status, or emotion;
- make each non-empty line carry one action, reveal, reaction, consequence, or causal turn;
- preserve the narrator's practical judgment, misunderstanding, complaint, or contrast so first person never becomes a neutral camera;
- end each major module on a changed fact and a live pressure, not explanation or atmosphere;
- never treat short lines, `俺`, or a metric pass as proof that the body is push narration.

For first person, draft in four passes from the first-person gate: consequence-led report, narrator mouth, state change, and payoff. For third person, use the third-person gate: consequence-led report, narrator stance/stable labels, state change, and payoff. In both, the opening exposes the abnormal result and causal gap; the middle changes mechanism after first proof; the climax recycles earlier story debt; the ending proves change with an action.

Only after the blind editor reaches `ready for user read`, run `../story/scripts/validate-flan-push.py` on every saved push body. `surface_fail` blocks push-format delivery and sends the body back to this branch; `surface_pass` remains surface-only.

### Blind Editor

Read before checking length or lint. Use one verdict:

- `rebuild core`
- `major structural rewrite`
- `scene rewrite`
- `line edit`
- `ready for user read`

State the earliest loss of interest, what the reader was waiting for, what the text supplied instead, and which earlier role must redo its work. For push, also mark the earliest line where the narrator becomes a scene camera, dialogue transcript, diary voice, or novel broken into subtitles; identify the first repeated conclusion, middle mechanism change, climax debt, and ending proof action. Never use numeric quality scores or `PASS`.

### Push Editorial Release Gate

For first person, clear `../story-first-person-script/references/push-quality-gate.md`. For third person, clear `../story-third-person-script/references/push-quality-gate.md`, including narrator stance, stable labels, knowledge boundary, and protagonist agency. A failed gate blocks delivery even when surface lint passes.

## First-Person Contract

First person controls knowledge, selected details, judgment, misunderstanding, reaction, and sentence flavor. It is not a pronoun swap or a diary requirement.

Before drafting, know: what I know, what I cannot know, what I notice first, how I judge, what I want now, and what I refuse to admit. Do not reveal hidden motives or off-screen facts as certainty.

## True Rewrite

When rewriting an old body:

1. Extract only user-approved facts, anchors, and ending requirements.
2. Build a fresh causal core and change outline.
3. Draft from that outline, not by editing/appending the old body.
4. Run `scripts/verify-rewrite.py --old <old> --new <new>`.
5. A reuse failure blocks the word “rewritten”; structural quality still requires blind editing.

## Length and Proof

The default complete Japanese one-shot/episode target is approximately 12,000 Japanese characters. Length is a budget unless the user/platform supplies a real hard limit. If short, add a new obstacle, choice, relationship turn, pressure, or consequence through the structure editor. Otherwise report the honest shortfall. Never fill with procedures, lore, scenery, more witnesses, or another test of the same conclusion.

One decisive proof per conclusion. A later demonstration survives only when mechanism, stakes, relationship, or result changes.

## Optional Tools

- Browse only for current/ranking/trend claims or a requested live seed.
- Opening cards are optional ideation; no random draw or quote evidence is required.
- Push surface lint is mandatory for saved push delivery and optional for unsaved snippets. It cannot approve story quality.
- Ledger/package/cover generation runs only for project memory or explicit delivery requests.
- Anti-AI cleanup runs after story and scene failures are fixed.

## Delivery

Report the lane, evidence mode, presentation branch, operation, actual character count, central promise/closure, blind-editor verdict, and any requested tool result labeled by scope (`surface only`, `rewrite integrity only`, or `package only`).

## Hard Rules

- One master chain; genre wrappers must not duplicate its workflow.
- No mandatory menus when the user's choice is clear.
- No validator, card, evidence file, beat count, or length count can certify quality.
- No repeated public-proof ladder as the default climax.
- No copied old body plus appended ending called a rewrite.
- No Chinese genre machinery translated word for word into Japanese.
- No `surface_fail` body delivered under a push-narration label.
