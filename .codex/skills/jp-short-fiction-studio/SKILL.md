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

For the male-isekai lane, also read `../jp-isekai/references/character-prompt-contract.md` whenever the task creates named cast or a script. This character-prompt companion is a lane deliverable, not optional cover packaging.

Read `references/dynamic-market-learning.md` for push production or current Japanese-market premise discovery.

When push narration is selected, also read `../story/references/push-prompt-architecture.md`, `../story/references/push-entertainment-gate.md`, `../story/references/push-retention-chain.md`, `../jp-isekai-write/references/push-narration-protocol.md`, and `../story/references/flan-push-strict-mode.md`. For first-person push, read `../story-first-person-script/SKILL.md` and its two push references. For third-person push, read `../story-third-person-script/SKILL.md` and its two push references. Do not load unrelated opening decks, ledgers, packaging guides, or old blueprint files unless the task needs them.

## Market-Basis Gate — Lao Liu Dynamic Learning

Before the Producer pass, choose exactly one evidence mode from `references/dynamic-market-learning.md`:

- `current evidence`: when the user asks what is hot, requests live sources, or delegates commercial premise discovery, browse only signals verified inside a rolling 24-hour JST window; return fewer signals rather than padding with older evidence;
- `provided evidence`: use a fresh user/project benchmark or decision card and record its scope;
- `hypothesis only`: when the user gives a fixed premise or explicitly skips research, proceed without pretending it is market-validated and attach a small-test plan.

For this Japanese push workflow, the target market and presentation are fixed. Lao Liu evidence selects topic, promise, story engine, emotional payoff, and saturation risk; the Flan contract selects opening delivery, oral cadence, quote density, narrator role, and subtitle shape. Do not reopen platform selection.

## Fast Path — Default

If the user already gave lane, premise, viewpoint, and presentation, do not ask a menu. Run eight passes:

First preserve the normalized handoff as an immutable run lock: `presentation=<traditional|push>`, `viewpoint=<first|third>`, and `writer_branch=<traditional_scene|flan_push>`. Raw menu code is never a branch value. When `presentation=push`, set `writer_branch=flan_push`; no later role may reopen or reinterpret it unless the user explicitly changes presentation.

1. **Market-basis editor**: record evidence mode, validated Japanese-market story functions, unvalidated assumptions, saturation/negative signal, and the smallest next test.
2. **Producer**: lock the speaker/listener contract, audience emotional contract, reader promise, protagonist desire, and the concrete event the audience is waiting for.
3. **Story-core editor**: choose a causal core where the protagonist makes an unusual choice, gets a visible result, and that result creates a new kind of trouble.
4. **High-value event scanner**: label candidate events `expand / one-line bridge / cut`; rotate conflict, reversal, information, relationship, visual proof, status, choice, and payoff instead of compressing every event evenly.
5. **Entertainment editor**: apply the `Push Entertainment Gate`; reject technical state changes without human collision, companion-as-function choreography, paraphrase-only conflict, early central payoff with a long tail, and any middle that is better described as a procedure than a confrontation.
6. **Structure editor**: group the selected event beats into 6-10 flexible change modules; one decisive proof per conclusion; switch the middle mechanism. For push, lock the `1 + 3 + N` retention chain before prose.
7. **Japanese writer**: execute the already locked branch. Select a branch only when the upstream handoff is genuinely missing; ask if ambiguous instead of defaulting to traditional. For push, keep `writer_branch=flan_push`, lock an oral spine, draft natural spoken sentences, and postpone subtitle splitting.
8. **Blind editor**: read the saved body without metrics, apply the entertainment and editorial release gates, identify the earliest boring point or presentation drift, then rewrite from the earliest failed stage.

Planning remains compact and in memory. For chat-only work, output only the requested artifact, plus the male-isekai character-prompt companion when named cast or a script is created. For project work, save the body plus one compact `作品决策卡.md`; in the male-isekai lane also save the required character-prompt asset. Do not create evidence, ledger, cover, or audit files unless requested.

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

### High-Value Event Scanner

Use the shared prompt contract in `../story/references/push-retention-chain.md`.

For every candidate event, record the visible before/after, human effect, emotional job, protagonist response, narrative function, and `expand / bridge / cut` decision. Keep the smallest set that forms a complete causal and emotional story.

Reject uniform compression. A page of travel may become one line; a five-second betrayal may deserve a full beat. Do not draft until the selected path alternates at least several functions such as conflict, information, relationship, tactic, status, cost, and payoff.

### Entertainment Editor

Use `../story/references/push-prompt-architecture.md` and `../story/references/push-entertainment-gate.md`. First lock one imagined listener, speaker mouth, dominant pressure emotion, mid-story emotional conversion, final release emotion, concrete object/action/line anchors, and title promise. For every `expand` event, require a present desire, active blocker, visible collision, human price, protagonist response, narrator take, emotional change, memorable action or decisive exact line, and a new audience question.

Relabel rule, route, pipe, contract, skill-system, registry, or policy changes as `bridge` unless they force a person to choose, refuse, lose, expose, betray, risk, or change relationship/status. Reject a roster whose members merely perform assigned functions. Lock the title-promise payoff position and the expected post-final-payoff share before the Structure Editor proceeds.

