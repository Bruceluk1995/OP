# Hot Source Router

Use when the user has no topic, wants 热点选题, asks for TikTok/YouTube, rejects Google Trends/news as boring, or says "都选/全选".

The goal is to choose a source strategy before title generation. Do not treat one platform as the default answer for every topic. Different sources reveal different signals:

## Source Menu

Ask this when the source is missing:

```text
你想从哪个热点入口找题？

1. YouTube/TikTok 热门视频：适合找视觉钩子、短视频标题、公众情绪和解释切口
2. Google Trends：适合看搜索需求和短期疑问
3. 新闻/离谱社会事件：适合制度、社会、教育、劳动、公共服务问题
4. 官方/数据/报告：适合政策、经济、人口、能源、科技、国际关系
5. 常青选题库：不追热点，做长期可看解释
6. 全选：多源交叉筛，选最适合讲解的题
```

## All-Source Mode

When the user chooses `全选`, collect small batches from all available sources:

- 3-5 Google Trends seeds.
- 3-5 YouTube/TikTok video hooks when public access works.
- 3-5 news/social-event seeds.
- 2-4 official/data/report seeds if the lane requires facts.
- 2-4 evergreen angles from the selected topic pack.

Then score everything together. Do not output one title per source by default; output the best mixed shortlist.

## Scoring

Score each seed from 1-5:

- Hook clarity: can the viewer understand the question in one sentence?
- Structural depth: does it reveal history, institution, incentive, geography, technology, or state capacity?
- Audience fit: does it matter to the chosen audience pack?
- Evidence availability: can key facts be verified quickly?
- Long-tail value: will the explanation still be useful after the trend fades?

Recommended pick:

- Main candidate needs total >= 19/25.
- If a source is hot but structurally shallow, reject or use it only as an opening anecdote.
- If a source is dry but structurally strong, upgrade it with a video/social hook.

## Source-Specific Use

| Source | Best for | Avoid |
|---|---|---|
| YouTube/TikTok | visible public reactions, short-video hooks, games/media/tech/work/society phenomena | copying creators, clips, jokes, songs, anime/game IP, or exact video sequences |
| Google Trends | search demand, "why now", public questions | celebrity/sports gossip with no mechanism |
| News/social events | institutions, law, labor, schools, infrastructure, social common sense | crime/tragedy spectacle or private-person stories |
| Official/data/report | policy, demographics, energy, money, geopolitics, technology | dry listicles without a central question |
| Evergreen | history and durable systems | stale textbook framing |

## Output Fields

For title batches, include:

```text
- Hot source mode:
- Source seed:
- Source type:
- Why this source:
- Topic pack:
- Audience pack:
- Promised argument:
- Fact-check/source note:
```

## Hard Rule

Never copy a video/news item's characters, wording, creator persona, exact scenes, or private-person details. Extract only the public question or mechanism, then rebuild an original explainer.
