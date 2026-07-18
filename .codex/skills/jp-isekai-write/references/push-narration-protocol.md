# Push Narration Content Protocol

Use for Japanese male-audience isekai video recap or push narration, standalone or serialized. Push narration is a presentation mode, not a viewpoint.

Read `../../story/references/push-prompt-architecture.md` for speaker/listener, emotional, concrete-anchor, and role separation locks; `../../story/references/push-entertainment-gate.md` for human heat and payoff shape; `../../story/references/push-retention-chain.md` for retention structure; and `../../story/references/flan-push-strict-mode.md` for surface lint. For first-person output, use `../../story-first-person-script/SKILL.md` and its push references. For third-person output, use `../../story-third-person-script/SKILL.md` and its push references. Those editorial rules control entertainment, knowledge, narrator stance, retention, and true rewriting.

The shared retention file also owns the global production prompt: delivery lock -> high-value event scan -> event chain -> spoken draft -> oral rewrite -> blind edit. Follow that order for both original stories and source adaptations.

## Person Lock

- First person: narrate only what the protagonist knows, observes, infers, misunderstands, or later learns. Select details through that person's priorities and practical judgment.
- Third person: use stable sparse labels, selective external reactions, and an explicit narrator stance. Do not become neutral chronology or head-hop for convenience.
- Do not alternate viewpoint for convenience.
- Do not confuse first person with added introspection or a simple pronoun swap.

## Oral Spine and Opening

Lock the matching viewpoint skill's oral spine before drafting. First person locks narrator mouth and knowledge; third person locks narrator stance, stable labels, external-reaction selection, and knowledge boundary.

Lock a visual story core:

`ordinary action/loss -> visible change -> human consequence`

Then open result-first:

1. abnormal visible outcome or contradiction;
2. ordinary cause, choice, or profession behind it;
3. immediate cost, humiliation, or changed status;
4. unanswered pressure that makes continuation necessary.

Build the full `1 + 3 + N` chain before prose. The stop hook must be followed by three different opening pressures and then by continuing changed-fact questions. Do not answer the first hook with biography, setting explanation, or a training chronology.

Do not delay the strongest contradiction behind routine scene entry. “Every three lines a reversal” is not a substitute for a causal gap.

The opening deck in `../../jp-isekai/references/opening-innovation-engine.md` is optional ideation. Use it only when it improves the event. Normal delivery requires no random draw, card ID, slot evidence, or validator.

For a standalone one-shot, never add a previous-episode bridge. For episode 2 or later, read the previous ending and bridge only the unresolved event needed now.

## Oral and Shot Logic

- Compress around causes and consequences, not around a fixed line length.
- Establish a person, abnormal event, and live question early.
- Introduce institutions while they act: refuse, seize, charge, accuse, reward, or lose.
- Show a physical or social result before naming a magical material or production rule.
- Keep only numbers, rules, and proper nouns that change the current choice or result.
- Dialogue, reported speech, narration, and reaction should sound compatible with the same character world.
- Remove timestamps, source-dialogue debris, ASR fragments, and disconnected highlights.
- Draft natural spoken sentences and short oral paragraphs before subtitle splitting. Do not create rhythm by breaking every dependent clause or inserting connectors to hit a ratio.

## High-Value Selection

- Do not narrate the outline at uniform depth. Mark every candidate event `expand / one-line bridge / cut` before prose.
- Expand conflict, reversal, information bombs, relationship changes, visual proof, status/reward changes, costly choices, and payoff.
- Bridge necessary chronology once. Cut scenery, routine movement, full lore, minor chatter, repeated reactions, and repeated proof.
- Rotate high-point functions. Escalation is not three larger versions of the same skill display.
- After a high point, introduce a different live question. Do not reset to biography, rules, or routine setup.
- Add narrator information value: causality, practical judgment, comparison, hidden implication, or consequence. Do not merely describe what the image already shows.

## Human Heat and Entertainment

