# Japanese Male-Isekai Character Prompt Contract

Use this contract whenever a male-isekai route invents named characters, outputs a cast, drafts a script with named characters, or saves an episode/one-shot.

## Delivery Trigger

- Treat the character-prompt companion as part of the male-isekai script, not as an optional cover package.
- When a saved script or project plan introduces named characters, create or update its adjacent character-prompt file.
- For a one-shot, use `角色提示词/角色提示词.md`. For a serialized episode, use `角色提示词.md`. For a project plan that creates the reusable cast, use `设定/角色提示词.md`.
- For chat-only work, append a compact character-prompt block after the requested artifact, or save it beside a long body and link it. Omit it only when the user explicitly requests body-only output.
- Include the protagonist, named heroines/companions, and major named antagonist. Do not create prompts for anonymous extras.

## Language and File Shape

- Write prompt bodies in natural Japanese only. Do not use English prompt prose or Chinese prompt prose.
- Start with one reusable `## 共通画風` paragraph, then use one `## キャラクター名` heading and one copyable paragraph per character.
- Keep the common style paragraph compact: Japanese commercial male-audience isekai anime, cel-style anime coloring, clean line art, attractive Japanese anime faces, neutral reference posture, plain background, empty hands, no text or watermark.
- Keep every character paragraph to durable identity only: age, role/species, height and proportions, hair color/style/texture, eye color, face, baseline expression/temperament, clothing silhouette and colors, and worn accessories such as glasses, ribbons, earrings, or hair ornaments.

## No-Held-Prop Reference Rule

Character mother prompts are identity references, not scene prompts. Keep both hands empty.

Do not include:

- symbolic possessions, signature objects, carried keepsakes, books, cards, tags, cloths, ropes, tuning forks, tools, cooking utensils, staffs, swords, guns, shields, or other weapons;
- phrases such as `象徴的な持ち物`, `象徴的な道具`, `手に持つ`, `握っている`, `掲げる`, `構える`, `携える`, or `腰に剣を下げる`;
- skill activation, spell light, aura, flames, sound waves, status panels, summoned creatures, or other temporary effects;
- cover composition, camera, shot size, background scene, action pose, one-off plot emotion, or another character's interaction.

Move weapons, tools, props, skill effects, action, and scene composition into the cover/shot prompt for the exact scene that needs them. A character prompt must still work as a neutral reference image when no story object is present.

## Male-Audience Heroine Look

- Unless the premise or user explicitly requires another visual lane, design named female leads and companions as distinct heroines from a Japanese commercial isekai harem anime.
- Do not infer a middle-aged face, tired body, or documentary-like workwear from occupation, poverty, widowhood, motherhood, trauma, or years of labor.
- For young adult heroines, use a clearly adult story age while preserving the youthful anime-girl look: large clear eyes, small nose and mouth, soft cheeks, fine chin, glossy hair with highlights, a lively six-and-a-half to seven-and-a-half-head anime proportion, and bright controlled color design.
- Express an occupation through clothing colors, trim, patterns, and silhouette. Do not force the character to hold the occupation's tool in every reference image.
- Assign visibly different heroine lanes when several women appear: orthodox/innocent, tsundere or strong big-sister, cool/quiet, energetic, healing/gentle, mischievous, noble, knightly, magical, or another story-fitting lane. Do not generate the same face with different hair colors.
- Romance is optional in the story, but the visual design should still have Japanese male-audience heroine appeal unless the user requests a non-harem visual direction.

## Compact Japanese Example

### 共通画風

`日本の商業異世界ハーレムアニメの公式キャラクター設定画風。清潔な線画、繊細なセル画調のアニメ塗り、艶のある髪、大きく透明感のある瞳、若々しく華やかな成人キャラクター。正面寄りの自然な立ち姿、両手は空、無地の背景、道具、武器、魔法効果、文字、透かしなし。`

### Character paragraph

`十九歳の人間族の美少女。清楚で控えめな正統派ヒロイン。身長は約百六十センチ、華奢で柔らかな七頭身のアニメ体形。腰まで届く艶やかな栗色の髪を青い細リボンで低い二つ結びにし、宝石のように大きな灰緑色の瞳、小さな鼻と口、細い顎、薄く桃色に染まる頬。白いふくらみ袖のブラウス、青灰色の短い肩掛け、紺色の膝上プリーツスカート、白い脚衣、焦げ茶の短靴。恥ずかしがりだが芯の強さを感じる表情。`

## Release Check

1. Confirm every new major named character has one prompt.
2. Confirm prompt bodies contain no ASCII letters.
3. Confirm every character can be rendered with empty hands and no skill effect.
4. Search for held-prop and symbolic-object wording; move every hit to a scene/cover prompt.
5. Confirm a multi-heroine cast has distinct face, hair silhouette, color palette, costume silhouette, and heroine lane.
6. Run `../scripts/validate-character-prompts.py <prompt-file>` for every saved prompt asset.
