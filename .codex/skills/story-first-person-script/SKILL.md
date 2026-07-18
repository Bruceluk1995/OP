---
name: story-first-person-script
description: First-person short-script creation, audit, and true rewriting across commercial fiction. Use when a draft merely swaps pronouns, breaks the narrator's knowledge boundary, sounds like a diary, over-explains emotion, lacks a distinctive narrator mouth, or falsely claims appended old text is rewritten. Japanese male/female genre promises remain owned by the matching jp-* skill.
metadata: {"openclaw":{"source":"https://github.com/worldwonderer/oh-story-claudecode"}}
---

# First-Person Short Script

Mandatory topic gate: when invoked without a fixed source premise and this
skill must invent, select, or materially change a topic, title, or story angle,
read `../story/references/global-topic-history.md` and obtain the company-wide
online reservation before outlining. Viewpoint-only editing of a fixed source
does not create a new topic.

This skill owns viewpoint craft, not genre routing. Use the selected genre skill for market promise and localization, then apply this first-person workflow directly.

For anime recap/push narration, read `../story/references/push-prompt-architecture.md`, `../story/references/push-entertainment-gate.md`, `../story/references/push-retention-chain.md`, `references/push-first-person-benchmark.md`, and `references/push-quality-gate.md` before outlining or rewriting. The prompt architecture locks a concrete speaker/listener and audience emotional contract; the entertainment gate rejects accurate-but-boring flowcharts, personality-free modules, misplaced payoff, and subtitle fragmentation; the retention contract distinguishes a sustained push chain from a strong opening followed by setup; the benchmark distinguishes a narrator-led oral account from first-person web-novel scenes with short line breaks; the release gate controls narrator mouth, middle change, climax payoff, and ending proof.

## Narrator Engine

Before outlining, lock:

```text
What I know now / cannot know
What I notice first / habitually ignore
How I judge money, danger, love, status, and shame
What I want in the current scene
What I refuse to admit
What choice only I would make
Who I am telling this to and why now
Dominant pressure emotion -> mid-story conversion -> final release
```

First person changes information selection, judgment, misunderstanding, reaction, and sentence flavor. It is not a pronoun replacement and does not require long introspection.

## Push Oral Spine

For push work, lock the `1 + 3 + N` chain from `../story/references/push-retention-chain.md` and the compact oral spine from `references/push-quality-gate.md` before prose: abnormal outcome, ordinary cause/choice, immediate cost or status loss, audience wait, narrator filter, first proof, irreversible conflict, middle mechanism changes, climax debt, and ending proof action. If any field is missing, do not draft around the gap.

## Native Workflow

1. State the reader's concrete waiting and the protagonist's desire.
2. Build a causal core: ordinary trouble -> narrator's unusual choice -> visible result -> new-kind trouble -> costly climax choice -> changed ending.
3. For push, scan candidate events with the shared contracts and label them `expand / one-line bridge / cut`. Every expanded event must include a present desire, blocker, visible human collision, price/status/relationship risk, narrator take, and memorable action or decisive line. Do not narrate every event at equal depth.
4. Group selected beats as `entering state -> my choice/interpretation -> human collision -> exiting state -> live question`. A technical state change alone does not qualify.
5. Draft only what the narrator can observe, infer, remember, misunderstand, or later learn. Let withheld admission create tension; do not hide facts the narrator is actively using.
6. Keep narration and dialogue compatible with one person's social position and priorities. A practical judgment is stronger than a generic joke.
7. Run the five push passes when applicable: report, event selection, narrator mouth, change, and payoff; then draft natural spoken sentences before any subtitle split and run the shared oral rewrite.
8. Blind-read the saved body, complete the entertainment adversarial read and retention contract's exact-anchor/character-percentage evidence map, and find the first low-value event expanded too far, high-value event compressed too much, repeated high-point function, flowchart/procedure run, character used only as a function, early payoff with long tail, or point where the narrator becomes a neutral reporter, diary writer, or author explainer. Rewrite from the earliest failed stage.
9. Apply every blocking test in `references/push-quality-gate.md` before surface lint. A blocking failure returns to the earliest responsible pass.

For push work, also require result-first opening, causal compression, sparse decisive quotation, narrator-specific practical judgment, and a changed fact/live question at each major module ending.

Do not enforce “one reversal every three lines.” Hooks must come from changed facts, consequential choices, or unresolved pressure. Short lines, slogans, and contrast templates cannot substitute for progression.

## True Rewrite

Extract user-approved facts and anchors, create a fresh causal/change outline, and draft from it. Run `scripts/verify-rewrite.py --old <old> --new <new>` when files exist. Copying the old body and appending an ending is a blocking failure; script success does not certify story quality.

## Hard Rules

- No hidden thoughts or off-screen facts presented as certainty.
- No three paragraphs explaining an emotion already shown by one specific action or object.
- No repeated proof or procedure used to keep the narrator talking.
- No expanded module that would read the same through a neutral camera; first-person selection, judgment, misunderstanding, refusal, or choice must remain locally visible.
- No central payoff followed by a policy list, second test, second climax, or extended safe-return procedure.
- No connector stuffing or clause-by-clause line breaking used to imitate oral momentum.
- No uniform retelling of the outline; expand high-value events, bridge necessary chronology once, and cut the rest.
- No narrator commentary that merely repeats the visible action without adding cause, judgment, implication, contrast, or consequence.
- No length, pronoun count, short-line ratio, or rewrite-similarity pass used as a quality verdict.
- No first-person scene transcript delivered as push narration merely because lines are short.
- No surface lint before the editorial release gate reaches `ready for user read`.
