from pico2d import *

Width,Height=1280,1024
def handle_events():
    global running,x,y
    evts=get_events()
    for e in evts:
        if e.type ==SDL_QUIT:
            running =False
        elif e.type == SDL_MOUSEMOTION:
            x,y= e.x, Height -1 -e.y
        elif e.type == SDL_KEYDOWN and e.key ==SDLK_ESCAPE:
            running = False
            
open_canvas(Width,Height)

gra = load_image('grass.png')
ch = load_image('run_animation.png')

x,y=Width//2,Height//2
frame_index=0
running = True
hide_cursor()

#게임 루프
while running:
    #렌더링 로직
    clear_canvas()  
    gra.draw(Width//2,Height//2)
    ch.clip_draw(frame_index*100,0,100,100,x,y) 
    update_canvas() 
    
    #게임 로직
    handle_events()

    frame_index = (frame_index + 1) % 8
   
delay(1)

close_canvas()
