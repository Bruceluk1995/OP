# Flan-Style Push Narration Contract

Use this for every male- or female-audience output selected as 动漫解说／推文口播. It distills reusable presentation mechanics rather than source wording. This file governs subtitle readability and oral surface only. It does not judge story quality, retention, originality, entertainment, or first-person authenticity.

Before this surface contract, read `push-entertainment-gate.md` and `push-retention-chain.md`, then complete their adversarial read and saved-body evidence map. For first-person work, read `../../story-first-person-script/SKILL.md` and its push references. For third-person work, read `../../story-third-person-script/SKILL.md` and its push references. The entertainment, retention, and viewpoint release gates outrank every metric in this file.

## Person and Presentation

Presentation and viewpoint are independent, but first person changes more than pronouns:

- First person obeys the narrator's knowledge boundary, selection, judgment, and brief self-reaction.
- Third person uses a deliberate narrator stance, stable sparse labels, selective external reactions, and a consistent knowledge boundary.
- Both may use recap compression and oral lines when push format is selected.

Never convert a novel into push copy by inserting line breaks alone. Never turn first person into diary-like introspection merely because the narrator says 俺／僕／私.

## Surface Guidance

Use these as adjustable diagnostics, not creative targets:

- Prefer one main action, reveal, reaction, consequence, or causal link per non-empty line.
- For Japanese, a median line length around 8-20 characters is usually readable; long lines should be rare.
- Keep direct-quote lines sparse when the requested format is recap narration.
- Vary causal connectors and subject omission naturally.
- Remove timestamps, ASR debris, copied source wording, and disconnected highlight lists.
- Establish a person, a legible event, and an unanswered pressure early.

Draft natural spoken sentences before subtitle splitting. Do not shorten a clear, forceful line merely to hit a percentile. Do not add connectors, quoted dialogue, or line breaks solely to satisfy a ratio. There is no minimum connector quota.

An extremely low median combined with too many spoken units per 1,000 characters signals subtitle-shard over-fragmentation, not energy. Recombine dependent clauses until the script still sounds natural when heard without visible line breaks. High repeated-connector density is a stuffing warning, not proof of causal momentum.

## Editorial Retention Gate

Audit by meaningful story modules or scenes, not fixed 6-10-line windows. Human rhythm is uneven. Never require “one hook every three lines”; hooks must arise from changed facts, consequential choices, or live pressure.

Every major module must change at least one of: fact, problem, choice, tactic, relationship, status, resource, cost, danger, reversal, or payoff. A narrator-specific judgment can sharpen a change but cannot replace one.

- One decisive proof is enough for one conclusion. A second demonstration is valid only when it changes mechanism, stakes, relationship, or result.
- Procedures, staffing, rules, inventories, contracts, tests, training, and chronology are kept only when they alter conflict.
- A teacher, expert, crafter, analyst, doctor, or engineer protagonist does not turn push narration into a tutorial. Keep the decisive professional judgment, then jump to proof and consequence.
- Treat six consecutive lines on one correction, question-and-answer drill, or micro-procedure without a changed fact as a blocking stasis candidate. Short line breaks do not excuse it.
- After a decisive correction or instruction, normally reach visible proof within 2-4 spoken lines. If not, identify the new pressure carried by every intervening line.
- Numbers and rules survive only when they change danger, reward, reputation, choice, or status.
- Male push may use practical complaint, contrast, skill absurdity, enemy misread, loot, or status inflation, but should rotate mechanisms rather than repeat correction scenes.
- Female push may be serious, painful, tender, suspenseful, healing, romantic, or cathartic; jokes are optional.
- Stop explaining once the audience knows what changed and why it matters. Preserve an active question.

Before delivery, clear the matching viewpoint skill's `push-quality-gate.md`. Third person must additionally clear neutral-summary, stable-label, knowledge-boundary, and protagonist-agency tests.

## Surface Lint

For every saved push body before delivery, run:

    python .codex/skills/story/scripts/validate-flan-push.py --body <正文.md> --person first

Use `--person third` for third-person output.

Interpret results literally:

- `surface_pass`: no configured subtitle-shape warning crossed its threshold.
- `surface_fail`: review oral readability and format; rewrite only where the warning identifies a real problem.
- `quality_verdict: not_evaluated`: mandatory reminder that this tool cannot approve a script.
- `retention_verdict: not_evaluated`: the tool did not verify stop/wall hooks, proof timing, conflict timing, true reversals, climax debt, or ending action.
- `scene_progression_verdict: not_evaluated`: the tool did not detect lecture replay, same-action stasis, or explanation padding.
- `high_value_event_selection_verdict: not_evaluated`: the tool did not detect uniform synopsis, rushed high points, repeated peak functions, or weak payoff selection.
- `spoken_units_per_1000_chars`: a fragmentation diagnostic, not a target.
- `warnings`: surface patterns that require listening or editorial review but do not create a quality verdict.
- `delivery_ready_from_this_tool: false`: even `surface_pass` requires the already-completed manual retention and viewpoint gates.

A surface failure blocks delivery under a push-narration label until the identified format problem is editorially reviewed and rewritten. A surface pass can never certify quality and must never be reported as “弗兰验证 PASS” or “剧本通过”.
