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
