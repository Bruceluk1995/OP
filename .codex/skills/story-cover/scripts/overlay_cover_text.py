#!/usr/bin/env python3
"""Deterministically overlay CJK-safe title text on cover or thumbnail art."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


ZH_FONT_CANDIDATES = (
    "C:/Windows/Fonts/msyhbd.ttc",
    "/System/Library/Fonts/PingFang.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",
    "/usr/share/fonts/truetype/noto/NotoSansCJK-Bold.ttc",
)

JA_FONT_CANDIDATES = (
    "C:/Windows/Fonts/meiryob.ttc",
    "C:/Windows/Fonts/YuGothB.ttc",
    "/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",
    "/usr/share/fonts/truetype/noto/NotoSansCJK-Bold.ttc",
)


def find_font(explicit: str | None, text: str) -> Path:
    has_japanese_kana = bool(re.search(r"[\u3040-\u30ff]", text))
    preferred = JA_FONT_CANDIDATES if has_japanese_kana else ZH_FONT_CANDIDATES
    fallback = ZH_FONT_CANDIDATES if has_japanese_kana else JA_FONT_CANDIDATES
    candidates = ([explicit] if explicit else []) + list(preferred) + list(fallback)
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return Path(candidate)
    raise SystemExit("No CJK font found. Pass --font with a .ttf/.ttc font path.")


def text_width(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, stroke: int) -> int:
    box = draw.textbbox((0, 0), text, font=font, stroke_width=stroke)
    return box[2] - box[0]


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, max_width: int, stroke: int) -> list[str]:
    explicit_lines = text.replace("\\n", "\n").splitlines() or [text]
    lines: list[str] = []
    for source in explicit_lines:
        current = ""
        for char in source:
            candidate = current + char
            if current and text_width(draw, candidate, font, stroke) > max_width:
                lines.append(current)
                current = char
            else:
                current = candidate
        if current or not source:
            lines.append(current)
    return lines


def fit_title(
    draw: ImageDraw.ImageDraw,
    text: str,
    font_path: Path,
    max_width: int,
    max_lines: int,
    max_size: int,
    min_size: int,
    stroke: int,
) -> tuple[ImageFont.FreeTypeFont, list[str]]:
    for size in range(max_size, min_size - 1, -2):
        font = ImageFont.truetype(str(font_path), size=size)
        lines = wrap_text(draw, text, font, max_width, stroke)
        if len(lines) <= max_lines:
            return font, lines
    raise SystemExit(f"Title is too long for {max_lines} lines. Add an explicit line break or shorten it.")


def add_vertical_gradient(image: Image.Image, top: bool, opacity: int) -> None:
    width, height = image.size
    band = int(height * 0.42)
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    pixels = overlay.load()
    for y in range(band):
        alpha = int(opacity * (1 - y / max(1, band - 1)))
        target_y = y if top else height - 1 - y
        for x in range(width):
            pixels[x, target_y] = (0, 0, 0, alpha)
    image.alpha_composite(overlay)


def draw_centered_lines(
    draw: ImageDraw.ImageDraw,
    lines: list[str],
    font: ImageFont.FreeTypeFont,
    center_x: int,
    start_y: int,
    fill: str,
    stroke: int,
    spacing: int,
) -> int:
    y = start_y
    for line in lines:
        box = draw.textbbox((0, 0), line, font=font, stroke_width=stroke)
        width, height = box[2] - box[0], box[3] - box[1]
        draw.text(
            (center_x - width / 2, y),
            line,
            font=font,
            fill=fill,
            stroke_width=stroke,
            stroke_fill="#111111",
        )
        y += height + spacing
    return y


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--mode", choices=("vertical", "youtube"), default="vertical")
    parser.add_argument("--title", default="")
    parser.add_argument("--subtitle", default="")
    parser.add_argument("--author", default="")
    parser.add_argument("--author-prefix", default="", help="Defaults to 著： for Japanese and 作者： otherwise")
    parser.add_argument("--text-json", type=Path, help="UTF-8 JSON with title/subtitle/author; safest for Windows PowerShell 5.1")
    parser.add_argument("--font")
    parser.add_argument("--title-color", default="#FFFFFF")
    parser.add_argument("--accent-color", default="#FFD54A")
    args = parser.parse_args()

    if not args.input.is_file():
        raise SystemExit(f"Input image not found: {args.input}")
    if args.text_json:
        data = json.loads(args.text_json.read_text(encoding="utf-8"))
        args.title = args.title or str(data.get("title", ""))
        args.subtitle = args.subtitle or str(data.get("subtitle", ""))
        args.author = args.author or str(data.get("author", ""))
    if not args.title:
        raise SystemExit("A title is required. Pass --title or --text-json.")
    font_path = find_font(args.font, f"{args.title}{args.subtitle}{args.author}")
    size = (1200, 1600) if args.mode == "vertical" else (1280, 720)
    source = Image.open(args.input).convert("RGB")
    canvas = ImageOps.fit(source, size, method=Image.Resampling.LANCZOS).convert("RGBA")
    add_vertical_gradient(canvas, top=True, opacity=190 if args.mode == "vertical" else 175)
    if args.author or args.subtitle:
        add_vertical_gradient(canvas, top=False, opacity=150)
    draw = ImageDraw.Draw(canvas)
    width, height = size
    margin = int(width * 0.08)
    stroke = max(3, width // 320)
    max_lines = 3 if args.mode == "vertical" else 2
    max_size = int(width * (0.13 if args.mode == "vertical" else 0.10))
    min_size = int(width * 0.045)
    font, lines = fit_title(draw, args.title, font_path, width - 2 * margin, max_lines, max_size, min_size, stroke)
    title_bottom = draw_centered_lines(
        draw,
        lines,
        font,
        width // 2,
        int(height * 0.065),
        args.title_color,
        stroke,
        max(8, font.size // 7),
    )

    small_font = ImageFont.truetype(str(font_path), size=max(28, int(width * 0.035)))
    if args.subtitle:
        subtitle_y = min(int(height * 0.78), title_bottom + int(height * 0.025))
        draw_centered_lines(draw, [args.subtitle], small_font, width // 2, subtitle_y, args.accent_color, max(2, stroke - 1), 6)
    if args.author:
        is_japanese = bool(re.search(r"[\u3040-\u30ff]", f"{args.title}{args.author}"))
        prefix = args.author_prefix or ("著：" if is_japanese else "作者：")
        author = f"{prefix}{args.author}"
        box = draw.textbbox((0, 0), author, font=small_font, stroke_width=2)
        draw.text(
            ((width - (box[2] - box[0])) / 2, height - margin - (box[3] - box[1])),
            author,
            font=small_font,
            fill="#FFFFFF",
            stroke_width=2,
            stroke_fill="#111111",
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    canvas.convert("RGB").save(args.output, quality=95)
    print(json.dumps({"output": str(args.output), "size": size, "font": str(font_path), "title_lines": lines}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
