# Dynamic Benchmarking Protocol

Use this before planning a Japanese male-audience isekai subtype when the user wants market fit, current popular works, website-based book analysis, or when no strong project benchmark exists.

## Priority

1. Project benchmark report: `对标/{lane}/{work}/拆文报告.md` or `拆文库/{work}/`.
2. Fresh public ranking/tag metadata from sites such as Kakuyomu and 小説家になろう.
3. Project subtype notes: `男频异世界知识库/type-packs/{lane}.md`.
4. Bundled type pack: `references/type-packs/{lane}.md`.

Bundled type packs are fallback scaffolds. They must not override a fresh benchmark or project拆文 report.

## Optional Cross-Market Inspiration

When the user requests Chinese novel sites or selects that source in the male-isekai topic gate, read `../../jp-isekai/references/chinese-novel-inspiration.md` and create a separate Chinese-market function card. Keep the Japanese source as the market-fit authority. Chinese rankings can suggest transferable cheats, pressure engines, progression rewards, and faction structures, but cannot prove Japanese demand.

## Candidate Scan

When browsing is allowed or requested:

- Search the matching platform/category/tag page for the selected lane.
- Collect 3-5 candidates with title, URL, ranking context, visible tags, update date if shown, public synopsis/premise, and why it matches the lane.
- Select one primary benchmark and one or two contrast benchmarks.
- Prefer currently visible ranking/tag pages over old memory.
- If a Chinese-site scan is included, keep those candidates in a labeled cross-market section and record whether the chosen mechanism has a current Japanese ranking/tag/reader-interest cross-check.

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
- Reader expectation:
- Payoff engine:
- Opening pressure pattern:
- Progression/reward pattern:
- Episode or arc rhythm inferred from public metadata:
- Differentiation rule for our project:
- Forbidden copying:
- Cross-market inspiration, if any:
- Japan cross-check status:
```

For public web pages, use only metadata, tags, titles, rankings, and short public synopsis-level information. Do not reproduce or paraphrase large amounts of prose.

## If Full Text Is Available

Only do chapter-level拆书 when the user provides the text, a project-owned拆文 report already exists, or the source is legitimately accessible for this use. Even then:

- Extract functions, not sentences.
- Summarize plot roles at a high level.
- Do not copy scene order directly into the new plan.
- Replace protagonist, cheat, faction, venue, pressure source, reward, and aftertaste.

## Save Back

For project-bound work, save reusable findings to:

- `对标/{lane}/_live-benchmark-{YYYYMMDD}.md` for source-specific cards.
- `男频异世界知识库/type-packs/{lane}.md` for distilled project-local lane notes.

Then record the generated plan in `男频异世界知识库/generated-ledger.jsonl` so later stories avoid repeating the same engine.

## Anti-Copy Rule

Every plan derived from a benchmark must state what is changed:

- protagonist role
- cheat/power engine
- pressure source
- venue
- reward/progression token
- faction relationship
- ending aftertaste

If at least three of these remain too close to the benchmark, revise before producing the outline.
