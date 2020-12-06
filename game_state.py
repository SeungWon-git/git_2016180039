from pico2d import *
import gfw

from stage1 import Stage1
from stage2 import Stage2
import bg

STATE_IN_GAME,STATE_GAME_OVER = range(2)

def enter(s_num, health):
    gfw.world.init(['bg','stage'])
    
    global stage, stage_num

    if s_num == 1:
        stage = Stage1(health)
        stage_num = 1
    elif s_num == 2:
        stage = Stage2(health)
        stage_num = 2

    gfw.world.add(gfw.layer.stage,stage)

    bg.init(stage_num)
    gfw.world.add(gfw.layer.bg,bg)

    global game_state
    game_state = STATE_IN_GAME

    global game_over_image
    game_over_image=gfw.image.load('res/game_over.png')
    
def exit():
    pass

def pause():
    stage.pause()

def resume(health):
    stage.resume(health)

def update():
    global stage,stage_num,game_state
    
    if game_state != STATE_IN_GAME: #게임중이 아닐떄 -> 게임오버이거나 등등..
        return
    
    gfw.world.update()

    if stage.health is 0:
        game_state = STATE_GAME_OVER
    #elif stage.next is True:
        #if stage_num is 1:
            #stage = Stage2(stage.health+10)
            #stage_num = 2
        
def draw():
    gfw.world.draw()
    if game_state == STATE_GAME_OVER:
        x=get_canvas_width()//2
        y=get_canvas_height()//2
        game_over_image.draw(x,y)
    
def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
            
    stage.handle_event(e)

if __name__=='__main__':
    gfw.run_main()
