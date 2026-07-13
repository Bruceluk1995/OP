---
name: silver-literature
description: "Silver-literature writing, planning, dynamic benchmarking, and review for Japanese senior-life family drama, シニア向け朗読, 熟年離婚, 介護, 遺産相続, 老後資金, 退職金, 年金, 老人ホーム, 終活, late-life romance, remarriage, adult-child betrayal, hidden proof, quiet revenge, scolding comeuppance, and healing second-life stories. Use when the user asks for 银发文学, 熟年文学, 老後, 中高年主人公, Japanese family reversal YouTube narration, or wants to distill/write/review silver-generation web fiction."
metadata: {"openclaw":{"source":"https://github.com/worldwonderer/oh-story-claudecode"}}
---

# Silver Literature

## 数字交互契约

- 凡需用户在有限选项中决定，必须在普通对话中列出数字编号，并以“请只回复数字；可多选时用 +，如 1+3”收尾。
- 禁止用开放式问题代替可枚举选项；禁止依赖 AskUserQuestion、request_user_input 或自由文本选项完成有限选择。
- “自定义 / 其他 / 提供素材”也必须编为数字选项。用户选中后，下一轮只索取一个必要内容（如关键词、书名、路径、链接或正文）；这类实际内容不强行数字化。
- 是非确认统一写成 1. 是 / 2. 否，并要求只回复数字。

Use this skill for Japanese silver-generation family stories: older or middle-aged protagonists, late-life dignity, family exploitation, hidden proof, quiet reversal, and emotional recovery. Keep meta notes in Chinese by default; write audience-facing Japanese prose in Japanese unless the user asks otherwise.

Before premise, hotspot, title, or angle work, read `../story/references/global-topic-history.md`, check the shared project ledger, and register every displayed candidate. Do not reuse topics previously shown by any fiction or explainer skill.

## Required Reads

- Read `references/patterns.md` before planning, drafting, rewriting, reviewing, or making titles.
- Read `references/anti-homogenization.md` before generating any new premise, outline, title batch, or full story.
- Read `references/project-memory.md` before opening a project, continuing a serial, creating saved files, or checking anti-homogenization.
- Read `references/episode-blueprint.md` before drafting any long narration, saved story, or 6-episode season.
- Read `references/dynamic-benchmarking.md` when the user wants current channel/site fit, website-based拆书, hottest works, or when no strong project benchmark exists for the chosen subtype.
- If the user asks for the latest channel trend or provides fresh channels/videos, browse or refresh public metadata first; do not rely only on the bundled snapshot.
- Before planning any subtype, resolve its benchmark priority: project拆文 or live website benchmark first, project subtype notes second, bundled type pack only as fallback.

## Type Pack Routing

- 介護労働 / unpaid care / caregiver discarded -> `references/type-packs/care-labor-reversal.md`
- 熟年離婚 / 定年離婚 / 退職金 / long marriage betrayal -> `references/type-packs/late-life-divorce-retirement-money.md`
- 遺産相続 / house deed / property rights / family money theft -> `references/type-packs/property-inheritance-rights.md`
- 病院 / 診断書 / medical neglect / health proof -> `references/type-packs/hospital-medical-neglect.md`
- 葬式 / 遺言 / 終活 / posthumous truth -> `references/type-packs/funeral-will-posthumous-truth.md`
- Hidden owner / old professional merit / underestimated retired expert -> `references/type-packs/hidden-identity-old-merit.md`
- Adult child betrayal / filial reckoning / grandchild witness -> `references/type-packs/adult-child-filial-reckoning.md`
- 老人ホーム / care facility / dementia / elder housing -> `references/type-packs/nursing-home-facility.md`
- 年金 / bank account / scam / pension fraud -> `references/type-packs/pension-fraud-bank-scam.md`
- Workplace retirement / demotion / founder or shareholder proof -> `references/type-packs/workplace-retirement-reputation.md`
- Late-life romance / remarriage / widowed second life -> `references/type-packs/second-life-romance-remarriage.md`
- Neighborhood / old house / community witness / housing boundary -> `references/type-packs/neighbor-community-housing.md`