- For every event marked `expand`, identify who wants what now, who blocks it, the visible collision, human price/status/relationship at risk, narrator take, memorable action or decisive exact line, and the next audience question.
- A change to pipes, routes, rules, skill labels, contracts, ledgers, registries, or institutions is bridge material unless it forces a person to choose, refuse, lose, expose, betray, risk, or change a relationship/status.
- If roughly 200-400 consecutive characters mainly explain system operation or assign functions while no person makes a consequential choice, compress the flowchart to the one consequence the audience must understand.
- Named companions must not read as interchangeable skill modules. Give each important companion a distinct desire, refusal, risk, choice, or exact line that changes the plan or relationship.
- Preserve a few decisive exact lines when their wording changes power, allegiance, humiliation, danger, or choice. Report routine dialogue; do not produce a transcript.
- Pay the title/central promise normally inside the final 15-25% of a closed one-shot. If it pays earlier, a stronger different promise must remain. After the final central payoff, default to roughly 10-15% or less for one consequence beat and one ending proof.

## Change Density

Every major module must add a new fact/problem/choice/tactic/relationship/status/cost/reversal/payoff. Do not enforce a fixed 800-1200-character cadence; that creates mechanical rhythm.

One important claim receives one decisive proof. After proof, introduce a different problem. A repeat demonstration survives only if it changes mechanism, stakes, relationship, or consequence.

If two consecutive passages only describe mood, resolve, travel, preparation, explanation, or the same witness reaction, merge, cut, or replace them.

## Teaching and Skill-Growth Compression

For teacher, mentor, crafter, appraisal, research, or repeated skill-growth premises:

1. Keep one visible mistake or blocked result only when the audience needs it.
2. Give the protagonist one decisive diagnosis, correction, or unusual choice.
3. Reach the impossible skill proof within 2-4 spoken lines by default.
4. Make the proof immediately expose danger, hostility, ownership, cost, or a new rule.

Do not replay the whole lesson as `question -> answer -> explanation -> retry -> safety lecture -> review`. That is classroom chronology even when every line is short.

One flagship lesson may show the engine. Compress later lessons to `sharp correction -> different result -> different complication`. If the protagonist's professional filter takes more text than the proof and consequence combined, cut the filter to the one judgment only this narrator would make.

## Continuity for Episode 2+

Extract from the previous episode: final event, unresolved pressure, new item/skill, location, relationship/status change, promised action, and running joke. Start from one of these. If the previous episode is unavailable, state the gap instead of inventing continuity silently.

For a closed one-shot, pay the title promise, show an observable aftermath, and stop. Do not append a generic next-episode tease. For serialization, end on a concrete new event or decision rather than withholding a fact the narrator already knows.

## Final Audit

- Complete the saved-body exact-anchor/character-percentage map in `../../story/references/push-retention-chain.md`.
- What makes the first 30 seconds necessary to continue?
- What changes in every module?
- Which events were expanded, bridged, and cut, and was any low-value event given more space than a high-value one?
- Which two adjacent high points perform the same function and should be merged or replaced?
- Which conclusion is proved twice?
- Where does explanation continue after meaning is clear?
- What is the longest same-action teaching/procedure run, and how many lines separate correction from proof?
- Does any later upgrade repeat the flagship lesson instead of changing the problem?
- In first person, which details prove this narrator selected and judged the story?
- Does the climax solve the changed problem rather than restage the first proof?
- Does a one-shot close its promise without a next-episode bridge?
- What changed after the first decisive proof, instead of repeating it?
- Which earlier choice, tool, relationship, mistake, or restraint pays for the climax?
- What final action proves change without a moral paragraph?
- Which named companion materially changes the plan, rescue, information, cost, or result?
- Where does entertainment first die even though facts continue to change?
- What is the first 200-400-character flowchart/procedure run, or none?
- Which expanded module lacks a human collision?
- Which important character functions only as a skill or solution module?
- At what character percentage does the title/main promise pay, what stronger promise remains after it, and what is the post-final-payoff share?
- Name five memorable lines, choices, or actions after the opening. If this is impossible, the opening is hiding a weak middle.
- Does the piece remain clear, personal, and punchy by audio alone with line breaks hidden?
- Does first-person voice survive locally in every expanded module, or does third-person narrator stance turn neutral?
- If surface lint ran, is it labeled surface-only rather than quality approval?

Complete the retention evidence map and the matching viewpoint skill's full blind-read template. Only a supported `ready for user read` editorial verdict proceeds to surface lint.
