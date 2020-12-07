from pico2d import *
import gfw

from stage1 import Stage1
import bg

STATE_IN_GAME,STATE_GAME_OVER = range(2)

def enter(s_num, health):
    gfw.world.init(['bg','stage'])

    global stage, stage_num

    if s_num == 1:
        stage = Stage1(health)
        stage_num = 1
    # elif s_num == 2:
    #     stage = Stage2(health)
    #     stage_num = 2

    gfw.world.add(gfw.layer.stage,stage)

    bg.init(stage_num)
    gfw.world.add(gfw.layer.bg,bg)

    global game_state
    game_state = STATE_IN_GAME

    global success_image, fail_image
    success_image = gfw.image.load('res/Success.png')
    fail_image = gfw.image.load('res/Fail.png')

    global s_music, f_music
    s_music = load_music('res/success.mp3')
    f_music = load_music('res/fail.mp3')

def exit():
    pass

def pause():
    stage.pause()

def resume(health):
    stage.resume(health)

def update():
    global stage,stage_num,game_state,compelete

    if game_state != STATE_IN_GAME: #게임중이 아닐떄 -> 게임오버이거나 등등..
        return

    gfw.world.update()

    if stage.health <= 0:
        game_state = STATE_GAME_OVER
        compelete = False
        f_music.repeat_play()
        print("-- Failed --")
    elif stage.success is True:
        game_state = STATE_GAME_OVER
        compelete = True
        s_music.repeat_play()
        print("-- Success --")
    #elif stage.next is True:
        #if stage_num is 1:
            #stage = Stage2(stage.health+10)
            #stage_num = 2

def draw():
    gfw.world.draw()
    if game_state == STATE_GAME_OVER:
        x = get_canvas_width() // 2
        y = get_canvas_height() // 2
        if compelete is True:
            success_image.draw(x,y)
        else:
            fail_image.draw(x, y)

def handle_event(e):
    global success_image, fail_image,s_music, f_music
    if e.type == SDL_QUIT:
        gfw.quit()
    elif game_state == STATE_GAME_OVER and  (e.type, e.key) == (SDL_KEYDOWN, SDLK_RETURN):
        if compelete:
            s_music.stop()
        else:
            f_music.stop()
        del success_image, fail_image
        del s_music, f_music
        gfw.pop(0)

    stage.handle_event(e)

if __name__=='__main__':
    gfw.run_main()
