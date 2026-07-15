# One-Shot Delivery Package

Use this reference whenever a full standalone male-audience isekai one-shot is saved to disk.

## Folder Contract

Create one package folder per one-shot:

`episodes/oneshots/<short-ascii-slug-or-short-title>/`

Include:

- `正文/正文.md`: Japanese audience-facing prose only. Do not mix blueprint, ledger notes, cover prompts, or character prompts into this file.
- `正文/标题.md`: Chinese working title, Japanese publish title, short click title, and optional title variants.
- `角色提示词/角色提示词.md`: visual prompts for all major characters appearing in the story.
- `封面/封面.md`: YouTube thumbnail or novel-cover brief, final image prompt, text layers, dimensions, and production status.
- `作品资料.md`: one-shot blueprint, source/seed notes, character count, checks, ledger fields, and package status.
- `开头抽卡证据.json`: selected card ID plus one exact opening quote for every required chain slot, every card-specific `surface_beat`, and the visual story core (`ordinary_action_or_loss`, `visible_change`, `human_consequence`); must pass `validate-opening-evidence.py`.
- `封面/封面.png`: actual generated cover/thumbnail image when image generation is requested or available.

Do not deliver only a mixed markdown file containing title, blueprint, body, cover notes, and ledger notes together.

## Body File

`正文/正文.md` is the file used for character counting and Codex AI story/prose self-check.

- It may include the Japanese publish title at the top.
- It must not include Chinese planning notes.
- It must not include artificial body boundary markers.
- Count this file after any prose cleanup.
- Reread this file directly for the Codex AI self-check. Do not judge body quality from `作品资料.md` alone.
- Check that Chinese source culture has been rebuilt for Japanese RPG isekai readers. Do not leave literal xianxia, sect, wuxia, or palace-drama mechanisms when the target setting is Japanese-style RPG/light-novel fantasy.

## Character Prompt File

Write `角色提示词/角色提示词.md` as direct, single-paragraph visual prompts, not field-by-field sheets.

Include the protagonist, major companions, major antagonist, and any story-relevant creature or boss that needs visual continuity. Keep one heading per character, then one complete paragraph that can be pasted into an image/character generation tool.

Default order inside each paragraph: age and role/species; height and body type; hair color, hairstyle, and texture; eye color, facial features, expression, and temperament; clothing, accessories, stable weapon/tool, emblem, and wear/cleanliness.

Character prompts are stable visual identity only. Do not add cover composition, camera framing, scene action, one-off plot movement, or lines such as `适合封面姿态：`, `本集重点姿态：`, `封面构图：`, or `画面中：`. Put those instructions only in `封面/封面.md`.

## Cover File

`封面/封面.md` is required even when no image is generated yet.

For male isekai one-shots, default to a 16:9 YouTube long-form thumbnail unless the user asks for a vertical novel cover:

- Use Japanese text inside the cover prompt.
- Use a short click title, not the full long title if it becomes unreadable.
- Include one strong protagonist or party face cluster, one clear conflict object, and one visible fantasy pressure source.
- Avoid crowded full-party posters; if companions matter, show 2-3 faces or silhouettes and make the protagonist/central conflict dominant.
- Keep no creator, no real-person, no copied clip scene, no copyrighted IP.

Prompt skeleton:

```text
Create a premium 16:9 YouTube long-form thumbnail for a Japanese male-audience RPG isekai one-shot. It must look like a high-performing Japanese fantasy YouTube thumbnail: polished anime fantasy faces, dramatic lighting, strong contrast, readable Japanese title design, clickable composition.

The image MUST include BOTH text layers below, in Japanese, with no other text, no logo, no watermark, no gibberish:

Main large click title text:
「<click title line 1>」
「<click title line 2>」

Smaller bottom banner or corner label:
『<work title>』

Visual concept: <protagonist>, <companions or antagonist>, <one conflict object>, <one fantasy pressure source>. High-end Japanese fantasy anime illustration, cinematic depth, strong rim light, clean silhouettes, no clutter.

Avoid: ugly faces, cheap sticker text, text mistakes, extra text, tiny unreadable typography, cluttered group portrait, Chinese xianxia, cultivation, flying swords, modern office, watermark, logo.
```

If `封面.png` is not generated, mark the status clearly as `prompt-only / image not generated yet`. Do not claim a finished cover image exists.

## Handoff

Final handoff should report the package folder and the three primary files:

- `正文/正文.md`
- `角色提示词/角色提示词.md`
- `封面/封面.md`

If `封面.png` exists, also report and display it when possible.

Also report the Codex AI self-check result in plain language: body-only Japanese prose, one-shot closure, localization, package completeness, and any rewrite applied.
