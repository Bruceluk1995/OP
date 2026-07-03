# YouTube Thumbnail Covers

Use this reference when the user asks for a YouTube, oil-pipe/油管, long-video, 16:9, or high-click thumbnail cover. Treat it as a video thumbnail, not a normal vertical novel cover.

## Required Output

- Generate an actual image file, not only a prompt.
- Use landscape 16:9. Prefer 1920x1080 or 3840x2160 when controllable; accept the image tool's native 16:9 output if dimensions differ slightly.
- Include the work/series title in the image unless the user explicitly says not to.
- Include one main click title from the episode/video title. Split it into 2-3 short readable blocks if the full title is too long.
- Keep all text inside safe margins and readable on mobile.

## Thumbnail Logic

Use high-CTR YouTube composition:

- One large expressive face or beautiful main character face.
- One obvious conflict object or pressure source, such as a contract, pursuer, monster, curse mark, betrayal letter, debt notice, or magical item.
- Few elements. Avoid crowded group portraits, tiny background details, and ordinary light-novel cover layouts.
- Strong contrast, cinematic rim light, clear foreground/background separation.
- Title hierarchy should be bold and legible: red/white/gold text, thick dark outline, glow, or ornate ribbon.
- Match the scene and episode honestly. Do not clickbait a scene that does not exist.

For Japanese fantasy/story narration thumbnails, prefer premium anime fantasy illustration: polished faces, dramatic blue-purple shadows, warm gold highlights, ornate title frame/ribbon, and large readable Japanese lettering. Avoid cheap sticker text, ugly faces, low-contrast brown rooms, clutter, modern leakage, watermark, logo, and gibberish text.

## Prompt Skeleton

```text
Create a premium 16:9 YouTube long-form thumbnail for a story narration video. It must look like a high-performing Japanese fantasy/anime YouTube thumbnail: beautiful anime faces, dramatic lighting, ornate title design, strong contrast, clickable composition.

The image MUST include BOTH text layers below, with no other text, no logo, no watermark, no gibberish:

Main large click title text:
"<click title line 1>"
"<click title line 2>"

Series/work title in a smaller bottom banner:
"<full work or series title>"

Text layout: main title large on the right or upper-right in red/white/gold fantasy lettering with thick dark outline and glow. Series title in a dark ornate bottom ribbon/bar, smaller but readable. Keep all text inside safe margins.

Visual concept: <one expressive protagonist>, <one pressure/conflict source>, <one conflict object>, and at most 1-2 companion elements. High-end anime/fantasy illustration, cinematic depth, strong rim light, clean silhouettes, no clutter.

Avoid: ugly faces, cheap sticker text, text mistakes, extra text, random symbols, small unreadable typography, cluttered group portrait, Chinese xianxia, cultivation, flying swords, modern office, modern business suit, oversexualized clothing, horror, gore, watermark, logo.
```

## Validation

- Confirm the saved image exists and opens.
- Confirm dimensions are 16:9 or close enough to 16:9.
- Confirm both the click title and the work/series title are present in the image.
- If replacing a bad version, keep the old image with a descriptive suffix instead of overwriting without trace.
