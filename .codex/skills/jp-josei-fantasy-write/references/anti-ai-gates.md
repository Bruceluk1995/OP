# JP Josei Fantasy Anti-AI Gates

Use this after the episode blueprint and again after drafting. It adapts the generic `story-deslop` gates to Japanese female-audience fantasy romance prose.

Goal: remove AI texture without flattening heroine emotion, romance tension, zamaa satisfaction, or push-narration retention.

## Gate 0: Protect Plot Function

Do not rewrite for prettiness. Keep:

- plot-bomb opening
- previous-episode bridge
- evidence, document, witness, contract, title, etiquette, injury, curse, rumor, or church/court rule continuity
- heroine agency
- male-lead recognition through action
- zamaa/social consequence logic
- next-episode hook

Only change how a line says the thing. Do not invent new plot, new rules, or new relationships during deslop.

## Gate A: Delete Generic Texture

Ban or heavily restrict generic lines that could fit any story:

- `運命`, `宿命`, `光`, `静寂`, `温かさ`, `胸が締め付けられる`, `涙がこぼれた`, `世界が色を失う`, `新しい人生`
- repeated trembling, tears, sighing, soft smiles, vague pain, vague beauty, light/silence imagery
- atmosphere paragraphs with no document, witness, hand movement, seating order, title, contract, door, injury, rumor, or social consequence

Replace with josei-specific anchors:

- torn letter, seal, family ledger, church record, witness name, glove, seat, cup, contract clause, debt amount, bruised wrist, door handle, servant whisper
- a social action: refuse a seat, ask for a witness, sign with the left hand, fold evidence away, return a title, choose a public answer

## Gate B: Break Stock Sentences

Rewrite:

- `それは悲しみではなく...` when it only sounds neat.
- `まるで世界が...` metaphors.
- `その瞬間、すべてが変わった` summary lines.
- polite explanatory paragraphs that state the heroine's wound, dignity, or love instead of showing it.
- romance praise that could be said to any heroine.

Prefer:

- evidence first, emotion second
- a public reaction before the heroine's inner line
- male-lead recognition through a specific action: preserving evidence, changing seating, remembering a detail, risking status, naming the injustice

## Gate C: Externalize Emotion

Female-audience prose may state strong emotion, but it must be tied to a scene object or action.

Weak:

- `私は深く傷ついた`
- `胸が苦しくなった`
- `涙が止まらなかった`

Stronger:

- she smooths the torn contract edge before answering
- she keeps the cup level though her glove is wet
- she counts witness names instead of looking at her father
- she signs with the hand her family said was useless
- she closes the ledger before the male lead can see one private line

## Gate D: Fix Rhythm And Density

- Dense beats get document/action/dialogue/witness/social consequence.
- Sparse beats get one or two sentences.
- Do not make every paragraph the same length.
- Do not let etiquette, scenery, or sadness receive the same weight as accusation, proof, or romantic recognition.
- If `scripts/check-ai-patterns.js` reports `period-stutter`, merge short fragments into a fuller action chain.
- If it reports `long-paragraph`, split by new action, object, line of dialogue, or social turn.

## Gate E: Make Dialogue Social

Female fantasy romance dialogue is status pressure.

- A father, prince, saint, duke, servant, and heroine should not share the same polished voice.
- Replace exposition dialogue with accusation, evasion, etiquette, rank, witness demand, contract term, or public choice.
- Let the heroine answer with precision, not passivity.
- Let the male lead protect through legal/social action, not generic possessive praise.

## Gate F: End On Evidence, Choice, Or Romantic Question

Do not end with abstract healing, destiny, or "a new life begins."

End with:

- a witness stepping through the door
- a seal that should not exist
- a contract clause being read aloud
- a title returned or granted
- a public accusation changing target
- the male lead asking a question that changes the heroine's next choice

## Gate G: Remove Author Explanation

Delete or convert:

- `私はまだ知らなかった`
- `これが後に...`
- `つまり...`
- `それは大きな意味を持っていた`
- narrator explanations of what the reader should feel about the heroine, male lead, family, or revenge

Convert them into what the heroine can see, hear, touch, count, misread, or choose now.

## Deterministic File Pass

When the episode is saved to a file, run the local scripts from this skill:

```powershell
node .codex/skills/jp-josei-fantasy-write/scripts/check-ai-patterns.js --check --fail-on=blocking <episode-file>
node .codex/skills/jp-josei-fantasy-write/scripts/check-degeneration.js --check --fail-on=blocking <episode-file>
node .codex/skills/jp-josei-fantasy-write/scripts/normalize-punctuation.js <episode-file>
```

If running from inside the skill directory, use `node scripts/...`.

Interpretation:

- `blocking`: fix or regenerate the affected paragraph before delivery.
- `advisory`: inspect manually; keep justified court reasoning, social silence, or deliberate short emotional beats.
- The scripts are conservative and language-mixed. They catch punctuation, stutter, long paragraphs, meta leakage, and some Chinese AI structures; they do not replace human Japanese prose review.

## Final Self-Check

- Did I remove abstract filler without deleting evidence, romance, or zamaa function?
- Does every emotional line have an object, action, dialogue, body response, or social consequence?
- Are dense beats visibly denser than transitions?
- Does the ending hook point to a concrete next witness, document, accusation, romantic question, or public choice?
- Did no engineering words, placeholders, or model refusal text leak into prose?
