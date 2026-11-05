import json,base64,os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
names=['senpai_face','title_senpai','grimace_face','trio_sepia_card','trio_sepia_face','navy_trio_card','navy_center_face','navy_left_face','navy_right_face','locker_left_face','locker_right_face','collar_card','collar_face']
wiki=['wiki/00_見返り美人','wiki/01_トヨタ_センチュリー','wiki/02_目線DB','wiki/03_ンギモッヂイイ！','wiki/04_こ↑こ↓','wiki/05_まずうちさぁ','wiki/06_遠野','wiki/07_四章野獣の眼光','wiki/08_ご満悦先輩','wiki/09_ヤジュ立ち','wiki/10_サッー','wiki/11_したり顔先輩','wiki/12_おっ大丈夫か大丈夫か','wiki/13_小鳥の囀り','wiki/14_やわらかスマホ','wiki/15_野獣ステップ','wiki/16_林檎','wiki/17_世界のトオノ']
tpl=open('src/template.html',encoding='utf-8').read()
rel={n:f'assets/{n}.jpg' for n in names+wiki}
open('index.html','w',encoding='utf-8').write(tpl.replace('/*ASSETS*/',json.dumps(rel)))
emb={n:'data:image/jpeg;base64,'+base64.b64encode(open(f'assets/{n}.jpg','rb').read()).decode() for n in names+wiki}
open('yajuu-td-single.html','w',encoding='utf-8').write(tpl.replace('/*ASSETS*/',json.dumps(emb)))
print('ok')
