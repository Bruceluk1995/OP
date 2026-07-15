---
name: story-first-person-script
description: First-person short-script creation, audit, and true rewriting across commercial fiction. Use when a draft merely swaps pronouns, breaks the narrator's knowledge boundary, sounds like a diary, over-explains emotion, lacks a distinctive narrator mouth, or falsely claims appended old text is rewritten. Japanese male/female genre promises remain owned by the matching jp-* skill.
metadata: {"openclaw":{"source":"https://github.com/worldwonderer/oh-story-claudecode"}}
---

# First-Person Short Script

This skill owns viewpoint craft, not genre routing. Use the selected genre skill for market promise and localization, then apply this first-person workflow directly.

## Narrator Engine

Before outlining, lock:

```text
What I know now / cannot know
What I notice first / habitually ignore
How I judge money, danger, love, status, and shame
What I want in the current scene
What I refuse to admit
What choice only I would make
```

First person changes information selection, judgment, misunderstanding, reaction, and sentence flavor. It is not a pronoun replacement and does not require long introspection.

## Native Workflow

1. State the reader's concrete waiting and the protagonist's desire.
2. Build a causal core: ordinary trouble -> narrator's unusual choice -> visible result -> new-kind trouble -> costly climax choice -> changed ending.
3. Outline scenes as `entering state -> my choice/interpretation -> exiting state -> live question`.
4. Draft only what the narrator can observe, infer, remember, misunderstand, or later learn. Let withheld admission create tension; do not hide facts the narrator is actively using.
5. Keep narration and dialogue compatible with one person's social position and priorities. A practical judgment is stronger than a generic joke.
6. Blind-read for the earliest point where the narrator becomes a neutral reporter, diary writer, or author explainer; rewrite the whole affected scene, not only pronouns.

## True Rewrite

Extract user-approved facts and anchors, create a fresh causal/change outline, and draft from it. Run `scripts/verify-rewrite.py --old <old> --new <new>` when files exist. Copying the old body and appending an ending is a blocking failure; script success does not certify story quality.

## Hard Rules

- No hidden thoughts or off-screen facts presented as certainty.
- No three paragraphs explaining an emotion already shown by one specific action or object.
- No repeated proof or procedure used to keep the narrator talking.
- No length, pronoun count, short-line ratio, or rewrite-similarity pass used as a quality verdict.
