from pico2d import *

open_canvas()

gra = load_image('grass.png')
ch = load_image('animation_sheet.png')

x=0
frame_index=0
action=0

#게임 루프
while x <800:
    #렌더링 로직
    clear_canvas()  
    gra.draw(400,30)
    ch.clip_draw(frame_index*100,100*action,100,100,x,85) #잘라그리기
    update_canvas() #프론트 버퍼로 업데이트
    
    #게임 로직
    get_events() #이벤트 처리해주어야 화면조작가능
    x+=2
    #frame_index+=1
    #if frame_index>=8:frame_index=0 #분기를 주는건 좋지않다!!
    frame_index = (frame_index + 1) % 8

    if x % 100 == 0:
        action=(action + 1)%4
    delay(0.02) #1초단위

delay(1)

close_canvas()
