# Push Opening Template Deck

Optional ideation deck for male-isekai push openings. Use only when the writer lacks a strong event-based opening or the user asks for variation. The authoritative workflow is `../../jp-short-fiction-studio/SKILL.md`; a card may inspire an entrance but never becomes a delivery gate.

## Optional Draw Procedure

0. First build a **visual story core**: one ordinary action or loss, one visible physical change, and one human consequence. If that already produces a strong opening, skip the deck.
1. Determine a primary lane such as `exile`, `battle`, `op`, `territory`, `academy`, `earth`, `tamer`, `craft`, `survival`, `rebirth`, `system`, or `mystery`.
2. Run `scripts/draw-opening-template.py --lane <lane> --root <project-root>` from the `jp-isekai` skill directory. The script automatically reads the last three `opening_card` values from `男频异世界短篇知识库/generated-ledger.jsonl`; use `--recent` only to add unsaved/current-session exclusions.
3. Treat `required_chain` and `surface_beats` as prompts, not obligations. Abandon the card when it weakens clarity, voice, or retention.
4. Record a card ID only when project anti-homogenization is explicitly in use.

## Card-Specific First-Shot Suggestions

The draw script returns `surface_beats`. Use whichever beats create the strongest truthful event; fixed order and first-1,000-character coverage are not required.

- `N1` begins with a ridiculous proof action; `A1` begins with a mistake; `E1` begins with a forbidden-but-practical move.
- `R1` begins while humiliation is happening; `C1` begins while the rejecter destroys or discards something valuable.
- `P2` begins with a tiny need; `F1` begins with the first suspicious preparation; `B1` begins with a boast coming back to bite.

For first-person narration, each card still needs one short, practical judgment that fits its own scene. For example, C1 may use: `九銅貨の石ころを朝食と呼ぶ勇気は、俺にはない。` Do not force the same quip position or the same four-step rhythm onto every card.

Keep the first-person knowledge boundary honest: do not claim that unseen nobles, hospitals, or officials are searching for something unless the protagonist has learned it on page.

## Audience Orientation Floor

Fast is not the same as cryptic. But do **not** solve confusion by stopping the story to define the setting. A new listener should understand through a familiar action, loss, want, or visible result—not through a glossary sentence.

- Start with a person doing something ordinary and legible: spending their last coins, feeding a creature, being thrown out, failing to buy breakfast, a worker joining a queue. Let the strange noun appear inside that action.
- Do not introduce three hard nouns in one breath. If a card needs three preparations, first show one comprehensible umbrella action such as `我把最后三铜换成了牲口都不吃的残渣`; reveal `甜菜渣、裂口陶罐、粗麦粉` only when each changes the outcome.
- A result-first price can lead if the price immediately causes a familiar reaction: `九铜一块的面包，搬一天货的人已经买不起了`. Do not pause to define what the bread, guild, rank, or institution is.
- Institutions exist only when they obstruct, buy, punish, or lose. Introduce `面包师公会` by having it burn a starter, seize a stall, or refuse flour—not by explaining its administrative jurisdiction.
- Ban empty near-miss and inflation words such as `差点`, `险些`, `直接`, `瞬间`, and `当场` unless the exact missed outcome, action, or time pressure is stated in the same sentence.
- The test is simple: if the line could be replaced by a glossary entry without changing the story, cut it.

## Visual Story Core Gate

Do not draw a card to rescue a weak premise. The card only chooses the entrance; it cannot make a list of materials, an undefined magical product, or an accounting rule feel like a story.

- Before drafting, write `ordinary action/loss -> visible change -> human consequence` in one line. If it cannot be understood without terms such as `金色发酵种`, `稀有材料`, `魔力回路`, `F级`, or institution names, rebuild the cheat first.
- The first proof of a craft/food cheat must be a change the listener can picture: dead dough rises, a cracked bowl overflows, a hard loaf becomes soft, one sack feeds more people, a queue forms, a hungry child can eat. Do not lead with a named magical ingredient, a glowing color, or an inventory list.
- A magic item may appear after it changes a current action. `面团把木盆顶裂了` can later be called a special starter; `它吐出金色发酵种` cannot carry the opening by itself.
- If the protagonist's action exists only to display preparation items, replace it with a real choice, cost, embarrassment, hunger, refusal, or rescue.
- No exact-quote evidence is required for normal delivery. Project teams may record examples for research, never as quality proof.

## Optional Card Diagnostics

When debugging the deck itself, a project may create `开头抽卡证据.json` beside `作品资料.md` using exact quotes from the body:

