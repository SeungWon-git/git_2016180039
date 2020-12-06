from pico2d import *
import gfw

def init(stage):
    global bg,time
    time = 0

    if stage is 1:
        bg = gfw.image.load('res/stage1/BackGround.png')
    else:
        bg = gfw.image.load('res/Me_shout.png')

def draw():
    global time
    frame = time * 2
    frame = int(frame) % 4

    bg.clip_draw_to_origin(0, frame * 300, 500, 300,0,0,get_canvas_width(),get_canvas_height())

def update():
    global time
    if time == None:
        time = 0
    else:
        time += gfw.delta_time

