# 野獣先輩タワーディフェンス ～迫真TD部～ (v1)
- index.html + assets/ : multi-file build (relative paths, works offline)
- yajuu-td-single.html : one-file build, all images embedded as data URLs
- src/template.html + build.py : source; `python3 build.py` regenerates both
- crop.py : makes the crops in assets/ from assets/src/ (the original attachments)

## Image mapping
| Source | Crop(s) | Used for |
|---|---|---|
| #1 face close-up (…ENZ2…jpg) | senpai_face, title_senpai | 先輩砲台 tower icon, 114514砲 icon (red tint + "810" tag), HUD avatar, title hero, win screen, toasts for wave clear/boss kill, cards いいゾ～これ / やりますねぇ / 114514 / 臨時収入 |
| #2 sepia jersey trio (…ER7Z…jpg) | trio_sepia_face, trio_sepia_card | 部室トリオ aura/support tower, cards そうだよ（便乗） / ありますねぇ！ |
| #3 navy Samurai Blue trio (…ESPN…webp) | navy_center_face / navy_left_face / navy_right_face / navy_trio_card | 連射塔 icon (center), enemy 後輩 (left), enemy 俊足後輩 (right), title side image, wave-start toast, cards サムライブルー魂 / おまたせ |
| #4 locker room (…EV64…jpg) | locker_left_face, locker_right_face (faces only) | tanky enemy 部室の主, armored enemy 鉄壁の見学者, card ぬわああん疲れた |
| #5 collar grab (…EWNT…jpg) | collar_face, collar_card | 胸ぐらスネア slow tower, boss-incoming toast, cards 胸ぐら指導 / 見とけよ |
| #6 grimace (…EZHV…jpg) | grimace_face (face only) | 迫真ボス sprite + boss HP bar, crit「ファッ！？」toast, life-lost toasts, game-over screen, card ファッ！？ |

## v2 — スマホ対応 (mobile)
- 縦画面: HUD 2段 → マップ(縦向きに転置して大きく表示) → タワー横並び → 情報バー。横画面スマホ: 細いサイドパネル。PC: 従来レイアウト。
- タップ操作: タワー選択 → マップを2回タップで設置 (1回目はプレビュー+射程表示)。設置済タワーをタップ → 強化/売却。
- ボタンは全て44px以上、セーフエリア対応、横スクロール無し、ピンチ/ダブルタップズーム無効。
- 高DPI キャンバス、マップ/スプライトのキャッシュ、パーティクル上限で 60fps。
- 画面を離れると自動一時停止、設置/被弾時バイブ。PC のキーボードショートカット(1-5 / Space / Esc / P / F)はそのまま。

## v3：汚さ＆戦術マシマシ版

### 新タワー（全10種・ホットキー 1〜9, 0）
| タワー | 役割 | 覚醒A / 覚醒B（Lv4で選択） |
|---|---|---|
| 先輩砲台 | 単体・クリ | 迫真狙い撃ち（クリ+25%・クリ装甲無視） / おかわり連射（2体同時） |
| 連射塔 | 高速連射 | 貫通サムライ（跳弾） / 焦らしブルー（減速） |
| 部室トリオ | 攻撃オーラ | 便乗の輪（範囲・効果UP） / ありますねぇ商法（範囲撃破+3G） |
| 胸ぐら | 範囲減速パルス | ふっとばし指導（ノックバック） / 締め上げ（スタン） |
| 114514砲 | 爆風 | 810焦土（燃える床） / 1919連打（連射） |
| **イキスギ電撃塔** | 連鎖（盾に2倍） | 電撃結婚（+3連鎖） / ビクンビクン（スタン） |
| **くさそうガス** | 毒DoT（装甲・盾無視） | 腐臭爆発（毒死で爆発） / くっさ濃縮（毒x2） |
| **見とけよ狙撃手** | 超射程・HP最大を狙う | 処刑（20%以下即死） / ボス特攻（x2.5） |
| **810銀行** | 経済（ウェーブ収入＋範囲撃破G） | 利息 / 先輩のおごり（ライフ+1/ウェーブ） |
| **迫真バリケード** | 道に置く壁・足止め（壊れる） | トゲトゲ（反撃） / 迫真復活（自己回復） |

### 新しい敵
盾持ち後輩（シールド）・看病する先輩（周囲回復）・分身後輩（死ぬと2体に分裂）・たかり後輩（抜けるとお金を盗む）・覗き見学者（タワーの近くまで透明）。
ボスは5ウェーブ毎にローテ：迫真ボス → 部室の主・真（後輩召喚） → 野獣の眼光（再生シールド＋HP50%で激おこ加速）。

### システム
- **シチュエーション**：開始時に3択でラン全体のルールが変わる（真夏の夜の淫夢／迫真空手部／金欠先輩／ビルの屋上／くさそうな部室／大量発生／普通だな！／バリケード祭り／暴れんなよ…／先輩のおごり）。
- **ドラフト追加カード**：利息、売却全額、2個タダ設置、床ヌルヌル（敵減速）、クリ累積、コンボ中毒、毒伝染、連鎖+2、壁強化、ステルス看破、クリノックバック、狙撃強化、銀行強化 など（max付きは1回まで）。**引き直し**ボタン（30+10×ウェーブG）。
- **コンボ**：連続撃破でコンボ。10コンボ以上で撃破ボーナス、10/25/50/100/200で実況。
- **演出**：画面揺れ、汗しぶき、床のシミ、ボス登場の巨大文字＋フラッシュ、覚醒演出、ランダム勝敗コピー。`prefers-reduced-motion` では揺れを抑制。

### 画像の再利用（色違い）
新キャラは既存の切り抜きを色付けして流用（追加の画像なし）：電撃塔=navy_right_face紫、くさガス=locker_right_face緑、狙撃手=title_senpai青、銀行=trio_sepia_face金、バリケード=collar_faceグレー、114514砲=senpai_face赤、分身後輩=navy_left_face紫、たかり後輩=navy_right_face金、覗き見学者=locker_right_faceグレー、部室の主・真=locker_left_face赤、野獣の眼光=grimace_face紫。
