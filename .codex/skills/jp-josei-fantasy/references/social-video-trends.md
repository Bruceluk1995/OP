# Social Video Trends To Josei Fantasy Hook

Use when the user wants TikTok, YouTube, Shorts, viral videos, 热门视频, short-video hooks, or when Google Trends/news seeds feel boring.

The goal is not to copy a creator, video, character, franchise, joke, song, or exact scene. Extract the short-video hook mechanic: before/after proof, public reaction, apology failure, "nobody believed me until...", hidden cost, family/work/school absurdity, pet rescue, room/home transformation, food comfort, message misunderstanding, or comment-bait question. Then convert that mechanic into original Japanese female-audience fantasy romance.

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

- Entertainment
- People & Blogs
- Comedy
- Howto & Style
- Pets & Animals
- Gaming
- Science & Technology
- Sports

Downrank music/idol/MV trends unless the usable hook is public performance, disguise, social proof, fan ritual, or reputation recovery.

### TikTok

TikTok public access is less stable. Use it when available, but treat it as secondary unless a browser/login flow is available:

- TikTok Creative Center trends: `https://ads.tiktok.com/business/creativecenter/trends/hub/pc/en`
- TikTok Creative Center top ads / hashtags when public pages load.
- If public pages block, require browser/login reuse through `$browser-cdp` or ask the user for links/screenshots/keywords.

For TikTok, prefer format/mechanic trends over exact hashtags:

- before/after proof
- "POV" role reversal
- nobody believed me until proof appeared
- public apology failure
- hidden cost / paywall / subscription joke
- work/school/service absurdity
- food, room, clothing, or self-care transformation
- pet/familiar rescue
- misunderstood message or letter

## Video Hook Score

Score each candidate from 1-5:

- Hook clarity: Can the idea be explained in one sentence?
- Emotional stakes: Does it contain humiliation, loneliness, false blame, care, belonging, desire to be believed, or relationship tension?
- Proof/reversal: Does it contain a visible before/after, record, witness, public reaction, contract, apology, or social proof?
- Romance-fantasy conversion: Can it become a salon, engagement, academy, church, court, frontier manor, contract marriage, letter, curse, or family-inheritance mechanism?
- Safety/IP distance: Can it avoid copying creators, real people, copyrighted characters, clips, music, dialogue, and exact scenes?

Recommended pick:

- Main pick needs hook clarity >= 4 and total >= 19/25.
- Prefer family/relationship/proof/home/care/comedy/service hooks over celebrity or music-only hooks.
- If the hook depends on an existing anime/game IP, extract only the broad mechanic and change the world, characters, powers, names, and scene.

## Conversion Matrix

| Video hook | Josei fantasy conversion | Best route |
|---|---|---|
| before/after proof | ruined-reputation heroine shows ledger, dress, healing mark, estate result, or public witness | `engagement-annulment-zamaa` / `craft-job-competence` |
| "nobody believed me until..." | false saint/false villainess accusation reversed by church record or witness | `saint-replacement-church` / `villainess-otome-game` |
| public apology failure | annulment hearing, royal apology, salon rumor collapse, forged letter exposure | `engagement-annulment-zamaa` / `letter-misunderstanding-comedy` |
| room/home transformation | cursed duke manor, frontier home, neglected estate revived by competence and care | `beloved-duke-frontier` / `craft-job-competence` |
| hidden cost / paywall / subscription joke | dowry trap, marriage contract fee, noble debt, cursed service contract | `contract-marriage-white-marriage` / `palace-family-inheritance` |
| food/cafe/care routine | comfort as proof of attention, healing kitchen, tea-party social recovery | `craft-job-competence` / `beloved-duke-frontier` |
| pet rescue / animal misunderstanding | dragon/familiar/demon prince trusts the heroine first | `monster-demon-interspecies-romance` |
| sports trick / ranking question | academy trial, knight tournament, public skill assessment | `strong-heroine-status-gap` / `villainess-otome-game` |
| message misunderstanding | forged letter, mistranslated intent, delayed confession, restored trust | `letter-misunderstanding-comedy` / `contract-marriage-white-marriage` |

## Output Format

```markdown
1. 中文标题：
   日语标题：
   - Platform/source:
   - Video seed:
   - Hook clarity score:
   - Total video-hook score:
   - Extracted hook mechanic:
   - Selected josei route:
   - Backup route:
   - Converted proof/romance mechanism:
   - Heroine wound:
   - One-shot or serial promise:
   - Safety transform:
```

## Hard Rule

Never reproduce a creator's exact premise, joke order, clip sequence, catchphrase, music, or IP setting. Use only the hook mechanics and rebuild an original Japanese female-audience fantasy romance story.
