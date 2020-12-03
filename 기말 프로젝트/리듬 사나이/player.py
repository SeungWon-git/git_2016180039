from pico2d import *
import gfw

MOVE_PPS = 300

class Player:
    def __init__(self):
        global time, player, friend, trainer, whistle, shout, number, count1, count2, plus

        player = gfw.image.load('res/Pt-Trainee.png')
        shout = gfw.image.load('res/Shout.png')
        number = gfw.image.load('res/Number.png')
        trainer = gfw.image.load('res/Trainer-back.png')
        whistle = gfw.image.load('res/Whistle.png')
        time = 0
        count1 = 0
        count2 = 0
        plus = False
        
    def update(self):
        global time
        if time == None:
            time = 0
        else:
            time += gfw.delta_time
            
    def draw(self):
        global time, count1, count2, plus
        frame1 = time * 2
        frame1 = int(frame1) % 4
        frame2 = time * 4
        frame2 = int(frame2) % 10
        frame2 = 1800 - frame2 * 200

        player.clip_draw_to_origin(0, frame2, 200, 200, 250, 230, 230, 230)

        player.clip_draw_to_origin(0, frame2, 200, 200, 250 + 150, 240, 230, 230)
        player.clip_draw_to_origin(0, frame2, 200, 200, 250 + 150 * 2, 250, 230, 230)
        player.clip_draw_to_origin(0, frame2, 200, 200, 250 + 150 * 3, 260, 230, 230)

        if frame2 == 1800:
            plus = True
        elif plus == True:
            plus = False
            count1 += 1
            if count1 == 10:
                count1 = 0
                count2 += 1

        if frame2 == 1800 and count2 > 0:
            if count1 != 0:
                shout.clip_draw_to_origin(0, 0, 40, 40, 370, 400, 130, 130)
                number.clip_draw_to_origin((count2 - 1) * 25 + 9 * 25, 0, 25, 25, 390, 440, 50, 50)
                number.clip_draw_to_origin((count1 - 1) * 25, 0, 25, 25, 435, 440, 50, 50)
            else:
                shout.clip_draw_to_origin(0, 0, 40, 40, 370, 400, 130, 130)
                number.clip_draw_to_origin((count2 - 1) * 25 + 9 * 25, 0, 25, 25, 410, 440, 50, 50)

        elif frame2 == 1800 and count1 != 0:
            shout.clip_draw_to_origin(0, 0, 40, 40, 370, 400, 130, 130)
            number.clip_draw_to_origin((count1 - 1) * 25, 0, 25, 25, 410, 440, 50, 50)

        trainer.clip_draw_to_origin(400, 0, 200, 200, 400, 100, 250, 250)

        whistle.clip_draw_to_origin(0, 0, 100, 100, 465, 100, 50, 50)
        whistle.clip_draw_to_origin(0, 0, 100, 100, 465 + 40, 100, 50, 50)
        whistle.clip_draw_to_origin(0, 0, 100, 100, 465 + 80, 100, 50, 50)

    def decreate_life(self):    #return TRUE if dead
            self.life-=1
            return self.life <= 0
                
    def handle_event(self,e):
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_LEFT:
                self.dx-=1
            elif e.key == SDLK_RIGHT:
                self.dx+=1
            elif e.key == SDLK_DOWN:
                self.dy-=1
            elif e.key == SDLK_UP:
                self.dy+=1
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_LEFT:
                self.dx+=1
            elif e.key == SDLK_RIGHT:
                self.dx-=1
            elif e.key == SDLK_DOWN:
                self.dy+=1
            elif e.key == SDLK_UP:
                self.dy-=1