## Benchmark Priority

1. If `对标/{lane}/{work}/拆文报告.md` or `拆文库/{work}/` exists, read it before bundled type packs.
2. If the user asks for current/hot/platform-fit or there is no project benchmark, browse relevant public ranking/tag pages, YouTube channel/video metadata, and create a Dynamic Benchmark Card from `references/dynamic-benchmarking.md`.
3. Read any project-local `银发文学知识库/type-packs/{lane}.md`.
4. Read the bundled `references/type-packs/{lane}.md` only as fallback scaffolding.

## Memory Ledger

Before creating a new silver-literature story, check the project ledger:

```powershell
python .codex/skills/silver-literature/scripts/ledger.py --root . summary
```

If the user already gave a candidate premise, check it against the ledger:

```powershell
python .codex/skills/silver-literature/scripts/ledger.py --root . check --lane "care-labor-reversal" --protagonist "67歳の元看護師" --pressure "義母介護の押しつけ" --proof "介護日誌" --venue "家族会議" --aftertaste "一人暮らしの再出発"
```

After generating a premise, outline, title set, or full story, append a compact record:

```powershell
python .codex/skills/silver-literature/scripts/ledger.py --root . add --title "{title}" --lane "{lane}" --protagonist "{protagonist}" --pressure "{pressure}" --proof "{proof}" --venue "{venue}" --aftertaste "{aftertaste}" --path "{output_path}"
```

Use `银发文学知识库/generated-ledger.jsonl` as the default project-local knowledge base. If the file does not exist, create it on first add. Never overwrite old records.

## Core Contract

Write for mature Japanese family-drama viewers, not fantasy progression:

- Center dignity, accumulated grievance, quiet endurance, and late-life recovery.
- Make the protagonist's age matter through social position, care burden, inheritance, work history, adult children, health, housing, pension, documents, long marriage, or retirement.
- Let the reversal come from proof, rights, labor history, social trust, professional identity, property, legal procedure, or a witness; avoid random omnipotent punishment.
- Use family/social spaces as pressure vessels: hospital, care home, funeral hall, family registry office, old house, company reception, airport, bank, lawyer office, dining table, neighborhood association.
- Treat elder abuse, illness, pregnancy, disability, death, dementia, and sexual threat with restraint. Use them as stakes and evidence, not spectacle.
- Extract formulas from reference channels and public tags; do not copy titles, scenes, or long summaries.

## Workflow

1. Classify the request:
   - Market/channel distillation -> summarize public metadata and update the working angle.
   - Concept or outline -> choose a lane, load benchmarks/type packs, design the silver-life premise and outline.
   - Draft or rewrite -> write Japanese prose from an outline and episode blueprint.
   - Review -> check genre fit, lane engine, evidence logic, elder dignity, Japanese naturalness, and AI flavor.
2. If the task only says "银发文学" or "シニア朗读", display a numbered lane menu before planning: `1 介护劳动`、`2 熟年离婚/退休金`、`3 遗产/房产`、`4 医院/医疗忽视`、`5 葬礼/遗嘱`、`6 隐藏身份/退休专家`、`7 成年子女背叛`、`8 养老院`、`9 年金/银行诈骗`、`10 职场退休逆转`、`11 黄昏恋/再婚`、`12 邻里/老宅`、`13 自定义`; require a numeric reply. Option 13 may request one keyword in the next turn.
3. Set the project scale:
   - Single story: use `小节大纲.md` and `正文.md`.
   - Short-season serialized novel: use fixed 6 episodes/chapters with `大纲/细纲_第XXX章.md`, `episodes/`, and `追踪/`.
   - Do not plan a hundred-chapter roadmap unless the user explicitly asks for a long webnovel.
   - For a long narration episode around 15,000 characters, treat length as a functional-density target, not padding permission.
   - If the user asks for "完整正文" after choosing YouTube/朗读/推文 narration, default to 14,500-16,500 Japanese characters unless the user gives another target.
