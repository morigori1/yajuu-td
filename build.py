import json,base64,os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
names=['senpai_face','title_senpai','grimace_face','trio_sepia_card','trio_sepia_face','navy_trio_card','navy_center_face','navy_left_face','navy_right_face','locker_left_face','locker_right_face','collar_card','collar_face']
tpl=open('src/template.html',encoding='utf-8').read()
rel={n:f'assets/{n}.jpg' for n in names}
open('index.html','w',encoding='utf-8').write(tpl.replace('/*ASSETS*/',json.dumps(rel)))
emb={n:'data:image/jpeg;base64,'+base64.b64encode(open(f'assets/{n}.jpg','rb').read()).decode() for n in names}
open('yajuu-td-single.html','w',encoding='utf-8').write(tpl.replace('/*ASSETS*/',json.dumps(emb)))
print('ok')
