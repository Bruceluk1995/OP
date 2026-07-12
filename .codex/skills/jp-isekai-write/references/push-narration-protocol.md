# Push Narration Protocol

Use this when writing Japanese male-audience isekai as video recap or push narration copy, whether short, long, standalone, or serialized.

Push narration is a presentation mode, not a viewpoint. It may use first person or third person. Confirm and lock the narrative person before drafting.

Read `../../story/references/flan-push-strict-mode.md` and treat it as the hard surface contract. This protocol controls content flow; the strict profile controls line length, quote ratio, clause density, and delivery validation.

This protocol governs oral delivery, information density, and retention. Use it with `episode-blueprint.md` for serial structure, `../../jp-isekai/references/presentation-modes.md` for the two-axis format gate, and `anti-ai-gates.md` for final cleanup.

## Narrative Person Lock

- First person: the protagonist tells the causal chain through `我/俺`. Keep the selected high-clarity hook and dense information turns. Do not reveal hidden facts the narrator cannot know unless marked as later-learned information.
- Third person: use `男主`, a stable role label, or a name once the listener can track it. The narrator may show external misunderstandings and witness reactions directly.
- Do not alternate first and third person for convenience. A quoted line does not change the narration person.
- Neither person changes push-copy structure: hook, causal gap, minimum setup, escalation, proof, aftershock, and ending pressure/closure. Viewpoint does not determine the opening mechanism.
- Neither person changes the Flan-style surface metrics. First-person push is not an intimate web-novel scene with shorter paragraphs.

## Why The Old Output Feels AI

The bad pattern is:

1. Start with atmosphere or abstract emotion.
2. Reintroduce the protagonist as if episode 1 is starting again.
3. Summarize feelings instead of naming the current concrete problem.
4. Delay the payoff until after several soft paragraphs.

That produces pretty but empty prose. For push-video episodes, the opening must behave like retention copy.

## Opening Selection

Before writing, run the random template draw in `../../jp-isekai/references/opening-innovation-engine.md` with `--root` so recent cards are excluded automatically. Follow the selected card and preserve its returned `required_chain`. After saving, create `开头抽卡证据.json` with exact quotes for every slot and run `validate-opening-evidence.py`. The fixed order below is only a repair scaffold when the selected card requires a result-first plot-bomb chain.

## Result-First Repair Order

Write the first 250-500 Japanese characters in this order:

1. **Plot-bomb first sentence.** Put the whole episode pressure in sentence one: accusation, betrayal, monster, debt, impossible result, guild ruling, public humiliation, or a choice with cost.
2. **Previous-episode bridge.** In 1-3 sentences, state what happened last episode and what remains unresolved. Use proper nouns, objects, money, wounds, contracts, guild ranks, monster names, or skill effects.
3. **Now-problem.** Name the immediate obstacle that forces today's scene to begin.
4. **Protagonist reaction.** Add one short practical reaction: direct self-comment in first person, or observable/brief reported reaction in third person.
5. **Scene entry.** Move into action, dialogue, or a visible object. Do not stay in explanation.

Do not label these parts as recap or summary inside the prose unless the user explicitly asks for narration labels.

## Oral Line and Shot Logic

- Write one action, reaction, reveal, or causal link per short line when the delivery format supports line breaks.
- Make the first 3-6 lines establish the protagonist, abnormal event, and contradiction/curiosity gap.
- Prefer chronological cause-effect movement after the selected hook unless another order is explicitly justified by the chosen structure card.
- Use concrete outcomes instead of labels such as `很强`, `很惨`, or `很震惊`.
- Keep each important setup tied to a later proof. Compression must not become a list of disconnected highlights.
- Vary connectors. `没想到`, `不料`, `殊不知`, `竟然`, and `就在这时` are functions, not a template to repeat mechanically.
- For original fiction, borrow only these presentation mechanics. Do not copy source-IP titles, scene order, dialogue, characters, or plot turns.
- If adapting subtitles, remove timestamps, repeated lines, source-dialogue debris, mistranscribed names, ASR fragments, and any sentence that cannot stand without the original audio.

## Continuity Inputs

Before writing episode 2 or later:

- Read the previous episode file or folder.
- Extract: final event, unresolved hook, new item/skill/familiar, current location, current social pressure, promised next action, and any running joke.
- Start the new episode from one of those extracted items. If no previous episode can be found, state the gap and create a provisional recap from the user's prompt instead of inventing continuity silently.
- Feed these extracted items into the `episode-blueprint.md` continuity lock before prose.

## Push-Style Beat Density

Every 800-1200 Japanese characters should contain at least one of:

- a new concrete problem
- a visible skill experiment
- a public reaction
- a price/reward/status consequence
- a comic reversal
- a new object or monster behavior
- a choice that changes the next scene

For shorter copy, scale this proportionally: do not allow a long stretch without a new problem, rule, tactic, reaction, proof, reward, status change, or danger.

If two consecutive paragraphs only describe mood, scenery, resolve, fate, warmth, sadness, beauty, or "the beginning of a new life", rewrite them into action.

## Anti-AI Prose Rules

Ban or heavily restrict:

- abstract theme sentences
- generic emotional adjectives without a body action
- repeated sighing, trembling, smiling, warmth, light, destiny, silence
- "as if the world..." metaphors
- paragraphs that only explain what the reader should feel
- recap that says "many things happened" instead of naming the actual things

Prefer:

- named documents, coins, tools, guild tags, monster parts, doors, wounds, ledgers, witness reactions, food, rent, and weather only when it affects action
- dialogue that changes social pressure
- one practical joke or complaint after a serious beat
- cause-effect sentence chains: because X happened last episode, Y is dangerous now, so the protagonist tries Z

## Opening Self-Check

Before delivering, answer internally:

- Does sentence one contain a concrete bomb?
- Is the chosen first/third person consistent?
- Could a new viewer understand the last episode's hook by line five?
- Does the first scene begin from the previous ending rather than a reset?
- Are there at least three concrete nouns in the first 250 Japanese characters?
- Did I remove decorative AI water before expanding length?
- Did I remove subtitle/ASR debris and vary repetitive connectors?
- If the prose is saved to a file, did Codex AI reread the saved file and fix real issues?
- Did `validate-opening-evidence.py` pass every slot in the drawn card rather than merely confirming that the card ID was recorded?
