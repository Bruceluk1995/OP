---
name: jp-isekai-write
description: "Write and package Japanese male-audience isekai episodes. Use for drafting or rewriting なろう系/カクヨム風 Japanese first-person episodes, 1万-2万字 installments, male protagonist RPG fantasy, cheat-skill slow life, adventurer guild/dungeon arcs, humorous inner monologue, Chinese-to-Japanese isekai localization without xianxia terms, and project-bound episode folders with title files, character prompts, and 16:9 YouTube thumbnail covers."
---

# JP Isekai Write

Write Japanese web-novel episodes for male-audience isekai. Use this for final prose.

## Required Reads

- Read `references/style-guide.md` before writing prose.
- Read `references/terminology.md` before writing if the source material contains Chinese fantasy terms or the user asks to avoid Chinese elements.
- Read `references/episode-blueprint.md` before drafting any episode/chapter prose, especially serial episodes that must hold viewer retention.
- Read `references/anti-ai-gates.md` before drafting and again before final delivery when the user mentions AI flavor, wateriness, weak prose, or when producing a saved episode file.
- Read `references/episode-delivery.md` when the user wants a finished episode, long-form serialization, per-episode files, character prompts, covers/thumbnails, YouTube, or project-bound output.
- Read `references/push-narration-protocol.md` when writing episode 2 or later, adapting for YouTube/recap narration, continuing from previous files, or when the user complains about AI flavor, weak hooks, wateriness, or failure to connect the last episode.

## Drafting Workflow

1. Confirm or infer the episode target:
   - Default: first-person Japanese, male protagonist, light humorous inner monologue, RPG fantasy vocabulary, 8k-20k Japanese characters.
   - If the user gives "每集1.5万字", target around 15,000 Japanese characters including punctuation and line breaks.
2. Build the full episode blueprint from `references/episode-blueprint.md` before prose:
   - Start with the episode's biggest plot bomb in the first sentence, not scenery, weather, mood, or abstract reflection.
   - For episode 2 or later, bridge from the exact previous ending before moving into new action.
   - Set target emotion, episode position, episode promise, core payoff, cost/risk, and ending hook.
   - Use a five-part shape: cause, development, turn, climax, ending state.
   - Break the episode into dense/sparse beats with target character budgets.
   - Make dense beats carry skill experiments, public proof, comic reaction, zamaa, practical reward, or new danger.
   - Compress sparse transitions; do not let travel, explanation, or mood become filler.
   - End with a specific next-episode trouble hook.
3. Write in Japanese prose:
   - Prefer `俺` first-person unless the user asks otherwise.
   - Use short inner-commentary beats for humor.
   - Keep paragraphs readable for web serialization.
   - Do not insert Chinese names, cultivation terms, sect terms, or Chinese monster taxonomy.
4. Run the JP anti-AI pass from `references/anti-ai-gates.md`:
   - Remove generic abstract texture without deleting plot function.
   - Convert mood/summary lines into objects, actions, dialogue, body response, price, rule, witness, or consequence.
   - Break uniform rhythm; keep dense beats visibly denser than transitions.
   - If prose was saved to a file, run the local scripts:
     `node .codex/skills/jp-isekai-write/scripts/check-ai-patterns.js --check --fail-on=blocking <file>`
     `node .codex/skills/jp-isekai-write/scripts/check-degeneration.js --check --fail-on=blocking <file>`
     `node .codex/skills/jp-isekai-write/scripts/normalize-punctuation.js <file>`
5. Save long outputs to a file when the result would be too large for chat. For project-bound episodes, create the per-episode delivery folder described in `references/episode-delivery.md`.
6. Package delivery assets when applicable:
   - `正文.md`, `标题.md`, `角色提示词.md`, `封面.md`, and an actual generated `封面.png`.
   - Continue syncing a flat `episodes/episode_XXX_ja.md` only for compatibility when the project already uses it.
7. Validate:
   - Count Japanese characters with Python.
   - Scan for banned Chinese leakage using `references/terminology.md`.
   - Check the draft against `references/episode-blueprint.md`: target emotion delivered, dense beats expanded, sparse beats compressed, cost/reward/status consequence present, and ending hook specific.
   - Scan the first 600 Japanese characters against `references/push-narration-protocol.md`: plot-bomb sentence, previous-episode recap bridge, concrete conflict, and no generic AI-flavored filler.
   - Scan the whole draft against `references/anti-ai-gates.md`: no generic texture, stock summary lines, author explanation, uniform paragraph rhythm, or model/meta leakage.
   - If below target by more than 10%, expand existing dense beats rather than adding random scenes.
   - If a cover is expected, verify `封面.png` exists, is 16:9, includes the episode click-title and the series/work title, and is an actual image file rather than only a prompt.

## Quality Bar

The episode must feel like Japanese isekai, not translated Chinese xianxia. The reader should immediately understand the social system, the cheat's rule, why the protagonist wants safety/profit/slow life, and what problem pulls him into the next installment.
