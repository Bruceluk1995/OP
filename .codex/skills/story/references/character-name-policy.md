
# Global Character Name Policy

Use this before finalizing names in any fiction skill. The project-wide ledger is:

```text
角色名历史/character-name-history.jsonl
```

## Mandatory Deduplication

1. Import existing names before naming a new cast.
2. Check every final named character against the ledger.
3. Reuse is allowed only when continuing the same work, or when the user explicitly requests reuse.
4. A different surname, title, spelling separator, or hiragana/katakana form does not make a reused fantasy given name new.
5. After the cast is selected or saved, record every actually used name. Unselected brainstorming names are not burned.

```powershell
python "$HOME/.codex/skills/story/scripts/character_names.py" --root . import-existing
python "$HOME/.codex/skills/story/scripts/character_names.py" --root . summary
python "$HOME/.codex/skills/story/scripts/character_names.py" --root . check --work "{work}" --name "{name}" --style jp-female-fantasy
python "$HOME/.codex/skills/story/scripts/character_names.py" --root . add --domain "{domain}" --work "{work}" --role "{role}" --name "{name}" --source "{source}"
```

The script blocks an exact reused full name or reused fantasy given name from another work. It warns on near-duplicates. Do not bypass a block by changing only `・`, spacing, kana form, or the family name.

## Japanese Isekai Naming Model

Official anime character pages commonly foreground short call names: `カズマ`, `アクア`, `めぐみん`, `ダクネス`, `レム`, `ラム`, `エミリア`, `ベアトリス`, `リムル`, `シュナ`, `シオン`, `ミリム`, `ラフタリア`, and `フィーロ`. Follow the functional pattern, never copy a protected cast as a set.

- Earth-origin Japanese characters: use a natural Japanese full name in formal records, then surname or given name consistently in narration.
- Local fantasy characters: prefer one short given name as the everyday display name.
- Give noble houses a separate short house name only when rank, inheritance, a contract, or a hearing needs it.
- Do not lengthen names to signal nobility. Use `公爵令嬢`, `辺境伯家`, a title, crest, or territory instead.
- Keep the main cast aurally distinct. Avoid names that share both the same opening sound and ending, such as `レナ／レイナ／レリア` in one work.
- Do not default repeatedly to model-favorite names such as `ミーナ`, `レイナ`, `セレス`, `リリア`, or `アリシア`; the ledger decides whether a name remains available.

## Female-Fantasy Length Gate

For Japanese female-audience fantasy and important women in male-isekai:

- Preferred everyday name: 2-6 Japanese characters, usually one katakana/hiragana segment.
- Maximum given-name length: 6 characters.
- Maximum two-part fantasy full name: 10 characters excluding `・` and spaces.
- Maximum segments: 2. Do not use three-part aristocratic names by default.
- A legal/formal full name may appear once when plot-relevant; narration and dialogue must return to the short given name.
- Character-prompt headings, cast lists, outline labels, and routine scene references must use the everyday short name, not the legal full name.
- Apply the same short-display-name rule to male leads and supporting cast; rank and house identity belong in the prompt body or story context, not in every name label.
- Reject names like `リーゼロッテ・ハルベルク` as a default display name. Shorten the call name and, if necessary, use a compact house name such as `リゼ・ベルク`.

Use `--style jp-female-fantasy` for this hard gate. For male fantasy names use `--style jp-male-fantasy`; for modern Japanese names use `--style jp-modern`.

## Cast-Level Readability

- Before drafting, read the final names aloud mentally as a list.
- Do not give more than two core characters the same first kana, final kana, or similar rhythm.
- Prefer role contrast over decorative spelling.
- Keep names stable after selection; do not switch between full name, nickname, and title without establishing the relationship.
