# Push Opening Template Deck

Use this for male-isekai push narration openings. Randomly draw one proven screenshot-derived template card, fill it with the current story, and connect directly into the body. Do not invent a new opening structure unless the user explicitly asks.

## Draw Procedure

1. Determine a primary lane such as `exile`, `battle`, `op`, `territory`, `academy`, `earth`, `tamer`, `craft`, `survival`, `rebirth`, `system`, or `mystery`.
2. Collect the last three used card IDs from the project opening ledger when available.
3. Run `scripts/draw-opening-template.py --lane <lane> --recent <comma-separated-card-ids>` from the `jp-isekai` skill directory.
4. Use the returned card exactly once. If the card cannot truthfully fit the story, redraw once; do not keep drawing until a preferred card appears.
5. Record the selected card ID with the finished work.
6. When there is no ledger, omit `--recent`. Never let the model choose the first or "best" card by habit.

## Template Deck

Fixed slots describe information functions. Fill them naturally; do not leave placeholders or translate Chinese connectors word for word into Japanese.

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

`主角明明具备某种人人都想要的价值，却被眼前的小队／家族／机构嫌弃；与此同时，多个更高层人物或势力正在寻找同一种能力；主角暂时不知道双方信息差；对方做出最后一次错误选择；接正文。`

Required chain: obvious value -> local rejection -> high-level demand -> information gap -> irreversible choice.

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

`主角突然花钱、囤货、锻造、训练或布置三项反常准备；旁人嘲笑或阻止；主角掌握未来灾变／重生信息／规则漏洞；倒计时出现；接第一项准备。`

Required chain: three preparations -> ridicule -> hidden future knowledge -> countdown -> first action.

### D3 单一规则连续兑现型

`一句讲明外挂规则；列出两个由小到大的具体兑现案例；第三次兑现落到当前主线危机；补充限制或歪打正着的代价；进入现场。`

Required chain: rule -> small proof -> larger proof -> current major proof -> limitation/cost.

## Fill Prompt

```text
你是小说推文口播作者。系统已经随机抽中模板卡：{card_id}。

请严格按照该卡的信息链，为以下故事写开头：
- 故事：{premise}
- 题材：{lane}
- 视角：{first_or_third_person}
- 语言：{language}
- 必须兑现的爽点：{promise}
- 正文起点：{body_start}

要求：
1. 使用抽中的模板，不得自行换模板或发明结构；
2. 写成一段连续、好懂、有信息升级的推文口播；
3. 前2句内交代主角身份和异常事件；
4. 完成卡片要求的信息链；至少一次明确升级，卡片要求多级递进时必须全部完成；
5. 最后一句自然接入正文起点；
6. 不写诗化断句、电影预告腔、纯谜语、复杂分析或结构说明；
7. 不照抄截图案例，只填充当前故事的事实；
8. 日文必须本地化成自然动漫解说口吻，不能逐字翻译中文连接词；
9. 输出模板编号和最终开头，不输出思维链。
10. 中文建议150—260字，日文建议250—450字，保持3—5句连续口播；每句必须增加新事实。
```

## Quality Floor

- If the result is weaker or less understandable than a straightforward fixed-form push opening, rewrite within the same card.
- Do not redraw merely because the wording is difficult; repair the wording first.
- Never merge two cards in one opening unless the user explicitly selects multiple cards.
- Randomness chooses the card, not story facts. All claims must be paid off by the outline.
