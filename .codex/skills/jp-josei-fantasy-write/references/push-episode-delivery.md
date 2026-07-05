# Push Episode Delivery

Use this when the user wants Japanese female-audience fantasy romance as anime-style 推文 / recap-like episodes, especially with per-episode files, character prompts, or YouTube covers.

This reference governs push-format delivery, opening retention, folders, covers, and handoff. Use it together with `episode-blueprint.md`, which governs the whole episode's emotion target, dense/sparse beats, payoff, cost, and ending hook, and `anti-ai-gates.md`, which governs final prose cleanup and script-based checks.

For finished/full episode, YouTube/朗读/推文 narration, or 6-episode short-season prose, the default body target is 14,500-16,500 Japanese characters unless the user sets another length. Count the saved body before handoff and keep expanding dense evidence/romance/zamaa beats if it is below 14,500.

## Language Contract

- Use the user's language for coordination, questions, and status updates.
- Write audience-facing prose, episode titles, thumbnail text, and character-name labels in Japanese unless the user says otherwise.
- If the user says "跟我对话用中文，推文用日语", keep all chat/meta in Chinese and all deliverables intended for viewers in Japanese.

## Episode Shape

- Treat each episode as a first-person viewing/narration experience, not a standard chapter summary.
- Default viewpoint for 推文 episodes: `私`, close to the heroine's fear, calculation, shame, relief, and attraction.
- Open with the whole episode's biggest social/emotional bomb in sentence one. Use accusation, annulment, witness testimony, betrayal, contract reveal, curse symptom, public choice, debt, trial, inheritance theft, or male-lead intervention. Do not open with scenery, weather, abstract mood, or a soft "I never imagined..." line unless the same sentence contains the concrete bomb.
- Immediately after sentence one, give a previous-episode bridge in prose: what happened last episode, what evidence/object/person remains unresolved, and why the heroine must act now. New viewers should understand the last hook by line five.
- Keep the episode moving through scenes: pressure -> heroine choice -> male lead action -> social consequence -> emotional aftertaste -> next hook.
- Build the full `episode-blueprint.md` before prose so the episode has a clear position, dense/sparse beat budget, concrete payoff, cost, and ending hook.
- If the user sets a target such as 2万字 per episode, preserve that as the active project target until changed.
- Do not pad with generic adjectives, repeated sighing, decorative scenery, or abstract declarations. Use documents, doors, witnesses, names, hands, contracts, etiquette, injuries, rumors, and concrete gestures.
- Before handoff, run the `anti-ai-gates.md` final self-check. If the prose is saved to a file, run the local anti-AI scripts and fix blocking findings.

## Mandatory Opening Order

For episode 2 or later, write the first 250-500 Japanese characters in this order:

1. **Plot-bomb first sentence.** Put the full pressure in sentence one: public accusation, broken engagement, false saint claim, cursed prince collapse, contract term, family betrayal, or witness reveal.
2. **Previous-episode bridge.** In 1-3 sentences, name what happened last episode and what remains unresolved. Use names, documents, witnesses, titles, injuries, contracts, rumors, or exact promises.
3. **Now-problem.** Name the immediate social or emotional obstacle forcing the current scene.
4. **Heroine reaction.** Give one close first-person reaction tied to a concrete body action or decision, not vague sadness.
5. **Scene entry.** Move into dialogue, a document, a door opening, a witness stepping forward, or the male lead taking action.

Do not label these parts as "recap" or "summary" in the prose unless the user explicitly asks for script labels.

## Anti-AI Push Prose

Ban or heavily restrict:

- abstract theme sentences
- generic emotional adjectives without action
- repeated sighs, trembling, tears, warmth, light, silence, destiny
- "as if the world..." metaphors
- paragraphs that only tell the reader the heroine is hurt, brave, beautiful, loved, or reborn
- recap that says "many things happened" instead of naming the actual incident

Prefer:

- documents, seals, witness names, etiquette mistakes, seating order, titles, contracts, rumor source, injuries, debt, doors, gloves, letters, family ledgers, church records
- dialogue that changes social status
- heroine choices that cost something
- male-lead recognition shown through a specific action, not generic praise
- cause-effect bridges: because X happened last episode, Y is dangerous now, so the heroine chooses Z