4. Check the ledger and choose a combination that has not been overused recently:
   - lane
   - protagonist role/age band
   - pressure source
   - proof object
   - reversal venue
   - aftertaste
5. Build the story engine:
   - Protagonist: age, role, old wound, quiet skill/resource, what they still protect.
   - Antagonist: spouse, in-law, adult child, remarriage partner, company superior, caregiver, neighbor, banker, facility worker, or scammer.
   - Exploitation: money, care labor, house, pension, inheritance, reputation, medical neglect, adult-child abandonment, or emotional erasure.
   - Proof object: diary, ledger, house deed, bank transfer, recorder, care log, will, diagnosis, security footage, registry, old photo, key, work ID, company register.
   - Reversal venue: hospital room, family meeting, funeral, lawyer office, company boardroom, airport, bank counter, police visit, care facility, or public ceremony.
   - Healing image: quiet meal, train ticket, apartment key, garden, grandchild's hand, old hobby, new job, second wedding, repaired room, or morning radio.
6. Draft in Japanese:
   - Start with a concrete event bomb in sentence one: a cruel line, document, hospital call, missing key, care note, inheritance notice, frozen bank account, or public humiliation.
   - Use first person `私` or close third person. First person is strongest for shame, endurance, and final calm.
   - Keep dense beats scene-level: dialogue, object, movement, witness, decision, consequence.
   - Compress generic background. Explain the long past through receipts, habits, scars, room details, medicine lists, bankbooks, and remembered lines.
   - Make the protagonist calm but not passive: they gather proof, set boundaries, call the right person, leave, sell, sign, refuse, testify, reveal, or transfer responsibility.
   - Preserve the selected lane's payoff loop. Do not flatten care labor, pension fraud, hospital proof, workplace reputation, or late-life romance into generic family revenge.
   - Audit each major scene as `entry state -> pressure/choice -> exit state`. At least one of proof, responsibility, money, housing, care burden, health decision, public reputation, family boundary, legal position, or next action must change. Repeated endurance, memories, seasonal scenery, or family scolding without a state delta must be compressed.
   - Track the episode promise through visible proof and consequence; the protagonist's final dignity must come from an exercised choice or right, not only from others regretting their behavior.
7. Polish:
   - Remove stock AI narration, abstract moralizing, repeated "静かに", and uniform paragraph rhythm.
   - Check that every emotional line has an object, action, witness, or consequence attached.
   - Delete or rewrite atmosphere, seasonal scenery, old memories, loneliness, kindness, beauty, silence, or sadness if it does not change proof, responsibility, money, housing, care, public reputation, relationship, or next action.
   - Count saved Japanese prose before delivery. If a YouTube/朗读完整正文 is below 14,500 characters, continue expanding dense beats instead of delivering: add proof movement, witness pressure, legal/financial/care state change, protagonist choice, public consequence, or recovery action.
   - If saved to a project file, run any available story deslop or punctuation checks already used by the project.
8. Record the generated work in the ledger with enough metadata to avoid repeating the same engine next time.

## Output Rules

- Keep planning/explanation in Chinese unless the user requests Japanese notes.
- Use Japanese prose for audience-facing story text by default.
- For project-bound output, do not leave the plan only in chat when the user expects reusable files; write the corresponding `设定/`, `大纲/`, `追踪/`, `对标/`, and `银发文学知识库/` artifacts.
- For quick concept work, output a compact plan first.
- For a finished prose request that is too long for chat, save `正文.md` or an episode file and report the path after reporting the character count. Do not report completion for a YouTube/朗读完整正文 until the saved prose is within the target range or the user has approved a shorter length.
