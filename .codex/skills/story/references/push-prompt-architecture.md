# Push Prompt Architecture

Use this prompt stack for every anime-recap/push-narration production run. It translates a premise into a speaker-led emotional account before retention, viewpoint, and surface editing.

Do not collapse these roles into one prompt. A writer cannot invent, structure, voice, and approve the same draft in one undifferentiated pass.

## 1. Speaker and Listener Contract

Lock a concrete speaking situation, not a vague adjective list:

```text
speaker identity and lived filter:
one imagined listener:
why the speaker must tell this story now:
what the listener already understands:
what the speaker finds absurd, painful, exciting, shameful, or satisfying:
words or sentence habits this speaker naturally uses:
neutral/reporting voice that is forbidden:
```

The speaking situation is a mouth simulator, not scenery to mention in the script. A first-person narrator tells an event they survived or later reconstructed. A third-person narrator sounds like an invested fan explaining why this person's story is worth hearing, not a database reading an event log.

Use the **one-listener test**: hide the prose and imagine the speaker saying it to one real listener. If the wording sounds like a synopsis, instruction manual, school essay, or production memo, rewrite it in the speaker's mouth.

Before the body, make one private voice-calibration pair from the current premise:

```text
neutral event-log version:
same event in this speaker's mouth:
selection/judgment that makes the second version personal:
```

Discard the calibration pair from audience-facing output. Do not import a stock slang persona across genres. Narration and decisive dialogue must sound as though they belong to the same social and story world.

## 2. Audience Emotional Contract

Before story structure, record:

```text
audience enters wanting:
dominant pressure emotion:
secondary flavor: humor / tenderness / dread / indignation / wonder / romance / other
protagonist's current desire:
what the audience should urge the protagonist to do:
mid-story emotional conversion:
final release emotion:
title promise:
```

Every major module needs an **emotional job**, not only a plot job:

```text
emotion entering -> concrete pressure/evidence -> protagonist response -> emotion leaving -> next desire
```

If the emotional state does not change, the module is setup, bridge, or repetition even when facts change. Rotate functions and emotions; constant escalation of one identical feeling becomes numbness.

Express the emotional change through behavior, object, decision, silence, or consequential speech before naming it. A label such as `he was furious` cannot perform the module's emotional job by itself.

## 3. Story-Specific Concrete Anchors

Extract these from the actual premise instead of inserting generic hooks:

```text
core contradiction:
relationship under pressure:
one object or physical trace that carries meaning:
one exact action that proves the conflict:
one number only if it changes scale, cost, time, or credibility:
one decisive line whose wording changes power or choice:
emotional high point:
hook anchor — the visible fact/action/line that creates "what happens next":
```

Prefer evidence the audience can picture or hear: a name erased from a card, a hospital going dark, a chair left empty, a hand refusing an offered tool, a contract torn before witnesses. Abstract labels such as `the system was unjust` or `her skill evolved` are conclusions, not anchors.

Hooks must grow from the core promise. End a module with a visible action, line, information gap, ironic consequence, countdown, or meaningful silence. Reveal enough to change expectation and withhold only the consequence still unfolding. Generic future promises and `he did not know` do not qualify.

## 4. Active Character Response

The protagonist and important companions cannot spend the story receiving information while systems act around them.

For each expanded event, record:

```text
pressure received:
the character's characteristic response:
what that response risks or sacrifices:
who answers or resists:
visible consequence:
```

Pain, surprise, admiration, and agreement are reactions, not agency. A response must alter the plan, relationship, evidence, risk, or available choice. A hidden plan may create suspense, but the body must show concrete actions that make the later payoff fair.

## 5. Separate Production Passes

Run in this order:

1. **Fact keeper** — extract approved facts, causal order, viewpoint knowledge, title promise, and ending requirement. Do not write style.
2. **Emotion designer** — assign every candidate event an emotional job and label it `expand / one-line bridge / cut`.
3. **Entertainment editor** — require human collision, character response, concrete anchor, memorable action/line, and payoff shape.
4. **Speaker writer** — draft natural spoken sentences through the locked speaker/listener contract. Do not split subtitles yet.
5. **Hook editor** — derive opening and module-end hooks from actual anchors and the audience's current wait; do not paste hook templates.
6. **Read-aloud editor** — listen with line breaks hidden. Repair neutral reporting, long setup, dialogue runway, breathless fragments, and unclear subjects.
7. **Adversarial editor** — use the entertainment, retention, and viewpoint gates on the saved body. The writer does not self-approve.
8. **Surface editor** — split subtitles and run shape lint last.

For source rewriting, preserve approved facts but rebuild voice and emphasis from the extracted fact sheet. Do not sentence-polish the old draft line by line when its selection or emotional curve is wrong.

Keep attention asymmetric like real telling: one decisive object, action, or line may receive detail while travel, repeated proof, and already-understood mechanics disappear into a bridge. Before decisive dialogue, use no runway or one brief action beat by default; several sentences of facial expression or abstract thought drain the line's force.

## 6. Example Pair

Reject an accurate event log:

```text
ミアの清掃スキルが進化した。
続いて四人は配管の役割を確認した。
セラが優先順位を決め、リネが管を結び、ベラが点火した。
その結果、学院の供給制度は停止した。
```

Target a speaker-led emotional event:

```text
ミアが自分の名札をひと拭きした瞬間、王立病院の灯りが全部消えた。
学院長は止めなかった。むしろ笑った。
「続けろ。お前が一本取り返すたび、先に病人が死ぬ」
ここで俺たちの目的が変わった。
炉を壊すだけじゃ足りない。誰も殺さずに、盗まれた力を奪い返す。
```

The second version works because a mechanism becomes a threat, a person speaks, the protagonist judges, and the goal changes. Short lines are not the cause.

## 7. Anti-Template Rules

- Do not impose a universal 9/10-chapter skeleton, fixed hook interval, fixed quote count, fixed joke interval, or fixed single-line percentage across genres.
- Do not require a self-deprecating aside every N characters; humor must come from the selected speaker and current pressure.
- Do not ban ordinary words globally when the speaker would naturally use them. Remove repetition and AI habits in context.
- Do not confuse a monetization/paywall hook around the midpoint with the final title-promise payoff of a closed one-shot.
- Positive/negative examples teach function. Never reuse their names, objects, scene order, or exact wording as story content.
- Transfer prompt functions across markets, not Chinese platform catchphrases or sentence templates. Japanese audience-facing copy must still pass the selected Japanese genre and viewpoint localization rules.
