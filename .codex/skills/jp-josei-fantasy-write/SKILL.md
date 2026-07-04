---
name: jp-josei-fantasy-write
description: "Write Japanese female-audience fantasy romance prose. Use for drafting or rewriting 女性向け異世界恋愛, 悪役令嬢, 婚約破棄, ざまぁ, 溺愛, 聖女, 契約婚, 令嬢, 宮廷ロマンス, frontier slow life, cursed prince/duke romance, time-loop villainess, and Japanese prose localized away from Chinese fantasy or male-audience RPG defaults."
---

# JP Josei Fantasy Write

Write Japanese web-novel prose for female-audience fantasy romance. Use this for audience-facing scenes, chapters, rewrites, and localization.

## Required Reads

- Read `references/style-guide.md` before writing prose.
- Read `references/terminology.md` before writing if the source material contains Chinese fantasy terms or the user asks to avoid Chinese elements.
- Read `references/episode-blueprint.md` before drafting any episode/chapter prose, especially serial episodes that must hold viewer retention.
- Read `references/anti-ai-gates.md` before drafting and again before final delivery when the user mentions AI flavor, wateriness, weak prose, or when producing a saved episode file.
- Read `references/push-episode-delivery.md` when writing episode 2 or later, YouTube/recap/push narration, per-episode folders, character prompts, covers, or when the user complains about AI flavor, weak hooks, wateriness, or failure to connect the previous episode.

## Drafting Workflow

1. Confirm or infer the target:
   - Default: Japanese prose, heroine-centered, emotionally legible, romance-forward, happy-ending direction.
   - Use first person `私` or close third person. Pick the viewpoint that best supports the heroine's dignity and romantic tension.
   - If the user gives an episode length, target that character count; otherwise keep chat drafts concise or save long chapters to a file.
2. Build the full episode blueprint from `references/episode-blueprint.md` before prose:
   - Start with the episode's biggest social/emotional bomb in sentence one: humiliation, accusation, broken engagement, witness testimony, contract reveal, curse symptom, public choice, or betrayal.
   - For episode 2 or later, bridge from the exact previous ending before moving into new action.
   - Set target emotion, episode position, episode promise, core payoff, cost/risk, and ending hook.
   - Use a five-part shape: cause, development, turn, climax, ending state.
   - Break the episode into dense/sparse beats with target character budgets.
   - Make dense beats carry humiliation, evidence, heroine choice, male-lead recognition, zamaa, tenderness, or social consequence.
   - Compress sparse transitions; do not let etiquette, scenery, or sadness become filler.
   - End with a romance question, social threat, witness, document, or next-stage proof.
3. Write in Japanese prose:
   - Use natural Japanese paragraphing and dialogue.
   - Let status, rank, magic, and setting emerge through action and social behavior.
   - Make `溺愛` visible through concrete choices: protection, listening, resources, public acknowledgement, remembering details.
   - Keep `ざまぁ` dramatic but coherent. The heroine can be kind without being passive.
4. Run the JP anti-AI pass from `references/anti-ai-gates.md`:
   - Remove generic abstract texture without deleting evidence, romance, or zamaa function.
   - Convert mood/summary lines into documents, hands, doors, witnesses, contracts, titles, injuries, choices, or social consequences.
   - Break uniform rhythm; keep dense beats visibly denser than transitions.
   - If prose was saved to a file, run the local scripts:
     `node .codex/skills/jp-josei-fantasy-write/scripts/check-ai-patterns.js --check --fail-on=blocking <file>`
     `node .codex/skills/jp-josei-fantasy-write/scripts/check-degeneration.js --check --fail-on=blocking <file>`
     `node .codex/skills/jp-josei-fantasy-write/scripts/normalize-punctuation.js <file>`
5. Validate:
   - Scan for Chinese/xianxia leakage using `references/terminology.md`.
   - Check that the heroine acts, the romance advances, and the scene promise matches the chosen tags.
   - Check the draft against `references/episode-blueprint.md`: target emotion delivered, dense beats expanded, sparse beats compressed, evidence/romance/status consequence present, and ending hook specific.
   - Scan the first 600 Japanese characters against `references/push-episode-delivery.md`: plot-bomb sentence, previous-episode recap bridge, concrete social pressure, and no generic AI-flavored filler.
   - Scan the whole draft against `references/anti-ai-gates.md`: no generic texture, stock summary lines, author explanation, uniform paragraph rhythm, or model/meta leakage.
   - If the prose reads like a synopsis, expand into scene-level action, dialogue, and internal reaction.

## Quality Bar

The result must feel like Japanese 女性向け異世界恋愛, not translated Chinese court fantasy and not male-audience RPG progression. The reader should understand the heroine's wound, why the male lead values her, what social injustice is being corrected, and why the happy ending feels emotionally deserved.
