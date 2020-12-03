import gfw
from pico2d import *
import game_state

def enter():
    global image, music
    image = load_image('../res/Title.png')
    music = load_music('res/title.mp3')
    music.repeat_play()
    music.set_volume(30)

def update():
    pass

def draw():
    image.clip_draw_to_origin(0, 0, 1495, 1121, -50, 0, 900, 600)

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_RETURN):
        music.stop()
        gfw.push(game_state)


def exit():
    global image,music
    del image
    del music

def pause():
    pass

def resume():
    music.repeat_play()
    music.set_volume(30)
    
if __name__ == '__main__':
    gfw.run_main()
