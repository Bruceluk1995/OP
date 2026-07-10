# Social Video Trends To Isekai Hook

Use when the user wants TikTok, YouTube, Shorts, viral videos, 热门视频, short-video hooks, or when Google Trends/news seeds feel boring.

The goal is not to copy a creator, video, character, franchise, joke, or exact scene. Extract the short-video hook mechanic: challenge, rule abuse, unexpected proof, "actually strongest" reveal, work/school absurdity, pet rescue, game mechanic, paywall trap, public reaction, or comment-bait question. Then convert that mechanic into an original Japanese male-audience isekai one-shot.

## Source Protocol

Use current sources before claiming what is trending.

### YouTube Japan

Prefer YouTube first because public trend lists are more accessible:

- Official page when browser access works: `https://www.youtube.com/feed/trending?gl=JP&hl=ja`
- Fallback current lists:
  - Kworb YouTube Trending Japan: `https://kworb.net/youtube/trending/jp.html`
  - CreatorDB YouTube Japan trending: `https://creatordb.app/free-tools/whats-trending-on-youtube/japan/`
  - YouTube Trends24 Japan: `https://youtube.trends24.in/japan`

Check categories, not only all-trending:

- Gaming
- Comedy
- Science & Technology
- Sports
- Pets & Animals
- Entertainment
- People & Blogs

Downrank music/idol/MV trends unless the usable hook is performance, ranking, fan ritual, disguise, or public proof.

### TikTok

TikTok public access is less stable. Use it when available, but treat it as secondary unless a browser/login flow is available:

- TikTok Creative Center trends: `https://ads.tiktok.com/business/creativecenter/trends/hub/pc/en`
- TikTok Creative Center top ads / hashtags when public pages load.
- If public pages block, require browser/login reuse through `$browser-cdp` or ask the user for links/screenshots/keywords.

For TikTok, prefer format/mechanic trends over exact hashtags:

- before/after proof
- "POV" role reversal
- impossible challenge
- one object solves everything
- hidden cost / paywall / subscription joke
- work/school/service absurdity
- pet/familiar rescue
- game exploit
- "nobody believed me until..."

## Video Hook Score

Score each candidate from 1-5:

- Hook clarity: Can the idea be explained in one sentence?
- Conflict/proof: Does it contain a visible challenge, rule, opponent, or test?
- Fantasy conversion: Can it become a skill, dungeon rule, guild test, boss mechanic, contract, route, or familiar behavior?
- Male-audience payoff: Can it deliver progression, public proof, zamaa, OP reveal, tactical win, or reward?
- Safety/IP distance: Can it avoid copying creators, real people, copyrighted characters, clips, music, dialogue, and exact scenes?

Recommended pick:

- Main pick needs hook clarity >= 4 and total >= 19/25.
- Prefer gameplay/mechanic/comedy/tech/pet/sports hooks over celebrity or music-only hooks.
- If the hook depends on an existing anime/game IP, extract only the broad mechanic and change the world, characters, powers, names, and scene.

## Mandatory User Selection Gate

1. Collect 6-10 raw current items and score them internally.
2. Present 3-5 viable numbered candidates using the format below. Include source/date or recency and a direct source link when available.
3. Ask the user to choose a candidate number or request another batch, then stop.
4. Do not treat “YouTube/TikTok”, a video category, subtype, payoff, or tone as selection of a concrete video seed.
5. Do not choose the highest-scoring candidate, build the final blueprint, draft prose, or save files until the user selects one.
6. Bypass the pause only if the user supplied the exact video/link/keyword or explicitly delegated selection with `你选/自动选/直接选最好的`. When delegated, identify the chosen candidate before continuing.

## Conversion Matrix

| Video hook | Isekai conversion | Best route |
|---|---|---|
| game exploit / "actually strongest weak unit" | mocked weak skill reveals hidden boss-rule value | `battle-leveling` / `op-dominance` |
| forced labor / underground work / resource grind | dungeon labor rule, exploited porter, buried reward | `exile-support-reversal` / `dungeon-master-territory` |
| paywall / paid button / subscription joke | cursed guild fee, noble toll, magic-service trap | `exile-support-reversal` / `craft-commerce-slowlife` |
| bad apology / message not understood | intent translation, truth record, royal hearing | `academy-game-knowledge` / `exile-support-reversal` |
| office/meeting-room transformation | territory/base management, functional room rebuild | `dungeon-master-territory` / `craft-commerce-slowlife` |
| pet rescue / animal misunderstanding | familiar contract, monster behavior rule, tamer proof | `tamer-familiar` |
| sports trick / trajectory question | guild projectile trial, wind/angle skill, rank match | `battle-leveling` |
| tech DIY / weird device | earth-commute tool logic, magic device exploit | `earth-commute` / `op-dominance` |

## Output Format

```markdown
1. 中文标题：
   日语标题：
   - Platform/source:
   - Video seed:
   - Hook clarity score:
   - Total video-hook score:
   - Extracted hook mechanic:
   - Selected theme route:
   - Backup route:
   - Converted cheat/skill:
   - One-shot promise:
   - Safety transform:
```

## Examples From YouTube-Type Hooks

- "地下の強制労働施設で埋蔵金を探す" -> exploited dungeon labor + buried reward; use a mocked `採掘経路鑑定` or `収納` skill.
- "同じ弱キャラなのに使用率3%以下が実は最強" -> overlooked weak skill/monster is strongest under a hidden rule.
- "有料化システムでホームボタンを押すとどうなる?" -> cursed paywall magic service; protagonist exposes the hidden contract.
- "伝わらない謝罪会見" -> `意図翻訳` or `真偽記録` skill in a public guild hearing.
- "会議室を居抜きして社食にする" -> base/territory conversion; protagonist turns useless room into survival infrastructure.

## Hard Rule

Never reproduce a creator's exact premise, joke order, clip sequence, catchphrase, music, or IP setting. Use only the hook mechanics and rebuild an original isekai story.