```json
{
  "card_id": "F1",
  "evidence": {
    "three_preparations": "exact quote from the opening",
    "ridicule_or_obstruction": "exact quote from the opening",
    "hidden_knowledge_or_loophole": "exact quote from the opening",
    "countdown": "exact quote from the opening",
    "first_action_bridge": "exact quote from the opening"
  },
  "surface_evidence": {
    "<first beat returned by draw>": "exact quote from the opening",
    "<second beat returned by draw>": "exact quote from the opening",
    "<third beat returned by draw>": "exact quote from the opening",
    "<fourth beat returned by draw>": "exact quote from the opening"
  },
  "visual_core_evidence": {
    "ordinary_action_or_loss": "exact quote from the opening",
    "visible_change": "exact quote from the opening",
    "human_consequence": "exact quote from the opening"
  }
}
```

Use the slot names returned by the draw script; do not copy the F1 keys for another card. `surface_evidence` uses that card's `surface_beats`; `visual_core_evidence` always uses the three keys above. Then run:

```powershell
python .codex/skills/jp-isekai/scripts/validate-opening-evidence.py `
  --body episodes/oneshots/<slug>/正文/正文.md `
  --evidence episodes/oneshots/<slug>/开头抽卡证据.json
```

This diagnostic checks whether a chosen card was represented; it does not approve an opening and never blocks normal delivery. If the card conflicts with the better story opening, discard the card rather than rewriting to satisfy it.

## Template Deck

Fixed slots describe escalation functions. Fill them naturally through the selected card's first-shot pattern; do not leave placeholders or translate Chinese connectors word for word into Japanese. No card may open with a static explanation when its `surface_beats` calls for an active scene.

### R1 反转・身份受辱型

`主角拥有一个低位／被嘲身份，却因具体原因遭到公开否定；众人不仅做出第一层错误判断，甚至造成更严重后果；然而主角真正拥有的是具体外挂／规则优势；事情要从某个起点说起。`

Required chain: identity -> humiliation/misjudgment -> escalation -> hidden advantage -> body origin.

### R2 反转・世界常识错误型

`这个世界所有人都相信某条常识，因此主角也被按该常识判定；可主角第一次实际测试便出现相反结果；更离谱的是结果继续升级；其他人尚不知道真正原因；接正文。`

Required chain: world rule -> protagonist classification -> contradictory test -> larger escalation -> cause gap.

### R3 反转・转生结果型

`主角转生／觉醒成看似最差的身份或物种，而且处境进一步恶化；旁人因此轻视或利用他；可主角随后发现该身份隐藏的具体成长机制；第一次行动即产生异常结果；接正文。`

Required chain: bad rebirth -> worse condition -> external contempt -> hidden mechanism -> first payoff.

### N1 无脑・证明离谱设定型

`为了证明一个离谱规则／能力，主角执行一个具体测试；测试对象或方法本身已经反常；结果不仅证明规则成立，还引发第二级夸张后果；更大的影响随即出现；接正文。`

Required chain: proof goal -> concrete test -> unexpected result -> second escalation -> consequence.

### N2 无脑・第一次就失控型

`主角第一次做某件普通或低级事情，却直接得到远超常识的结果；不仅周围人无法理解，连制度／系统／强者都被迫反应；而主角最初只是为了一个非常实际的小目标；接正文。`

Required chain: first attempt -> impossible result -> public/system reaction -> mundane motive -> body.

### N3 无脑・全民错误认知型

`全世界／全国／整个行业的人都对某人或某规则存在同一种认知；其实目标并非表面身份，而是另一种具体存在；更夸张的是旧传说或公开记录也理解错了；直到主角做出某个动作；接正文。`

Required chain: mass belief -> correction -> deeper correction -> protagonist trigger.

### C1 对比・被嫌弃与被争抢型

`主角正在被眼前的小队／家族／机构毁掉、扔掉或低价处理一个看似没用的东西；主角用一件不合常理但很实际的方式接住残余价值；价值立刻通过顾客、怪物、货物或现场效果自己证明；刚才拒绝他的人回头阻拦、收购或强夺；主角做出让旧机构失去选择权的决定；接正文。`

Required chain: rejection/destruction -> improper countermove -> visible value -> return pressure -> irreversible choice.

### C2 对比・离开前后型

`主角在场时，团队一直保持某个看似理所当然的良好状态；主角离开后，短时间内连续出现三项具体故障／失败；团队这才发现被忽视的工作或能力；但主角已经进入新的机会；接正文。`

Required chain: before stability -> departure -> three concrete failures -> realization -> protagonist's new path.

### P1 铺垫・异常行为合理借口型

`主角先做出一件看似离谱的异常行为；他给出一个非常现实的借口；行为却产生意外收益；借口背后逐渐暴露真正的世界规则或外挂；接当前动作。`

Required chain: abnormal behavior -> practical excuse -> unexpected result -> hidden rule -> current action.

### P2 铺垫・小目标滚成大灾难型

`主角最初只想解决一个极小、极现实的问题；行动产生第一个意外收益；收益又触发新的规则；规则最终引来远超原目标的大人物／怪物／国家级后果；而一切源于最初的小目标；接正文。`

Required chain: tiny motive -> accidental gain -> rule escalation -> large consequence -> return to origin.

### D1 直接上・世界规则清单型

