from pico2d import *
import gfw
from time import sleep

MOVE_PPS = 300

class Stage1:
    def __init__(self,health):
        self.time = 0
        self.health = health

        global whistle_num,progress,intro,correct,punishment
        intro = True
        whistle_num = 3
        progress = 0
        correct = True
        punishment = False

        global intro_player,intro_friend,intro_trainer,trainer_dem,intro_dialog
        intro_player = gfw.image.load('res/Pt-Trainee intro.png')
        intro_friend = gfw.image.load('res/Pt-Trainee intro.png')
        intro_trainer = gfw.image.load('res/Trainer intro.png')
        trainer_dem = gfw.image.load('res/Pt-Trainer.png')
        intro_dialog = [gfw.image.load('res/intro_dialog-1.png'),gfw.image.load('res/intro_dialog-2.png'),\
                        gfw.image.load('res/intro_dialog-3.png'),gfw.image.load('res/intro_dialog-4.png'),\
                        gfw.image.load('res/intro_dialog-5.png'),gfw.image.load('res/intro_dialog-6.png'),\
                        gfw.image.load('res/intro_dialog-7.png'),gfw.image.load('res/intro_dialog-8.png')]

        global pt, pt_sorry,pt_angry, trainer, whistle, shout, number, healthbar_blue,healthbar_red,key,me,Ack,lunge,speak,bell
        pt = gfw.image.load('res/Pt-Trainee.png')
        pt_sorry = gfw.image.load('res/Pt-Trainee-sorry.png')
        pt_angry = gfw.image.load('res/Pt-Trainee-angry.png')
        shout = gfw.image.load('res/Shout.png')
        number = gfw.image.load('res/Number.png')
        trainer = gfw.image.load('res/Trainer-back.png')
        whistle = gfw.image.load('res/Whistle.png')
        lunge = gfw.image.load('res/Lungs.png')
        healthbar_blue = gfw.image.load('res/HealthBar Blue.png')
        healthbar_red = gfw.image.load('res/HealthBar Red.png')
        me = gfw.image.load('res/Me.png')
        key = gfw.image.load('res/Key.png')
        Ack = gfw.image.load('res/악!.png')
        speak = gfw.image.load('res/Speak.png')
        bell = gfw.image.load('res/Bell.png')

        global answer,ask,count1, count2, plus
        answer = False
        ask = False
        count1 = 0
        count2 = 0
        plus = False

        self.intro_x, self.intro_y = -400, 250
        self.intro_size = 250

    def update(self):
        self.time += gfw.delta_time
            
    def draw(self):
        global intro,time,count1, count2, plus, answer ,ask
        time = self.time
        frame1 = time * 2
        frame1 = int(frame1) % 4
        frame2 = time * 4
        frame2 = int(frame2) % 10
        frame2 = 1800 - frame2 * 200

        if intro is True:
            fidx = (time * 2)
            fidx = int(fidx) % 2
            if self.intro_x < 112:
                intro_trainer.clip_draw_to_origin(fidx*200, 0, 200, 200, self.intro_x, self.intro_y, self.intro_size,self.intro_size)
                intro_player.clip_draw_to_origin(fidx*300, 0, 300, 200, 50, 235, 375, 250)
                intro_friend.clip_draw_to_origin(fidx*300, 0, 300, 200, 50 + 150 * 2, 255, 375, 250)
                self.intro_x += 1
            elif self.intro_y > 230:
                intro_trainer.clip_draw_to_origin(fidx*200, 0, 200, 200, self.intro_x, self.intro_y, self.intro_size,self.intro_size)
                intro_player.clip_draw_to_origin(fidx*300, 0, 300, 200, 50, 235, 375, 250)
                intro_friend.clip_draw_to_origin(fidx*300, 0, 300, 200, 50 + 150 * 2, 255, 375, 250)
                self.intro_y -= 2
                self.intro_x += 0.4
            elif self.intro_y > 100:
                intro_player.clip_draw_to_origin(600, 0, 300, 200, 50, 235, 375, 250)
                intro_friend.clip_draw_to_origin(900, 0, 300, 200, 50 + 150 * 2, 255, 375, 250)
                intro_trainer.clip_draw_to_origin(fidx*200, 0, 200, 200, self.intro_x, self.intro_y, self.intro_size,self.intro_size)
                self.intro_y -= 2
                self.intro_x += 0.4
                self.intro_size += 1
            elif self.intro_y == 100:
                intro_player.clip_draw_to_origin(1200, 0, 300, 200, 50, 235, 375, 250)
                intro_friend.clip_draw_to_origin(1200, 0, 300, 200, 50 + 150 * 2, 255, 375, 250)
                intro_trainer.clip_draw_to_origin(400, 0, 200, 200, 142, 100, 316, 316)
                self.intro_y += 0.01
                self.time = 0
            elif self.time <= 0.5:
                    intro_player.clip_draw_to_origin(1200, 0, 300, 200, 50, 235, 375, 250)
                    intro_friend.clip_draw_to_origin(1200, 0, 300, 200, 50 + 150 * 2, 255, 375, 250)
                    intro_trainer.clip_draw_to_origin(400, 0, 200, 200, 142,100,316, 316)
            elif self.time <= 1:
                intro_player.clip_draw_to_origin(1200, 0, 300, 200, 50, 235, 375, 250)
                intro_friend.clip_draw_to_origin(1200, 0, 300, 200, 50 + 150 * 2, 255, 375, 250)
                intro_trainer.clip_draw_to_origin(600, 0, 200, 200, 142, 100, 316, 316)
            elif self.time <= 1.5:
                intro_player.clip_draw_to_origin(1200, 0, 300, 200, 50, 235, 375, 250)
                intro_friend.clip_draw_to_origin(1200, 0, 300, 200, 50 + 150 * 2, 255, 375, 250)
                intro_trainer.clip_draw_to_origin(800, 0, 200, 200, 142, 100, 316, 316)
            elif self.time > 1.5 and self.time < 22.5:
                intro_player.clip_draw_to_origin(1200, 0, 300, 200, 50, 235, 375, 250)
                intro_friend.clip_draw_to_origin(1200, 0, 300, 200, 50 + 150 * 2, 255, 375, 250)
                indx = self.time - 1.5
                indx = int(indx) // 3
                if indx == 4 and answer == False:
                    ask = True
                    self.time = 14
                if indx == 4 and answer == True:
                    shout.clip_draw_to_origin(0, 0, 40, 40, 330, 400, 130, 130)
                    Ack.clip_draw_to_origin(0, 0, 32, 32, 370, 440, 50, 50)
                    pt.clip_draw_to_origin(0, 1800, 200, 200, 50, 235, 250, 250)
                    pt.clip_draw_to_origin(0, 1800, 200, 200, 50 + 132, 235, 250, 250)
                    pt.clip_draw_to_origin(0, 1800, 200, 200, 50 + 300, 255, 250, 250)
                    pt.clip_draw_to_origin(0, 1800, 200, 200, 50 + 300 + 132, 255, 250, 250)
                elif indx >= 5:
                    pt.clip_draw_to_origin(0, 1000, 200, 200, 50, 235, 250, 250)
                    pt.clip_draw_to_origin(0, 1000, 200, 200, 50 + 132, 235, 250, 250)
                    pt.clip_draw_to_origin(0, 1000, 200, 200, 50 + 300, 255, 250, 250)
                    pt.clip_draw_to_origin(0, 1000, 200, 200, 50 + 300 + 132, 255, 250, 250)
                intro_trainer.clip_draw_to_origin(800 + fidx * 200, 0, 200, 200, 142, 100, 316, 316)
                intro_dialog[indx].clip_draw_to_origin( 0, 0, 1371, 487, 350, 300, 430, 150)
                self.x = 200
                self.y = -200
            elif self.time >= 22.5:
                pt.clip_draw_to_origin(0, 1000, 200, 200, 50, 235, 250, 250)
                pt.clip_draw_to_origin(0, 1000, 200, 200, 50 + 132, 235, 250, 250)
                pt.clip_draw_to_origin(0, 1000, 200, 200, 50 + 300, 255, 250, 250)
                pt.clip_draw_to_origin(0, 1000, 200, 200, 50 + 300 + 132, 255, 250, 250)
                trainer.clip_draw_to_origin(0, 0, 200, 200, 142, 100, 316, 316)
                if self.y < 40:
                    self.y += 3
                    trainer_dem.clip_draw_to_origin(0, 1000, 200, 200, self.x, self.y, 325, 325)
                    trainer_dem.clip_draw_to_origin(0, 1000, 200, 200, self.x + 132, self.y, 325, 325)
                    trainer_dem.clip_draw_to_origin(0, 1000, 200, 200, self.x + 264, self.y, 325, 325)
                elif self.x < 300:
                    self.y = 40
                    intro_dialog[7].clip_draw_to_origin(0, 0, 1371, 487, 350, 300, 430, 150)
                    trainer_dem.clip_draw_to_origin(0, 1000, 200, 200, 200, self.y, 325, 325)
                    trainer_dem.clip_draw_to_origin(0, 1000, 200, 200, 200 + 132, self.y, 325, 325)
                    trainer_dem.clip_draw_to_origin(0, 1000, 200, 200, 200 + 264, self.y, 325, 325)
                    self.x += 1
                else:
                    trainer_dem.clip_draw_to_origin(0, frame2, 200, 200, 200, self.y, 325, 325)
                    trainer_dem.clip_draw_to_origin(0, frame2, 200, 200, 200 + 132, self.y, 325, 325)
                    trainer_dem.clip_draw_to_origin(0, frame2, 200, 200, 200 + 264, self.y, 325, 325)



        # pt.clip_draw_to_origin(0, frame2, 200, 200, 50, 235, 250, 250)
        # pt.clip_draw_to_origin(0, frame2, 200, 200, 50 + 132, 235, 250, 250)
        # pt.clip_draw_to_origin(0, frame2, 200, 200, 50 + 300, 255, 250, 250)
        # pt.clip_draw_to_origin(0, frame2, 200, 200, 50 + 300 + 132, 255, 250, 250)
        #
        # if frame2 == 1800:
        #     plus = True
        # elif plus == True:
        #     plus = False
        #     count1 += 1
        #     if count1 == 10:
        #         count1 = 0
        #         count2 += 1
        #
        # if frame2 == 1800 and count2 > 0:
        #     if count1 != 0:
        #         shout.clip_draw_to_origin(0, 0, 40, 40, 330, 400, 130, 130)
        #         number.clip_draw_to_origin((count2 - 1) * 25 + 9 * 25, 0, 25, 25, 350, 440, 50, 50)
        #         number.clip_draw_to_origin((count1 - 1) * 25, 0, 25, 25, 395, 440, 50, 50)
        #     else:
        #         shout.clip_draw_to_origin(0, 0, 40, 40, 330, 400, 130, 130)
        #         number.clip_draw_to_origin((count2 - 1) * 25 + 9 * 25, 0, 25, 25, 370, 440, 50, 50)
        #
        # elif frame2 == 1800 and count1 != 0:
        #     shout.clip_draw_to_origin(0, 0, 40, 40, 330, 400, 130, 130)
        #     number.clip_draw_to_origin((count1 - 1) * 25, 0, 25, 25, 370, 440, 50, 50)
        #
        # trainer.clip_draw_to_origin(400, 0, 200, 200, 142, 100, 316, 316)
        #
        # whistle.clip_draw_to_origin(0, 0, 100, 100, 350, 130, 50, 50)
        # whistle.clip_draw_to_origin(0, 0, 100, 100, 350, 170, 50, 50)
        # whistle.clip_draw_to_origin(0, 0, 100, 100, 350, 210, 50, 50)

        me.clip_draw_to_origin(0, 0, 100, 100, 150, 460, 50, 50)
        bell.clip_draw_to_origin(0, 0, 100, 100, 80, 30, 200, 200)

    def decreate_life(self):    #return TRUE if dead
            self.life-=1
            return self.life <= 0
                
    def handle_event(self,e):
        global answer,ask
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_LEFT:
                self.dx-=1
            elif e.key == SDLK_RIGHT:
                self.dx+=1
            elif e.key == SDLK_DOWN:
                self.dy-=1
            elif e.key == SDLK_UP:
                self.dy+=1
            elif e.key == SDLK_RETURN and ask == True:
                answer = True
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_LEFT:
                self.dx+=1
            elif e.key == SDLK_RIGHT:
                self.dx-=1
            elif e.key == SDLK_DOWN:
                self.dy+=1
            elif e.key == SDLK_UP:
                self.dy-=1

