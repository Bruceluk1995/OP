# Push Narration Protocol

Use this when writing serial Japanese male-audience isekai for video recap, push narration, or project episodes that must connect across installments.

This protocol governs the opening and retention surface. Use it together with `episode-blueprint.md`, which governs the whole episode's emotion target, dense/sparse beats, payoff, cost, and ending hook, and `anti-ai-gates.md`, which governs Codex AI final prose cleanup.

## Why The Old Output Feels AI

The bad pattern is:

1. Start with atmosphere or abstract emotion.
2. Reintroduce the protagonist as if episode 1 is starting again.
3. Summarize feelings instead of naming the current concrete problem.
4. Delay the payoff until after several soft paragraphs.

That produces pretty but empty prose. For push-video episodes, the opening must behave like retention copy.

## Mandatory Opening Order

Write the first 250-500 Japanese characters in this order:

1. **Plot-bomb first sentence.** Put the whole episode pressure in sentence one: accusation, betrayal, monster, debt, impossible result, guild ruling, public humiliation, or a choice with cost.
2. **Previous-episode bridge.** In 1-3 sentences, state what happened last episode and what remains unresolved. Use proper nouns, objects, money, wounds, contracts, guild ranks, monster names, or skill effects.
3. **Now-problem.** Name the immediate obstacle that forces today's scene to begin.
4. **Protagonist reaction.** Add one short male-protagonist inner comment or practical complaint.
5. **Scene entry.** Move into action, dialogue, or a visible object. Do not stay in explanation.

Do not label these parts as recap or summary inside the prose unless the user explicitly asks for narration labels.

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
- Could a new viewer understand the last episode's hook by line five?
- Does the first scene begin from the previous ending rather than a reset?
- Are there at least three concrete nouns in the first 250 Japanese characters?
- Did I remove decorative AI water before expanding length?
- If the prose is saved to a file, did Codex AI reread the saved file and fix real issues?
