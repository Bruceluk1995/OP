# Josei Push Opening Template Deck

Use only for female-audience fantasy-romance push narration. Filter by lane, randomly draw one compatible card, fill it truthfully, and record its ID. Do not merge cards or invent a nineteenth structure unless the user explicitly asks.

## Draw Procedure

1. Determine one primary lane: `engagement`, `saint`, `villainess`, `contract`, `family`, `beloved`, `loop`, `proof`, `craft`, or `mystery`.
2. Collect the last three card IDs from the project ledger when available.
3. Run `scripts/draw-opening-template.py --lane <lane> --recent <ids>` from the `jp-josei-fantasy` skill directory.
4. Fill the returned card. Redraw once only if required story facts are absent.
5. Record card ID, lane, proof object, public venue, heroine decision, and opening first sentence.

## Cards

### J01 公开婚约破弃反转

Public humiliation/annulment -> heroine calmly accepts -> opponent escalates by taking status/property -> heroine reveals the evidence or condition they fear -> return to before the ceremony.

Lanes: engagement, villainess, proof.

### J02 反向服从撤回付出

Opponent orders heroine to leave/stop/hand over a role -> heroine agrees too quickly -> opponent celebrates -> heroine states what labor, blessing, contract, or protection leaves with her -> first visible failure begins.

Lanes: engagement, saint, family, craft.

### J03 假圣女上位后连续失效

Replacement is crowned -> true saint is expelled -> purification/healing/barriers fail in two or three concrete ways -> church record points to heroine -> heroine has already been welcomed elsewhere.

Lanes: saint, proof.

### J04 恶役千金避死触发新路线

Heroine knows the original death flag -> actively avoids the first fatal action -> male lead or system makes an impossible deviation -> safer route becomes a new danger -> enter the changed scene.

Lanes: villainess, loop.

### J05 契约到期主动离婚反转

Contract deadline arrives -> heroine submits separation/divorce first -> witnesses expect male lead's relief -> he refuses under a previously established respectful condition -> heroine must choose, not merely be claimed.

Lanes: contract, beloved.

### J06 继承权让出后债务反转

Favored sibling receives inheritance -> heroine signs without resistance -> will/blood seal/ledger activates -> apparent fortune reveals debt, curse, or duty -> real asset recognizes heroine because of prior work.

Lanes: family, proof.

### J07 女主离开前后崩坏

While heroine stayed, household/temple/territory worked normally -> after she leaves, three concrete systems fail -> family discovers her invisible labor -> heroine is already respected in a new place.

Lanes: family, saint, craft, beloved.

### J08 被嫌弃与被具体珍视

Local group calls heroine cold/useless -> higher-status person names specific things she did, not her beauty -> public recognition restores dignity -> romance promise follows after proof.

Lanes: beloved, saint, villainess.

### J09 重生后让出前世选择

Previous life followed family route and ended badly -> heroine returns to choice day -> rival takes her former option -> heroine does not resist and chooses another path -> hidden cost of the stolen option begins.

Lanes: loop, family.

### J10 双重生抢走表面幸福

Heroine and rival both remember the past -> rival grabs the apparently superior fiancé/role -> heroine knows its concealed price -> their opposite choices start producing opposite results.

Lanes: loop, villainess, family.

### J11 文件最后一条翻案

Marriage paper/will/church register is used to accuse heroine -> heroine asks that the hidden final clause be read aloud -> identity, liability, or inheritance reverses -> public room reacts -> enter document origin.

Lanes: engagement, saint, family, proof.

### J12 被夺功劳的二次实证

Rival claims heroine's achievement -> public detector cannot decide -> heroine demonstrates the cost, wound, process, or second proof only the true worker knows -> result changes status and relationship.

Lanes: saint, craft, proof.

### J13 小谎证据连锁崩塌

Everyone accepts one testimony -> prepared witness/record disproves one small detail -> that contradiction collapses the larger accusation -> antagonist's own statement becomes final evidence.

Lanes: engagement, family, proof, mystery.

### J14 耻辱印记其实是功勋

Mark/curse/scar is publicly used to shame heroine -> institution or informed person identifies it as sacrifice, protection, or legitimate proof -> humiliation venue becomes recognition venue -> heroine decides what recognition means.

Lanes: saint, villainess, beloved, proof.

### J15 不公平规则漏洞反杀

Everyone obeys one unfair marriage/church/inheritance rule -> heroine appears trapped -> she reveals a hidden clause or contradiction -> uses it publicly to free herself and expose an older case.

Lanes: saint, engagement, family, proof.

### J16 先还名誉再公开选择

Crowd expects male lead to choose replacement -> he first presents evidence restoring heroine's name -> then publicly chooses or proposes partnership -> heroine retains the right to accept or refuse.

Lanes: beloved, engagement, saint, proof.

### J17 小愿望滚成王国事件

Heroine wants one small practical thing: shop, divorce, sleep, safe room -> small action solves a larger local problem -> consequence reaches male lead/territory/court -> romance or public contract follows through clear causality.

Lanes: contract, craft, beloved.

### J18 错投信件／契约对象掉马

Letter/ring/application/help request goes to wrong person -> heroine expects rejection -> receiver formally accepts -> identity reveal creates romantic and social stakes -> heroine actively decides whether to continue.

Lanes: contract, beloved, mystery.

## Fill Prompt

```text
你是日本女性向幻想恋爱推文口播作者。系统随机抽中模板卡：{card_id}。

请严格按照该卡的信息链写开头：
- 故事：{premise}
- 题材：{lane}
- 视角：{first_or_third_person}
- 语言：{language}
- 女主当前伤口／损失：{heroine_wound}
- 必须兑现的证据、恋爱与反杀：{promise}
- 正文起点：{body_start}

要求：
1. 不换卡、不混卡、不发明新结构；
2. 前2句讲清女主身份和当下爆点；
3. 完成卡片要求的信息链，至少一次明确递进；
4. 女主必须有主动选择，不能只等高位男主救场；
5. 先恢复尊严／证据，再推进恋爱；
6. 写成连续推文口播，不写文学氛围、诗化断句或预告片碎句；
7. 日文要自然本地化为女性向动漫解说口吻；
8. 最后一句直接接正文；
9. 只输出模板编号和最终开头。
```

## Safety and Quality

- Do not import incest, sexual violence, crude sexual jokes, misogyny, IP characters, fabricated extreme numbers, or humiliation that objectifies the heroine.
- Do not use male lead status as the only proof. Evidence and heroine action must matter.
- Do not make zamaa coincidence-based. Use records, witnesses, law, contracts, church rules, work results, or antagonist actions.
- If wording is weak, repair within the same card. Redraw only for factual incompatibility.
