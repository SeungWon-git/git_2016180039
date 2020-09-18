from pico2d import *

def handle_events():
    global running,x,dx
    evts=get_events()
    for e in evts:
        if e.type ==SDL_QUIT:
            running =False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
            elif e.key == SDLK_LEFT:
                dx -= 1
            elif e.key == SDLK_RIGHT:
                dx += 1
                
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_LEFT:
                dx += 1
            elif e.key == SDLK_RIGHT:
                dx -= 1
                
open_canvas()

gra = load_image('grass.png')
ch = load_image('run_animation.png')

x=400
dx=0
frame_index=0
running = True
#게임 루프
while running:
    #렌더링 로직
    clear_canvas()  
    gra.draw(400,30)
    ch.clip_draw(frame_index*100,0,100,100,x,85) 
    update_canvas() 
    
    #게임 로직
    handle_events()

    x+=dx
    delay(0.01) 
    frame_index = (frame_index + 1) % 8
   
delay(1)

close_canvas()
