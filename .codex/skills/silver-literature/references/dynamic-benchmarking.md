# Dynamic Benchmarking Protocol

Use this before planning a silver-literature subtype when the user wants current channel/site fit, public website拆书, hot topics, or when no strong project benchmark exists.

## Priority

1. Project benchmark report: `对标/{lane}/{work}/拆文报告.md` or `拆文库/{work}/`.
2. Fresh public metadata from YouTube channels/videos, Kakuyomu tags, Syosetu searches, or other public ranking/tag pages.
3. Project subtype notes: `银发文学知识库/type-packs/{lane}.md`.
4. Bundled type pack: `references/type-packs/{lane}.md`.

Bundled type packs are fallback scaffolds. They must not override fresh public metadata, a project-owned拆文 report, or project-local subtype notes.

## Candidate Scan

When browsing is allowed or requested:

- Search the matching platform/category/tag page for the selected lane.
- Collect 3-5 candidates with title, URL, platform context, visible tags, upload/update date if shown, public synopsis/premise, and why it matches the lane.
- Select one primary benchmark and one or two contrast benchmarks.
- Prefer currently visible channel/video/ranking/tag pages over old memory.
- Use only metadata, titles, tags, ranking context, and short public premise signals. Do not copy prose, narration scripts, scene order, dialogue, or proprietary outlines.

## Benchmark Card

Create a compact benchmark card before making the story plan:

```text
## Dynamic Benchmark Card

- Captured at:
- Lane:
- Source pages:
- Primary benchmark:
- Contrast benchmarks:
- Visible title/tag promises:
- Protagonist age/role:
- Pressure source:
- Proof object:
- Reversal venue:
- Dignity payoff:
- Late-life recovery image:
- Episode or arc rhythm inferred from public metadata:
- Differentiation rule for our project:
- Forbidden copying:
```

## If Full Text Is Available

Only do chapter-level拆书 when the user provides the text, a project-owned拆文 report already exists, or the source is legitimately accessible for this use. Even then:

- Extract functions, not sentences.
- Summarize plot roles at a high level.
- Do not copy scene order directly into the new plan.
- Replace protagonist role/age, pressure source, proof object, antagonist, reversal venue, consequence, and aftertaste.

## Save Back

For project-bound work, save reusable findings to:

- `对标/{lane}/_live-benchmark-{YYYYMMDD}.md` for source-specific cards.
- `银发文学知识库/type-packs/{lane}.md` for distilled project-local lane notes.

Then record the generated plan in `银发文学知识库/generated-ledger.jsonl` so later stories avoid repeating the same engine.

## Anti-Copy Rule

Every plan derived from a benchmark must state what is changed:

- protagonist role and age band
- pressure source
- proof object
- antagonist relation
- reversal venue
- public consequence
- late-life recovery image
- ending aftertaste

If at least three of these remain too close to the benchmark, revise before producing the outline.
