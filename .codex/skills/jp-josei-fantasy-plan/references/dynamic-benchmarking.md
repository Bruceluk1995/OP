# Dynamic Benchmarking Protocol

Use this before planning a Japanese female-audience fantasy romance subtype when the user wants market fit, current popular works, website-based book analysis, or when no strong project benchmark exists.

For any `hot`, `current ranking`, or live-source claim, record `searched_at_jst` and use only realtime/daily/24-hour ranking snapshots verified inside the rolling 24-hour window. Weekly/monthly/all-time rankings and undated pages may be historical benchmark context only, never current heat evidence.

If the user asks for Google Trends, YouTube, TikTok, viral videos, weird news, 热点选题, or 全源选题, first use `../../jp-josei-fantasy/references/hot-source-router.md` and the matching hot-source reference, then return here only when ranking/tag benchmarking is also needed.

## Priority

1. Project benchmark report: `对标/{lane}/{work}/拆文报告.md` or `拆文库/{work}/`.
2. Fresh public ranking/tag metadata from sites such as Syosetu and Kakuyomu.
3. Project subtype notes: `女频幻想恋爱知识库/type-packs/{lane}.md`.
4. Bundled type pack: `references/type-packs/{lane}.md`.

Bundled type packs are fallback scaffolds. They must not override a fresh benchmark, a project-owned拆文 report, or project-local subtype notes.

## Optional Cross-Market Inspiration

When the user requests Chinese women-oriented novel sites or selects that source in the hot-source menu, read `../../jp-josei-fantasy/references/chinese-novel-inspiration.md` and create a separate Chinese-market function card. Keep Japanese ranking/tag or reader-interest evidence as the market-fit authority. Chinese rankings can suggest heroine wounds, relationship pressure, identity reversals, proof objects, pursuit/redemption engines, and family/marriage functions, but cannot prove Japanese demand.

## Candidate Scan

When browsing is allowed or requested:

- Search the matching platform/category/tag page for the selected lane.
- Collect 3-5 candidates with title, URL, ranking context, visible tags, update date if shown, public synopsis/premise, and why it matches the lane.
- Select one primary benchmark and one or two contrast benchmarks.
- Prefer qualifying 24-hour ranking/tag pages over older memory. If the strict window is thin, report the limitation instead of widening it.
- Use metadata, titles, tags, ranking context, and short public premise signals only. Do not copy prose, scene order, dialogue, or proprietary outlines.
- If a Chinese-site scan is included, keep those candidates in a labeled cross-market section and record whether the selected mechanism has a same-window Japanese ranking/tag/reader-interest cross-check.

## Hot Source Scan

When the request starts from a hot source instead of a novel platform:

- Collect a small batch from the requested source: 5-10 Google Trends JP items, 3-5 YouTube/TikTok hook mechanics, 5-8 weird/social-news seeds, 6-10 Chinese women-oriented novel-site mechanisms, or mixed batches for 全选.
- Score candidates with the matching hot-source reference before choosing one.
- Convert only the underlying female-audience mechanism: public humiliation, reputation repair, contract pressure, family wound, ceremony, social proof, etiquette trap, comfort desire, or relationship recognition.
- After selecting a seed, read `../../jp-josei-fantasy/references/trend-theme-router.md` and map the seed to a josei fantasy route before building the Dynamic Benchmark Card or outline.

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
- Cross-market inspiration, if any:
- Japan cross-check status:
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
