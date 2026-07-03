# Episode Delivery

Use this reference when an episode should be delivered as project files, especially for long-form Japanese isekai YouTube narration workflows.

## Folder Contract

Create one folder per episode:

`episodes/第XXX話_<short-title>/`

Include:

- `正文.md`: Japanese episode prose.
- `标题.md`: full title, chapter title, and Chinese working title if useful.
- `角色提示词.md`: visual prompts for all characters appearing in the episode.
- `封面.md`: cover brief, final prompt, dimensions, generated-file notes, and old-version notes.
- `封面.png`: actual generated thumbnail image.

If the project already has flat episode files, also sync `episodes/episode_XXX_ja.md` for compatibility. Do not treat a prompt-only `封面.md` as a completed cover.

## YouTube Cover Defaults

Default `封面.png` is a YouTube long-form thumbnail:

- Landscape 16:9. Prefer 3840x2160 or 1920x1080 when controllable; accept model-native 16:9 such as 1672x941 if that is what the image tool returns.
- Directly generate the image with title text in the image. Do not switch to local text overlay unless the user asks.
- Include two text layers:
  - Main click title: the episode title or a 2-3 block high-click split from it.
  - Series/work title: the full work title in a bottom ribbon, corner label, or other stable branding area.
- Keep text readable on mobile. Avoid cramming a full long sentence when a shorter title split is clearer.
- Save replacements non-destructively: keep old versions as `封面_旧版_<reason>.png` or similar.

## High-CTR Thumbnail Heuristics

Use YouTube-thumbnail logic, not ordinary light-novel cover logic:

- One strong emotion face or beautiful protagonist face.
- One obvious conflict object: contract, pursuer, curse mark, monster, betrayal letter, etc.
- Few elements. Avoid crowded group portraits and tiny background details.
- Strong contrast, rim light, red/white/gold or other clear text hierarchy.
- Clear action or emotion for new viewers; familiar recurring characters for subscribers.
- Rule-of-thirds composition when possible.
- The thumbnail and title must accurately reflect the episode. Do not bait a scene that is not in the episode.

For Japanese fantasy narration thumbnails, use premium anime fantasy styling: polished faces, dramatic blue-purple shadows plus warm gold highlights, ornate title frame/ribbon, and large readable Japanese lettering. Avoid cheap sticker text, ugly faces, clutter, and low-contrast brown room scenes.

## Prompt Skeleton

Use or adapt this skeleton for Image2/direct generation:

```text
Create a premium 16:9 YouTube long-form thumbnail for a Japanese male-audience RPG isekai story video. It must look like a high-performing Japanese fantasy YouTube thumbnail: beautiful anime faces, dramatic lighting, ornate title design, strong contrast, clickable composition.

The image MUST include BOTH text layers below, in Japanese, with no other text, no logo, no watermark, no gibberish:

Main large click title text:
「<episode click title line 1>」
「<episode click title line 2>」

Series/work title in a smaller bottom banner:
『<series title>』

Text layout: main title large on the right or upper-right in red/white/gold fantasy lettering with thick dark outline and glow. Series title in a dark ornate bottom ribbon/bar, smaller but readable. Keep all text inside safe margins.

Visual concept: <one emotional protagonist>, <one pressure/conflict source>, <one conflict object>, and at most 1-2 mascot/companion elements. High-end Japanese fantasy anime illustration, cinematic depth, strong rim light, clean silhouettes, no clutter.

Avoid: ugly faces, cheap sticker text, text mistakes, extra text, random symbols, small unreadable typography, cluttered group portrait, Chinese xianxia, cultivation, flying swords, modern office, modern business suit, oversexualized clothing, horror, gore, watermark, logo.
```

## Tracking

After packaging, update `追踪/上下文.md` if it exists:

- last completed episode/chapter
- delivery folder path
- cover status and any notable caveats
- next episode outline status
