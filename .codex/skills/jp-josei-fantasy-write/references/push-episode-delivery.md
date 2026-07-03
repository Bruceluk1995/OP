# Push Episode Delivery

Use this when the user wants Japanese female-audience fantasy romance as anime-style 推文 / recap-like episodes, especially with per-episode files, character prompts, or YouTube covers.

## Language Contract

- Use the user's language for coordination, questions, and status updates.
- Write audience-facing prose, episode titles, thumbnail text, and character-name labels in Japanese unless the user says otherwise.
- If the user says "跟我对话用中文，推文用日语", keep all chat/meta in Chinese and all deliverables intended for viewers in Japanese.

## Episode Shape

- Treat each episode as a first-person viewing/narration experience, not a standard chapter summary.
- Default viewpoint for 推文 episodes: `私`, close to the heroine's fear, calculation, shame, relief, and attraction.
- Open with a 1-2 sentence hook that lets a new viewer understand the immediate danger or humiliation.
- Keep the episode moving through scenes: pressure -> heroine choice -> male lead action -> social consequence -> emotional aftertaste -> next hook.
- If the user sets a target such as 2万字 per episode, preserve that as the active project target until changed.
- Do not pad with generic adjectives, repeated sighing, decorative scenery, or abstract declarations. Use documents, doors, witnesses, names, hands, contracts, etiquette, injuries, rumors, and concrete gestures.

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

At the end, report the saved folder and important files. If an image was generated, show the actual `cover.png` inline when the environment supports local image rendering.
