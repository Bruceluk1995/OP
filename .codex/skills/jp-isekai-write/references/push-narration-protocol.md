# Push Narration Content Protocol

Use for Japanese male-audience isekai video recap or push narration, standalone or serialized. Push narration is a presentation mode, not a viewpoint.

Read `../../story/references/flan-push-strict-mode.md` for surface lint. For first-person output, also use `../../story-first-person-script/SKILL.md`, its benchmark, and `../../story-first-person-script/references/push-quality-gate.md`; those editorial rules control knowledge, voice, retention, and true rewriting.

## Person Lock

- First person: narrate only what the protagonist knows, observes, infers, misunderstands, or later learns. Select details through that person's priorities and practical judgment.
- Third person: use stable, sparse role labels and may show external reactions.
- Do not alternate viewpoint for convenience.
- Do not confuse first person with added introspection or a simple pronoun swap.

## Oral Spine and Opening

For first person, lock the oral spine in `push-quality-gate.md` before drafting. For third person, lock the same fields except narrator mouth.

Lock a visual story core:

`ordinary action/loss -> visible change -> human consequence`

Then open result-first:

1. abnormal visible outcome or contradiction;
2. ordinary cause, choice, or profession behind it;
3. immediate cost, humiliation, or changed status;
4. unanswered pressure that makes continuation necessary.

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

## Change Density

Every major module must add a new fact/problem/choice/tactic/relationship/status/cost/reversal/payoff. Do not enforce a fixed 800-1200-character cadence; that creates mechanical rhythm.

One important claim receives one decisive proof. After proof, introduce a different problem. A repeat demonstration survives only if it changes mechanism, stakes, relationship, or consequence.

If two consecutive passages only describe mood, resolve, travel, preparation, explanation, or the same witness reaction, merge, cut, or replace them.

## Continuity for Episode 2+

Extract from the previous episode: final event, unresolved pressure, new item/skill, location, relationship/status change, promised action, and running joke. Start from one of these. If the previous episode is unavailable, state the gap instead of inventing continuity silently.

## Final Audit

- What makes the first 30 seconds necessary to continue?
- What changes in every module?
- Which conclusion is proved twice?
- Where does explanation continue after meaning is clear?
- In first person, which details prove this narrator selected and judged the story?
- Does the climax solve the changed problem rather than restage the first proof?
- Does a one-shot close its promise without a next-episode bridge?
- What changed after the first decisive proof, instead of repeating it?
- Which earlier choice, tool, relationship, mistake, or restraint pays for the climax?
- What final action proves change without a moral paragraph?
- Which named companion materially changes the plan, rescue, information, cost, or result?
- If surface lint ran, is it labeled surface-only rather than quality approval?

For first-person push, complete the full blind-read template in `push-quality-gate.md`. Only a `ready for user read` editorial verdict proceeds to surface lint.