`直接说明这是一个怎样反常的世界；列出三种不同人群在该规则下会获得的具体能力或后果；随后说明主角得到的东西既不在其中又更加离谱；马上进入第一次验证。`

Required chain: abnormal world -> three concrete examples -> protagonist exception -> immediate test.

### D2 直接上・主角设定连爆型

`直接说出主角的新身份；紧接着给出第一项优势、第二项升级和第三项更夸张的限制／代价；最后用一个正在发生的危机验证这些设定；进入正文。`

Required chain: identity -> advantage -> escalation -> cost/limit -> live crisis.

### E1 经验共识・偏偏反着做型

`做过某职业／任务的人都知道一条避坑常识；列出正常人会如何处理；主角却偏偏反着做；不是因为愚蠢，而是掌握具体利益或外挂规则；当前行为即将验证。`

Required chain: shared experience -> normal avoidance -> protagonist violation -> concrete reason -> live proof.

### A1 意外・误操作滚大型

`主角因喝醉、手滑、错认、错发或选错对象做出错误操作；本以为会受罚或社死；结果错误竟然成立；随后触发更大的第二级结果；隐藏规则出现。`

Required chain: mistaken action -> expected punishment -> successful anomaly -> second escalation -> hidden rule.

### B1 吹牛／谎话字面成真型

`主角随口吹牛或说谎；隔天内容以具体方式成真；旁人仍不相信；第二次更夸张的兑现出现；世界规则／系统机制被揭开。`

Required chain: casual claim -> literal fulfillment -> disbelief -> stronger fulfillment -> rule reveal.

### C3 对比・明明有功却受罚型

`主角明明完成具体功绩或拥有稀缺价值；却遭到与事实相反的待遇；证人或制度暂时支持错误判断；主角掌握的证据／规则反转局面；接事件起点。`

Required chain: concrete merit -> opposite treatment -> institutional misjudgment -> proof/reversal -> origin.

### F1 反常备灾／囤积型

`先让观众看见一个普通人能读懂的生活动作或马上要发生的损失；主角才突然花钱、囤货、锻造、训练或布置三项反常准备；旁人嘲笑或阻止；主角掌握未来灾变／重生信息／规则漏洞；倒计时出现；接第一项准备。`

Required chain: ordinary stake -> three preparations -> ridicule -> hidden future knowledge -> countdown -> first action.

### D3 单一规则连续兑现型

`一句讲明外挂规则；列出两个由小到大的具体兑现案例；第三次兑现落到当前主线危机；补充限制或歪打正着的代价；进入现场。`

Required chain: rule -> small proof -> larger proof -> current major proof -> limitation/cost.

## Fill Prompt

```text
你是小说推文口播作者。系统已经随机抽中模板卡：{card_id}。

请严格按照该卡的信息链和该卡专属的 `surface_beats`，为以下故事写开头：
- 故事：{premise}
- 题材：{lane}
- 视角：{first_or_third_person}
- 语言：{language}
- 必须兑现的爽点：{promise}
- 正文起点：{body_start}

要求：
1. 使用抽中的模板，不得自行换模板或发明结构；
2. 先依次完成该卡的 `surface_beats`；每个 beat 必须是一句能被镜头拍到的动作、物件变化、明确后果或正在发生的处境，不能替换成背景说明；
3. 再完成卡片要求的信息链；至少一次明确升级，卡片要求多级递进时必须全部完成；
4. 第一人称必须有一句短促的实用吐槽／判断／反击，且位置与内容服从所抽卡片的现场，不得写成口号；
5. 开写前先锁定“普通动作／损失 -> 可见变化 -> 人的后果”。陌生材料、稀有配方、金色光效和杂物清单不得充当可见变化；
6. 在第二次升级前完成观众定位，但只能通过人物动作、花钱、丢失、排队、挨饿、阻拦或可见结果完成；不得用定义句解释黑面包、公会、等级、怪物或制度；
7. 用8—12行短口播推进，每行只给一个画面或因果变化；不要把背景事实均匀排成清单；
8. 最后一句自然接入正文起点；
9. 不写诗化断句、电影预告腔、纯谜语、复杂分析或结构说明；禁用没有精确后果的“差点／险些／直接／瞬间／当场”；
10. 不照抄截图案例，只填充当前故事的事实；日文必须本地化成自然动漫解说口吻，不能逐字翻译中文连接词；
11. 输出模板编号和最终开头，不输出思维链。
```

## Quality Floor

- If the result is weaker or less understandable than a straightforward fixed-form push opening, rewrite within the same card.
- If the opening ignores the selected card's `surface_beats` and can be reduced to a premise summary, it fails even when every chain slot is present.
- A practical joke must sharpen the conflict or reveal the narrator's judgment. Do not bolt on a quip that changes nothing.
- Do not redraw merely because the wording is difficult; repair the wording first.
- Never merge two cards in one opening unless the user explicitly selects multiple cards.
- Randomness chooses the card, not story facts. All claims must be paid off by the outline.
