from PIL import Image, ImageOps
S='src/'
def c(f,box,out,size):
    im=Image.open(S+f).convert('RGB').crop(box)
    im=im.resize(size,Image.LANCZOS) if size else im
    im.save(out,quality=86); return im
# icons 128x128 (faces)
c('01M6M9ENZ2M8FMSQTJ31WW8649.jpg',(105,70,375,340),'senpai_face.jpg',(128,128))
c('01M6M9ENZ2M8FMSQTJ31WW8649.jpg',(0,0,500,500),'title_senpai.jpg',(360,360))
c('01M6M9EZHVFX4JS1Z333QS1VEM.jpg',(75,5,335,262),'grimace_face.jpg',(128,128))
c('01M6M9ER7ZRTCV2TBNNK9HJK73.jpg',(70,45,410,320),'trio_sepia_card.jpg',(320,260))
c('01M6M9ER7ZRTCV2TBNNK9HJK73.jpg',(195,80,285,170),'trio_sepia_face.jpg',(128,128))
c('01M6M9ESPNHFZMYJJKMXFCN7PC.webp',(0,20,442,332),'navy_trio_card.jpg',(320,226))
c('01M6M9ESPNHFZMYJJKMXFCN7PC.webp',(225,45,315,135),'navy_center_face.jpg',(128,128))
c('01M6M9ESPNHFZMYJJKMXFCN7PC.webp',(28,50,113,135),'navy_left_face.jpg',(128,128))
c('01M6M9ESPNHFZMYJJKMXFCN7PC.webp',(298,55,368,125),'navy_right_face.jpg',(128,128))
c('01M6M9EV642XY42QNN27HRXPW9.jpg',(90,100,170,180),'locker_left_face.jpg',(128,128))
c('01M6M9EV642XY42QNN27HRXPW9.jpg',(282,112,356,186),'locker_right_face.jpg',(128,128))
c('01M6M9EWNTH6SEE0JPD2M26XK9.jpg',(0,0,309,187),'collar_card.jpg',(320,194))
c('01M6M9EWNTH6SEE0JPD2M26XK9.jpg',(110,0,190,80),'collar_face.jpg',(128,128))
