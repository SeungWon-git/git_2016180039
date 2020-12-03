from pico2d import *
import gfw

from stage1 import Stage1
import bg

STATE_IN_GAME,STATE_GAME_OVER = range(2)

def enter():
    gfw.world.init(['bg','stage'])
    
    global stage,stage_num
    stage = Stage1(100)
    stage_num = 1
    gfw.world.add(gfw.layer.stage,stage)

    bg.init(stage_num)
    gfw.world.add(gfw.layer.bg,bg)

    global game_state
    game_state = STATE_IN_GAME

    global game_over_image
    game_over_image=gfw.image.load('res/game_over.png')
    
def exit():
    pass

def update():
    global stage,stage_num,game_state
    
    if game_state != STATE_IN_GAME:
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
    global stage
    if e.type == SDL_QUIT:
        gfw.quit()
            
    stage.handle_event(e)

if __name__=='__main__':
    gfw.run_main()
        