## Beat Density

Every 800-1200 Japanese characters should contain at least one of:

- new evidence
- public pressure
- heroine choice
- male-lead action with social cost
- zamaa setup or payoff
- romantic recognition through behavior
- legal/family/church/court consequence
- next-hook escalation

## Title Format

Use a romance-forward Japanese episode title. A good default format is:

```text
♡ 第N話 ♡「本集の強い出来事・感情フック」『シリーズタイトル 〜サブタイトル〜』
```

For thumbnails, do not force the entire long title into the image. Use the episode title's core conflict as large readable text.

## Per-Episode Folder

When the user asks for each episode as its own package, create one folder per episode. Prefer stable ASCII filenames unless the project already uses another convention:

- `body_ja.md`: complete Japanese episode正文 only.
- `title.md`: full episode title/title card.
- `character_prompts.md`: characters appearing in this episode and image-generation prompts.
- `cover.png`: final actual cover image.
- `cover_prompt.md`: prompt and production notes for reproducibility.

If a previous local convention uses `正文.md`, `标题.md`, `角色提示词.md`, and `封面.png`, follow that convention instead of renaming the project.

## Character Prompts

- Reuse existing character prompts when the same characters return.
- Keep concrete visual continuity: age range, hair, eyes, height, clothing, social role, expression, and episode-specific state.
- Add only the characters needed for the current episode. Do not invent extra cast for convenience.
- If the user shows prior character cards/screenshots, infer missing prompts from the visible names and previous episode context, then state uncertainty briefly.

## YouTube Cover Rules

The cover means an actual image file, not only a prompt.

- Use 16:9 horizontal composition for YouTube long videos. Prefer 1280x720 when doing local post-processing.
- Directly generate the thumbnail with Japanese title text inside the image, following the `jp-isekai-write` episode-cover workflow. Do not use a no-text background plus local text overlay unless the user explicitly asks for it or a generated text layer is unusable and the user approves repair.
- Do not force a left black text panel. Use full-image high-CTR composition: big emotional faces, one clear conflict object, readable title blocks, and a smaller series title banner or corner label.
- Design for mobile readability: huge faces, one clear conflict, strong emotion, strong contrast, and short large text.
- Prefer a thumbnail hook over a light-novel poster: close-up heroine + male lead + visible threat beats full-body beauty shots.
- Keep the cover copy to the episode title's core conflict. Avoid cramming the full series title if it becomes tiny.
- Regenerate the background if it looks like a pretty book cover but would not get clicks as a YouTube thumbnail.
- Back up existing covers before overwriting unless the user explicitly wants replacement.

Direct Image2 prompt pattern:

```text
Create a premium 16:9 YouTube long-form thumbnail for a Japanese female-audience fantasy romance story video. It must look like a high-performing Japanese anime fantasy thumbnail: beautiful emotional faces, romantic suspense, dramatic lighting, ornate readable Japanese title design, strong contrast, clickable composition.

The image MUST include BOTH text layers below, in Japanese, with no other text, no logo, no watermark, no gibberish:

Main large click title text:
「<click title line 1>」
「<click title line 2>」

Series/work title in a smaller bottom banner or corner label:
『<series title>』

Visual concept: <heroine emotion>, <male lead presence>, <one conflict object or pressure source>. Keep the composition uncluttered, with text integrated into the art rather than isolated in a blank black panel.

Avoid: text mistakes, extra text, small unreadable typography, cluttered group portrait, light-novel poster layout, Chinese xianxia, modern objects, oversexualized clothing, horror, gore, watermark, logo.
```

## Handoff

After packaging a project-bound episode, update the project memory files described in `../../jp-josei-fantasy/references/project-memory.md`:

- last completed episode/chapter, saved folder, cover/package status, and next outline status in `追踪/上下文.md`
- new/advanced/resolved hooks in `追踪/伏笔.md`
- event order in `追踪/时间线.md`
- heroine, male-lead, antagonist, family, reputation, contract, curse, or romance state changes in `追踪/角色状态.md`
- one generated-history record in `女频幻想恋爱知识库/generated-ledger.jsonl`

At the end, report the saved folder and important files. If an image was generated, show the actual `cover.png` inline when the environment supports local image rendering.
