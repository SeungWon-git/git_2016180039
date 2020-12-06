# version 2020-0927
import time
from pico2d import *
import gfw.world
import gfw.image
import gfw.font

running = True
stack = None
frame_interval = 0.01
delta_time = 0

def quit():
    global running
    running = False

def run(start_state):
    global running, stack
    running = True
    stack = [start_state]

    w,h = 800,600
    if hasattr(start_state, 'canvas_width'): w = start_state.canvas_width
    if hasattr(start_state, 'canvas_height'): h = start_state.canvas_height

    open_canvas(w=w, h=h)

    start_state.enter()

    global delta_time
    last_time = time.time()
    while running:
        # inter-frame (delta) time
        now = time.time()
        delta_time = now - last_time
        last_time = now

        # event handling
        evts = get_events()
        for e in evts:
            stack[-1].handle_event(e)

        # game logic
        stack[-1].update()

        # game rendering
        clear_canvas()
        stack[-1].draw()
        update_canvas()

        delay(frame_interval)

    while (len(stack) > 0):
        stack[-1].exit()
        stack.pop()

    close_canvas()

def change(state,stage,health):
    global stack
    if (len(stack) > 0):
        stack.pop().exit()
    stack.append(state)
    state.enter(stage,health)

def push(state,stage,health):
    global stack
    if (len(stack) > 0):
        stack[-1].pause()
    stack.append(state)
    state.enter(stage,health)

def pop(health):
    global stack
    size = len(stack)
    if size == 1:
        quit()
    elif size > 1:
        # execute the current state's exit function
        stack[-1].exit()
        # remove the current state
        stack.pop() #제일 위에 스택 pop()

        # execute resume function of the previous state
        stack[-1].resume(health)

def run_main():
    import sys
    main_module = sys.modules['__main__']
    run(main_module)