### Structure Editor

Group several selected event beats inside each major module when the length needs it. For each beat record only:

`entering state -> event/choice -> exiting state -> live audience question`

Every expanded beat changes fact, problem, tactic, choice, relationship, status, resource, cost, danger, reversal, or payoff through human collision. A technical state change alone does not qualify. Bridges stay to one line. Two consecutive preparation/explanation/travel/test/audit/sadness beats are forbidden.

### Traditional Scene Writer

Enter scenes near pressure, give the viewpoint character a current want, let action/dialogue force a choice or new interpretation, select character-specific details, and exit on the strongest changed fact or decision. Do not explain a punch after it lands.

Use this branch only when `presentation=traditional` and `writer_branch=traditional_scene`. Do not apply it, even partially, after push has been locked; do not reuse it for push narration by inserting extra line breaks.

### Flan-Style Push Narrator

Use this branch whenever `presentation=push` and require `writer_branch=flan_push`:

- open result-first: abnormal outcome -> ordinary cause/choice -> immediate pressure, changed status, or live question;
- follow the stop hook with three different opening pressures; do not spend the opening block paying off the hook with biography or lore;
- expand only the selected high-value events, bridge necessary chronology in one line, and cut the rest; never retell the full outline at uniform depth;
- compress around cause and consequence rather than acting out every beat in real time;
- for teaching, training, crafting, diagnosis, or repeated upgrades, compress to `decisive correction -> visible proof -> external consequence`; normally reach proof within 2-4 spoken lines;
- keep professional judgment shorter than the proof and consequence it unlocks; a teacher premise is not a tutorial request;
- keep direct quotation sparse but preserve the few lines whose wording changes conflict, status, allegiance, humiliation, danger, or choice; paraphrase-only human conflict fails;
- make each non-empty line carry one action, reveal, reaction, consequence, or causal turn;
- preserve the narrator's practical judgment, misunderstanding, complaint, or contrast so first person never becomes a neutral camera;
- end each major module on a changed fact and a live pressure, not explanation or atmosphere;
- never treat short lines, `俺`, or a metric pass as proof that the body is push narration;
- draft natural spoken sentences and oral paragraphs through the locked speaker/listener contract first; split subtitles only after the entertainment, retention, and viewpoint gates pass; never add connectors to hit a ratio.

For first person, draft in five passes from the first-person gate: consequence-led report, event selection, narrator mouth, state change, and payoff. For third person, also use five: consequence-led report, event selection, narrator stance/stable labels, state change, and payoff. Then run the shared oral rewrite. In both, the opening exposes the abnormal result and causal gap; the first concrete proof arrives before setup can drain the hook; the main irreversible conflict starts early; the middle changes mechanism after first proof; the climax recycles earlier story debt; the ending proves change with an action.

Only after the blind editor reaches `ready for user read`, run `../story/scripts/validate-flan-push.py` on every saved push body. `surface_fail` blocks push-format delivery and sends the body back to this branch; `surface_pass` remains surface-only.

### Blind Editor

Read before checking length or lint. Complete the exact-anchor/character-percentage evidence map in `../story/references/push-retention-chain.md` for push work, then use one verdict:

- `rebuild core`
- `major structural rewrite`
- `scene rewrite`
- `line edit`
- `ready for user read`

State the earliest loss of interest, what the reader was waiting for, what the text supplied instead, and which earlier role must redo its work. For push, also mark the first low-value event expanded too far, first high-value event compressed too much, first repeated high-point function, first 200-400-character flowchart/procedure run, first module without human collision, first character used only as a function, and earliest line where the narrator becomes a scene camera, neutral report, dialogue transcript, diary voice, tutorial lecturer, or novel broken into subtitles. Then identify the middle mechanism change, climax debt, title-promise payoff position, stronger promise after it or none, post-final-payoff share, ending proof action, five memorable post-opening lines/choices/actions, audio-only verdict, and whether the closed/serialized ending branch was honored. An incomplete or outline-only entertainment/retention map forbids `ready for user read`. Never use numeric quality scores or `PASS`.

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

The default complete Japanese one-shot/episode target is approximately 12,000 Japanese characters. Length is a budget unless the user/platform supplies a real hard limit. If short, return to the high-value event scanner and Entertainment Editor, then add a distinct human obstacle, refusal, consequential choice, relationship turn, pressure, reversal, memorable confrontation, or consequence. Otherwise report the honest shortfall. Never slow one event, restore cut material, or fill with procedures, lore, scenery, more witnesses, policy settlement, or another test of the same conclusion.

One decisive proof per conclusion. A later demonstration survives only when mechanism, stakes, relationship, or result changes.

## Optional Tools

- Browse only for current/ranking/trend claims or a requested live seed. Any item presented as hot/live, including novel rankings, news, YouTube, TikTok, and Google Trends, must be timestamp-verifiable inside the rolling 24-hour JST window.
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
- In the male-isekai lane, no newly created named cast without Japanese-only empty-hand character prompts, and no symbolic object, weapon, tool, skill effect, action, or scene composition inside those prompts.
