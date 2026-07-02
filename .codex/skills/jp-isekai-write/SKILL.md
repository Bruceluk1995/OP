---
name: jp-isekai-write
description: "Write Japanese male-audience isekai prose. Use for drafting or rewriting なろう系/カクヨム風 Japanese first-person episodes, 1万-2万字 Japanese webnovel installments, male protagonist RPG fantasy, cheat-skill slow life, adventurer guild/dungeon arcs, humorous inner monologue, and Japanese localization of Chinese webnovel settings without Chinese fantasy terminology."
---

# JP Isekai Write

Write Japanese web-novel episodes for male-audience isekai. Use this for final prose.

## Required Reads

- Read `references/style-guide.md` before writing prose.
- Read `references/terminology.md` before writing if the source material contains Chinese fantasy terms or the user asks to avoid Chinese elements.

## Drafting Workflow

1. Confirm or infer the episode target:
   - Default: first-person Japanese, male protagonist, light humorous inner monologue, RPG fantasy vocabulary, 8k-20k Japanese characters.
   - If the user gives "每集1.5万字", target around 15,000 Japanese characters including punctuation and line breaks.
2. Build a short beat plan before prose:
   - Hook within first 300-500 Japanese characters.
   - Daily-life pressure or social unfairness.
   - Cheat discovery or new application.
   - Small experiment with concrete item/monster/tool.
   - Public proof, comic reaction, or zamaa beat.
   - New practical reward that supports slow-life/base-building.
   - Next-episode trouble hook.
3. Write in Japanese prose:
   - Prefer `俺` first-person unless the user asks otherwise.
   - Use short inner-commentary beats for humor.
   - Keep paragraphs readable for web serialization.
   - Do not insert Chinese names, cultivation terms, sect terms, or Chinese monster taxonomy.
4. Save long outputs to a file when the result would be too large for chat. Report the absolute path and character count.
5. Validate:
   - Count Japanese characters with Python.
   - Scan for banned Chinese leakage using `references/terminology.md`.
   - If below target by more than 10%, expand existing dense beats rather than adding random scenes.

## Quality Bar

The episode must feel like Japanese isekai, not translated Chinese xianxia. The reader should immediately understand the social system, the cheat's rule, why the protagonist wants safety/profit/slow life, and what problem pulls him into the next installment.
