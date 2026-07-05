# Dynamic Benchmarking Protocol

Use this before planning a Japanese female-audience fantasy romance subtype when the user wants market fit, current popular works, website-based book analysis, or when no strong project benchmark exists.

## Priority

1. Project benchmark report: `对标/{lane}/{work}/拆文报告.md` or `拆文库/{work}/`.
2. Fresh public ranking/tag metadata from sites such as Syosetu and Kakuyomu.
3. Project subtype notes: `女频幻想恋爱知识库/type-packs/{lane}.md`.
4. Bundled type pack: `references/type-packs/{lane}.md`.

Bundled type packs are fallback scaffolds. They must not override a fresh benchmark, a project-owned拆文 report, or project-local subtype notes.

## Candidate Scan

When browsing is allowed or requested:

- Search the matching platform/category/tag page for the selected lane.
- Collect 3-5 candidates with title, URL, ranking context, visible tags, update date if shown, public synopsis/premise, and why it matches the lane.
- Select one primary benchmark and one or two contrast benchmarks.
- Prefer currently visible ranking/tag pages over older memory.
- Use metadata, titles, tags, ranking context, and short public premise signals only. Do not copy prose, scene order, dialogue, or proprietary outlines.

## Benchmark Card

Create a compact benchmark card before making the story plan:

```text
## Dynamic Benchmark Card

- Captured at:
- Lane:
- Source pages:
- Primary benchmark:
- Contrast benchmarks:
- Visible tags:
- Public premise promise:
- Heroine wound:
- Romance engine:
- Evidence / zamaa engine:
- Social venue:
- Male-lead recognition mode:
- Episode or arc rhythm inferred from public metadata:
- Differentiation rule for our project:
- Forbidden copying:
```

## If Full Text Is Available

Only do chapter-level拆书 when the user provides the text, a project-owned拆文 report already exists, or the source is legitimately accessible for this use. Even then:

- Extract functions, not sentences.
- Summarize plot roles at a high level.
- Do not copy scene order directly into the new plan.
- Replace heroine role, wound, male lead, pressure source, proof object, venue, social consequence, and ending aftertaste.

## Save Back

For project-bound work, save reusable findings to:

- `对标/{lane}/_live-benchmark-{YYYYMMDD}.md` for source-specific cards.
- `女频幻想恋爱知识库/type-packs/{lane}.md` for distilled project-local lane notes.

Then record the generated plan in `女频幻想恋爱知识库/generated-ledger.jsonl` so later stories avoid repeating the same wound-romance-reversal engine.

## Anti-Copy Rule

Every plan derived from a benchmark must state what is changed:

- heroine role
- opening wound
- male-lead role and recognition mode
- pressure source
- proof object
- reversal venue
- social consequence
- ending aftertaste

If at least three of these remain too close to the benchmark, revise before producing the outline.
