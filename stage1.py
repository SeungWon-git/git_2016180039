from pico2d import *
import gfw
import random
import game_state

class Stage1:
    def __init__(self,health):
        print("-- Stage1 --")
        self.health = health

        global frame, answer, ask, count1, count2, count_up
        frame = 1800
        answer = False
        ask = False
        count1 = 0
        count2 = 0
        count_up = False

        self.intro_x, self.intro_y = -400, 250
        self.intro_size = 250

        global whistle_num, progress, intro, practice, correct, time, key, goal, p_key,\
            me_shout_time, speed, check, shout_randidx, last_speak, ask_, m_intro, time_, answer_time, speed_check
        intro = False
        practice = False
        m_intro = False # False로 해놔야지 인트로 훈련에서도 타이밍 체크함
        whistle_num = 5
        progress = 0
        correct = True
        time = 10
        key = -1
        goal = 3
        p_key = 0
        me_shout_time = 0
        speed = 4
        check = False # 반복 체크를 막기위해 -> 프레임으로 체크하다보니 중복발생
        shout_randidx = 0
        last_speak = False
        ask_ = False
        time_ = get_time()
        answer_time = -1
        speed_check = False

        #대사 이미지
        global intro_player, intro_friend, intro_trainer, trainer_dem, intro_dialog, m_intro_dialog
        intro_player = gfw.image.load('res/stage1/Pt-Trainee intro.png')
        intro_friend = gfw.image.load('res/stage1/Pt-Trainee intro.png')
        intro_trainer = gfw.image.load('res/stage1/Trainer intro.png')
        trainer_dem = gfw.image.load('res/stage1/Pt-Trainer.png')
        intro_dialog = [gfw.image.load('res/stage1/intro_dialog-1.png'),gfw.image.load('res/stage1/intro_dialog-2.png'),\
                        gfw.image.load('res/stage1/intro_dialog-3.png'),gfw.image.load('res/stage1/intro_dialog-4.png'),\
                        gfw.image.load('res/stage1/intro_dialog-5.png'),gfw.image.load('res/stage1/intro_dialog-6.png'),\
                        gfw.image.load('res/stage1/intro_dialog-7.png'),gfw.image.load('res/stage1/intro_dialog-8.png'),\
                        gfw.image.load('res/stage1/intro_dialog-9.png')]
        m_intro_dialog = [gfw.image.load('res/stage1/dialog_lastspeak.png'),gfw.image.load('res/stage1/dialog_gw.png'),\
                          gfw.image.load('res/stage1/dialog_lastp1.png'),gfw.image.load('res/stage1/dialog_lastp2.png'),\
                          gfw.image.load('res/stage1/dialog_lastp3.png')]

        #이미지
        global pt, pt_sorry,pt_angry, trainer, whistle, shout, number, \
            qwer, me, Ack, speak, bell, me_shout, me_key
        pt = gfw.image.load('res/stage1/Pt-Trainee.png')
        pt_sorry = gfw.image.load('res/stage1/Pt-Trainee-sorry.png')
        pt_angry = gfw.image.load('res/stage1/Pt-Trainee-angry.png')
        shout = gfw.image.load('res/Shout.png')
        me_shout = gfw.image.load('res/Me_shout.png')
        number = gfw.image.load('res/Number.png')
        trainer = gfw.image.load('res/stage1/Trainer-back.png')
        whistle = gfw.image.load('res/Whistle.png')
        me = gfw.image.load('res/Me.png')
        qwer = gfw.image.load('res/Key.png')
        Ack = gfw.image.load('res/악!.png')
        speak = gfw.image.load('res/Speak.png')
        bell = gfw.image.load('res/Bell.png')
        me_key = gfw.image.load('res/Keyboard.png')

        #배경음악
        global intro_music, main_music
        intro_music = load_music('res/stage1/stage1-intro.mp3')
        main_music  = load_music('res/stage1/stage1-main.mp3')

        #효과음
        global BBick1, BBick2, BBick_w, BBick_p
        BBick1 = load_wav('res/삑.wav')
        BBick1.set_volume(20)
        BBick2 = load_wav('res/삐~삑.wav')
        BBick2.set_volume(20)
        BBick_w = load_wav('res/삑!삑!(경고).wav')
        BBick_p = load_wav('res/삑~(열외).wav')
        BBick_p.set_volume(30)

    def pause(self):
        main_music.pause()

    def resume(self, health):
        main_music.resume()
        self.health = health
        print("Stage1 resumed\nprogress: ",progress)

    def exit(self):
        global intro_player, intro_friend, intro_trainer, trainer_dem, intro_dialog, m_intro_dialog, \
            pt, pt_sorry, pt_angry, trainer, whistle, shout, number, qwer, me, Ack, speak, bell, me_shout, me_key, \
            intro_music, main_music, BBick1, BBick2, BBick_w, BBick_p
        del intro_player, intro_friend, intro_trainer, trainer_dem, intro_dialog, m_intro_dialog, \
            pt, pt_sorry, pt_angry, trainer, whistle, shout, number, qwer, me, Ack, speak, bell, me_shout, me_key
        del intro_music, main_music, BBick1, BBick2, BBick_w, BBick_p

    def update(self):
        global time, frame, frame_, speed, check, correct, p_key, key, practice,\
            last_speak, goal, progress, count1, count2, intro, whistle_num, time_, m_intro, speed_check
        time += gfw.delta_time
        frame_ = round(time * speed,1)
        frame = int(time * speed) % 10
        frame = 1800 - frame * 200

        if frame == 1800 and round(frame_ - int(frame_),2) == 0.9 and progress != 0 and not intro:
            self.Correct_Check() # 너무 늦게 클릭 확인

        if frame == 600 and round(frame_ - int(frame_),2) == 0.1 and progress != 0:
            if speed_check == False:
                speed_check = True
                self.Speed_Up()  # 속도 증가 -> 1번에 0.025씩

        if frame == 1600 and round(frame_ - int(frame_),2) == 0.9:  #참고 - 프레임이 1600일때는 키보드 입력 안됨
            #초기화
            check = False
            correct = True
            p_key = 0
            key = -1
            speed_check = False

        # 종료 -> 초기화
        if progress == goal + 1 and round(frame_ - int(frame_),2) == 0.9:
            if last_speak == True and intro == False and practice == False: #마지막 구호 말했을때
                goal += 5   #처음부터 +5만큼 다시하기
                count1 = 0
                count2 = 0
                progress = 0
                time = 0
                speed = 4
                whistle_num = 5
                last_speak = False
            elif intro == False and practice == True: #연습끝
                practice = False
                progress = 0
                goal = 15
                count1 = 0
                count2 = 0
                time = 0
                speed = 4
                whistle_num = 5
                time_ = get_time()
                m_intro = True
            else: #스테이지1 클리어
                print("Stage1 Clear!\nhealth: ",self.health)
                gfw.pop(self.health)

    def draw(self):
        global intro, time, frame, count1, count2, count_up, answer ,ask, key, last_time, progress, speed,\
            goal, practice , me_shout_time, me_shout_randidx, check, last_speak, whistle_num,\
            time_, m_intro, ask_, answer_time

        #intro
        if intro is True:
            fidx = (time * 2)
            fidx = int(fidx) % 2
            if self.intro_x < 112: #웅성웅성
                intro_trainer.clip_draw_to_origin(fidx*200, 0, 200, 200, self.intro_x, self.intro_y, self.intro_size,self.intro_size)
                intro_player.clip_draw_to_origin(fidx*300, 0, 300, 200, 50, 235, 375, 250)
                intro_friend.clip_draw_to_origin(fidx*300, 0, 300, 200, 50 + 150 * 2, 255, 375, 250)
                self.intro_x += 1
            elif self.intro_y > 230: #조교 어깨빵
                intro_trainer.clip_draw_to_origin(fidx*200, 0, 200, 200, self.intro_x, self.intro_y, self.intro_size,self.intro_size)
                intro_player.clip_draw_to_origin(fidx*300, 0, 300, 200, 50, 235, 375, 250)
                intro_friend.clip_draw_to_origin(fidx*300, 0, 300, 200, 50 + 150 * 2, 255, 375, 250)
                self.intro_y -= 2
                self.intro_x += 0.4
                intro_music.repeat_play()
            elif self.intro_y > 100: #조교 자리로 가는 중
                intro_player.clip_draw_to_origin(600, 0, 300, 200, 50, 235, 375, 250)
                intro_friend.clip_draw_to_origin(900, 0, 300, 200, 50 + 150 * 2, 255, 375, 250)
                intro_trainer.clip_draw_to_origin(fidx*200, 0, 200, 200, self.intro_x, self.intro_y, self.intro_size,self.intro_size)
                self.intro_y -= 2
                self.intro_x += 0.4
                self.intro_size += 1
            elif self.intro_y == 100: #조교 자리 도착
                intro_player.clip_draw_to_origin(1200, 0, 300, 200, 50, 235, 375, 250)
                intro_friend.clip_draw_to_origin(1200, 0, 300, 200, 50 + 150 * 2, 255, 375, 250)
                intro_trainer.clip_draw_to_origin(400, 0, 200, 200, 142, 100, 316, 316)
                self.intro_y += 0.01
                time = 0
            elif time <= 0.5: #조교 잠시 정지
                    intro_player.clip_draw_to_origin(1200, 0, 300, 200, 50, 235, 375, 250)
                    intro_friend.clip_draw_to_origin(1200, 0, 300, 200, 50 + 150 * 2, 255, 375, 250)
                    intro_trainer.clip_draw_to_origin(400, 0, 200, 200, 142,100,316, 316)
            elif time <= 1: #조교 뒤로 도는 중
                intro_player.clip_draw_to_origin(1200, 0, 300, 200, 50, 235, 375, 250)
                intro_friend.clip_draw_to_origin(1200, 0, 300, 200, 50 + 150 * 2, 255, 375, 250)
                intro_trainer.clip_draw_to_origin(600, 0, 200, 200, 142, 100, 316, 316)
            elif time <= 1.5: #조교 완전히 뒤돌음
                intro_player.clip_draw_to_origin(1200, 0, 300, 200, 50, 235, 375, 250)
                intro_friend.clip_draw_to_origin(1200, 0, 300, 200, 50 + 150 * 2, 255, 375, 250)
                intro_trainer.clip_draw_to_origin(800, 0, 200, 200, 142, 100, 316, 316)
            elif time > 1.5 and time < 22.5: #조교 설명
                intro_player.clip_draw_to_origin(1200, 0, 300, 200, 50, 235, 375, 250)
                intro_friend.clip_draw_to_origin(1200, 0, 300, 200, 50 + 150 * 2, 255, 375, 250)
                indx = time - 1.5
                indx = int(indx) // 3
                if indx == 4 and answer == False: #조교 질문
                    ask = True
                    time = 14
                if indx == 4 and answer == True: #답변받음
                    shout.clip_draw_to_origin(0, 0, 40, 40, 330, 400, 130, 130)
                    Ack.clip_draw_to_origin(0, 0, 32, 32, 370, 440, 50, 50)
                    pt.clip_draw_to_origin(0, 1800, 200, 200, 50, 235, 250, 250)
                    pt.clip_draw_to_origin(0, 1800, 200, 200, 50 + 132, 235, 250, 250)
                    pt.clip_draw_to_origin(0, 1800, 200, 200, 50 + 300, 255, 250, 250)
                    pt.clip_draw_to_origin(0, 1800, 200, 200, 50 + 300 + 132, 255, 250, 250)
                elif indx >= 5: #답변후 훈련생 표정 진지
                    pt.clip_draw_to_origin(0, 1000, 200, 200, 50, 235, 250, 250)
                    pt.clip_draw_to_origin(0, 1000, 200, 200, 50 + 132, 235, 250, 250)
                    pt.clip_draw_to_origin(0, 1000, 200, 200, 50 + 300, 255, 250, 250)
                    pt.clip_draw_to_origin(0, 1000, 200, 200, 50 + 300 + 132, 255, 250, 250)

                intro_trainer.clip_draw_to_origin(800 + fidx * 200, 0, 200, 200, 142, 100, 316, 316)
                intro_dialog[indx].clip_draw_to_origin( 0, 0, 1371, 487, 350, 300, 430, 150)
                self.x = 200
                self.y = -200
            elif time >= 22.5: #시범조교 위치로
                pt.clip_draw_to_origin(0, 1000, 200, 200, 50, 235, 250, 250)
                pt.clip_draw_to_origin(0, 1000, 200, 200, 50 + 132, 235, 250, 250)
                pt.clip_draw_to_origin(0, 1000, 200, 200, 50 + 300, 255, 250, 250)
                pt.clip_draw_to_origin(0, 1000, 200, 200, 50 + 300 + 132, 255, 250, 250)
                trainer.clip_draw_to_origin(0, 0, 200, 200, 142, 100, 316, 316)
                if self.y < 40 and count2 == 0: #위치로 가는중
                    self.y += 3
                    trainer_dem.clip_draw_to_origin(0, 1000, 200, 200, self.x, self.y, 325, 325)
                    trainer_dem.clip_draw_to_origin(0, 1000, 200, 200, self.x + 132, self.y, 325, 325)
                    trainer_dem.clip_draw_to_origin(0, 1000, 200, 200, self.x + 264, self.y, 325, 325)
                    intro_music.stop()
                elif self.x < 300: #위치 도착 준비시작멘트
                    self.y = 40
                    intro_dialog[7].clip_draw_to_origin(0, 0, 1371, 487, 350, 300, 430, 150)
                    trainer_dem.clip_draw_to_origin(0, 1000, 200, 200, 200, self.y, 325, 325)
                    trainer_dem.clip_draw_to_origin(0, 1000, 200, 200, 200 + 132, self.y, 325, 325)
                    trainer_dem.clip_draw_to_origin(0, 1000, 200, 200, 200 + 264, self.y, 325, 325)
                    self.x += 1
                    time = 30
                    if self.x == 300:
                        main_music.repeat_play()
                elif count2 <= 1:  # 시범중
                    self.Count_Up()
                    self.WhistleSound()

                    if count2 == 1 and count_up == True:  # 10번째 -> 주의할건 실제 count는 11인 상태이다.
                        count2 = 2
                        trainer_dem.clip_draw_to_origin(0, 1000, 200, 200, 200, 40, 325, 325)
                        trainer_dem.clip_draw_to_origin(0, 1000, 200, 200, 200 + 132, 40, 325, 325)
                        trainer_dem.clip_draw_to_origin(0, 1000, 200, 200, 200 + 264, 40, 325, 325)
                    else:
                        trainer_dem.clip_draw_to_origin(0, frame, 200, 200, 200, 40, 325, 325)
                        trainer_dem.clip_draw_to_origin(0, frame, 200, 200, 200 + 132, 40, 325, 325)
                        trainer_dem.clip_draw_to_origin(0, frame, 200, 200, 200 + 264, 40, 325, 325)

                    if progress == 0 and frame == 1800: #시작시 입 안벌리게
                        trainer_dem.clip_draw_to_origin(0, 1000, 200, 200, 200, 40, 325, 325)
                        trainer_dem.clip_draw_to_origin(0, 1000, 200, 200, 200 + 132, 40, 325, 325)
                        trainer_dem.clip_draw_to_origin(0, 1000, 200, 200, 200 + 264, 40, 325, 325)

                    if frame == 1800 and count1 != 0:  # 카운팅이 1~9일때
                        speak.clip_draw_to_origin(0, 0, 40, 40, 680, 300, 130, 130)
                        number.clip_draw_to_origin((count1 - 1) * 25, 0, 25, 25, 720, 350, 50, 50)

                    if frame == 200:  # 키 입력 제시
                        trainer.clip_draw_to_origin(200, 0, 200, 200, 142, 100, 316, 316)
                        trainer_dem.clip_draw_to_origin(0, frame, 200, 200, 200, 40, 325, 325)
                        self.RandomKey()
                        qwer.clip_draw_to_origin((key - 1) * 25, 0, 25, 25, 175, 320, 50, 50)
                    else:
                        key = -1  # 랜덤키 생성을 함번씩만 하기위해서
                elif count2 == 2:
                    last_time = get_time()
                    count2 += 1
                    trainer_dem.clip_draw_to_origin(0, 1000, 200, 200, 200, 40, 325, 325)
                    trainer_dem.clip_draw_to_origin(0, 1000, 200, 200, 200 + 132, 40, 325, 325)
                    trainer_dem.clip_draw_to_origin(0, 1000, 200, 200, 200 + 264, 40, 325, 325)
                elif get_time() - last_time < 2:  # 잠시 정지
                    trainer_dem.clip_draw_to_origin(0, 1000, 200, 200, 200, 40, 325, 325)
                    trainer_dem.clip_draw_to_origin(0, 1000, 200, 200, 200 + 132, 40, 325, 325)
                    trainer_dem.clip_draw_to_origin(0, 1000, 200, 200, 200 + 264, 40, 325, 325)
                elif get_time() - last_time < 6:  # 훈련 준비
                    self.y -= 1.5
                    intro_dialog[8].clip_draw_to_origin(0, 0, 1371, 487, 350, 300, 430, 150)
                    trainer_dem.clip_draw_to_origin(0, 1000, 200, 200, 200, self.y, 325, 325)
                    trainer_dem.clip_draw_to_origin(0, 1000, 200, 200, 200 + 132, self.y, 325, 325)
                    trainer_dem.clip_draw_to_origin(0, 1000, 200, 200, 200 + 264, self.y, 325, 325)
                else:  # 인트로 끝
                    intro = False
                    progress = 0
                    goal = 10
                    count1 = 0
                    count2 = 0
                    time = 0
                    speed = 4
        #practice
        elif practice is True:
            if frame == 200:  # 키 입력 제시
                self.RandomKey()

            if get_time() - me_shout_time < 0.2 and frame != 1600:
                self.Me_Click()

            me.clip_draw_to_origin(0, 0, 100, 100, 150, 460, 50, 50)
            if correct == True:
                pt.clip_draw_to_origin(0, frame, 200, 200, 50, 235, 250, 250)

                pt.clip_draw_to_origin(0, frame, 200, 200, 50 + 132, 235, 250, 250)
                pt.clip_draw_to_origin(0, frame, 200, 200, 50 + 300, 255, 250, 250)
                pt.clip_draw_to_origin(0, frame, 200, 200, 50 + 300 + 132, 255, 250, 250)
            else: #틀렸을때
                pt_sorry.clip_draw_to_origin(0, frame, 200, 200, 50, 235, 250, 250)

                pt_angry.clip_draw_to_origin(0, frame, 200, 200, 50 + 132, 235, 250, 250)
                pt_angry.clip_draw_to_origin(0, frame, 200, 200, 50 + 300, 255, 250, 250)
                pt_angry.clip_draw_to_origin(0, frame, 200, 200, 50 + 300 + 132, 255, 250, 250)

            if correct == False: #틀렸을때
                trainer.clip_draw_to_origin(400, 0, 200, 200, 142, 100, 316, 316)
            elif frame == 200: #키 제시
                trainer.clip_draw_to_origin(200, 0, 200, 200, 142, 100, 316, 316)
                qwer.clip_draw_to_origin((key - 1) * 25, 0, 25, 25, 175, 320, 50, 50)
            else:
                trainer.clip_draw_to_origin(0, 0, 200, 200, 142, 100, 316, 316)

            self.Count_Up()
            self.WhistleSound()
            self.NumberCount()

            if whistle_num == 0:
                whistle_num = 1

            for i in range(whistle_num):
                whistle.clip_draw_to_origin(0, 0, 100, 100, 350, 130 + i*40, 50, 50)
        #본 게임 준비
        elif m_intro == True:
            fidx_ = (time * 2)
            fidx_ = int(fidx_) % 2
            if get_time() - time_ < 3:
                if last_speak == True: #마지막 구호 넣지 말라 경고
                    pt_sorry.clip_draw_to_origin(0, 1000, 200, 200, 50, 235, 250, 250)
                    pt_angry.clip_draw_to_origin(0, 1000, 200, 200, 50 + 132, 235, 250, 250)
                    pt_angry.clip_draw_to_origin(0, 1000, 200, 200, 50 + 300, 255, 250, 250)
                    pt_angry.clip_draw_to_origin(0, 1000, 200, 200, 50 + 300 + 132, 255, 250, 250)

                    trainer.clip_draw_to_origin(400, 0, 200, 200, 142, 100, 316, 316)
                    m_intro_dialog[0].clip_draw_to_origin(0, 0, 1371, 487, 350, 300, 430, 150)
                else:   #칭찬
                    pt.clip_draw_to_origin(0, 1000, 200, 200, 50, 235, 250, 250)

                    pt.clip_draw_to_origin(0, 1000, 200, 200, 50 + 132, 235, 250, 250)
                    pt.clip_draw_to_origin(0, 1000, 200, 200, 50 + 300, 255, 250, 250)
                    pt.clip_draw_to_origin(0, 1000, 200, 200, 50 + 300 + 132, 255, 250, 250)

                    intro_trainer.clip_draw_to_origin(800+200*fidx_ , 0, 200, 200, 142, 100, 316, 316)
                    m_intro_dialog[1].clip_draw_to_origin(0, 0, 1371, 487, 350, 300, 430, 150)
            elif get_time() - time_ < 6:
                pt.clip_draw_to_origin(0, 1000, 200, 200, 50, 235, 250, 250)
                pt.clip_draw_to_origin(0, 1000, 200, 200, 50 + 132, 235, 250, 250)
                pt.clip_draw_to_origin(0, 1000, 200, 200, 50 + 300, 255, 250, 250)
                pt.clip_draw_to_origin(0, 1000, 200, 200, 50 + 300 + 132, 255, 250, 250)

                intro_trainer.clip_draw_to_origin(800 + 200 * fidx_, 0, 200, 200, 142, 100, 316, 316)
                m_intro_dialog[2].clip_draw_to_origin(0, 0, 1371, 487, 350, 300, 430, 150)
            elif answer_time < 0:
                ask_ = True

                pt.clip_draw_to_origin(0, 1000, 200, 200, 50, 235, 250, 250)
                pt.clip_draw_to_origin(0, 1000, 200, 200, 50 + 132, 235, 250, 250)
                pt.clip_draw_to_origin(0, 1000, 200, 200, 50 + 300, 255, 250, 250)
                pt.clip_draw_to_origin(0, 1000, 200, 200, 50 + 300 + 132, 255, 250, 250)

                intro_trainer.clip_draw_to_origin(800 + 200 * fidx_, 0, 200, 200, 142, 100, 316, 316)
                m_intro_dialog[3].clip_draw_to_origin(0, 0, 1371, 487, 350, 300, 430, 150)
            elif get_time() - answer_time < 3:
                shout.clip_draw_to_origin(0, 0, 40, 40, 330, 400, 130, 130)
                Ack.clip_draw_to_origin(0, 0, 32, 32, 370, 440, 50, 50)
                pt.clip_draw_to_origin(0, 1800, 200, 200, 50, 235, 250, 250)
                pt.clip_draw_to_origin(0, 1800, 200, 200, 50 + 132, 235, 250, 250)
                pt.clip_draw_to_origin(0, 1800, 200, 200, 50 + 300, 255, 250, 250)
                pt.clip_draw_to_origin(0, 1800, 200, 200, 50 + 300 + 132, 255, 250, 250)

                intro_trainer.clip_draw_to_origin(800 + 200 * fidx_, 0, 200, 200, 142, 100, 316, 316)
                m_intro_dialog[3].clip_draw_to_origin(0, 0, 1371, 487, 350, 300, 430, 150)
            elif get_time() - answer_time < 6:
                pt.clip_draw_to_origin(0, 1000, 200, 200, 50, 235, 250, 250)
                pt.clip_draw_to_origin(0, 1000, 200, 200, 50 + 132, 235, 250, 250)
                pt.clip_draw_to_origin(0, 1000, 200, 200, 50 + 300, 255, 250, 250)
                pt.clip_draw_to_origin(0, 1000, 200, 200, 50 + 300 + 132, 255, 250, 250)

                intro_trainer.clip_draw_to_origin(800 + 200 * fidx_, 0, 200, 200, 142, 100, 316, 316)
                m_intro_dialog[4].clip_draw_to_origin(0, 0, 1371, 487, 350, 300, 430, 150)
            else: #중간 인트로 끝 -> 시간 초기화
                pt.clip_draw_to_origin(0, 1000, 200, 200, 50, 235, 250, 250)
                pt.clip_draw_to_origin(0, 1000, 200, 200, 50 + 132, 235, 250, 250)
                pt.clip_draw_to_origin(0, 1000, 200, 200, 50 + 300, 255, 250, 250)
                pt.clip_draw_to_origin(0, 1000, 200, 200, 50 + 300 + 132, 255, 250, 250)

                intro_trainer.clip_draw_to_origin(800 + 200 * fidx_, 0, 200, 200, 142, 100, 316, 316)
                m_intro_dialog[4].clip_draw_to_origin(0, 0, 1371, 487, 350, 300, 430, 150)

                m_intro = False
                time = 0
                last_speak = False
        #game start
        else:
            if frame == 200:  # 키 입력 제시
                self.RandomKey()

            if get_time() - me_shout_time < 0.2 and frame != 1600:
                self.Me_Click()

            me.clip_draw_to_origin(0, 0, 100, 100, 150, 460, 50, 50)
            if correct == True:
                pt.clip_draw_to_origin(0, frame, 200, 200, 50, 235, 250, 250)

                pt.clip_draw_to_origin(0, frame, 200, 200, 50 + 132, 235, 250, 250)
                pt.clip_draw_to_origin(0, frame, 200, 200, 50 + 300, 255, 250, 250)
                pt.clip_draw_to_origin(0, frame, 200, 200, 50 + 300 + 132, 255, 250, 250)
            else: #틀렸을때
                pt_sorry.clip_draw_to_origin(0, frame, 200, 200, 50, 235, 250, 250)

                pt_angry.clip_draw_to_origin(0, frame, 200, 200, 50 + 132, 235, 250, 250)
                pt_angry.clip_draw_to_origin(0, frame, 200, 200, 50 + 300, 255, 250, 250)
                pt_angry.clip_draw_to_origin(0, frame, 200, 200, 50 + 300 + 132, 255, 250, 250)

            if whistle_num == 0: #열외
                trainer.clip_draw_to_origin(600, 0, 200, 200, 142, 100, 316, 316)
            elif correct == False: #틀렸을때
                trainer.clip_draw_to_origin(400, 0, 200, 200, 142, 100, 316, 316)
            elif frame == 200: #키 제시
                trainer.clip_draw_to_origin(200, 0, 200, 200, 142, 100, 316, 316)
                qwer.clip_draw_to_origin((key - 1) * 25, 0, 25, 25, 175, 320, 50, 50)
            else:
                trainer.clip_draw_to_origin(0, 0, 200, 200, 142, 100, 316, 316)

            self.Count_Up()
            self.WhistleSound()
            self.NumberCount()

            for i in range(whistle_num):
                whistle.clip_draw_to_origin(0, 0, 100, 100, 350, 130 + i*40, 50, 50)

        bell.clip_draw_to_origin(0, 0, 100, 100, 80, 30, 200, 200)

    def WhistleSound(self):
        if correct or intro == True:
            if frame == 1400 and round(frame_ - int(frame_),2) == 0.9:
                BBick1.play()
            elif frame == 1000 and round(frame_ - int(frame_),2) == 0.9:
                BBick2.play()

    def Count_Up(self):
        global count1, count2, count_up, frame, progress
        if frame == 1800:
            count_up = True
        elif count_up == True:
            count_up = False
            count1 += 1
            progress += 1
            if count1 == 10:
                count1 = 0
                count2 += 1

    def Speed_Up(self): #속도 증가 -> 1번에 0.025씩
        global speed
        speed += 0.025
        speed = round(speed,3)
        if speed >= 5.0: #속도 최대치 = 5
            speed = 5

    def RandomKey(self):
        global key
        if key == -1:
            key = random.randint(1,4)

    def NumberCount(self):
        global frame, count1, count2, shout_randidx
        if frame == 1600:
            shout_randidx = random.randint(0,2)
        if progress != goal:
            if frame == 1800 and count2 > 0:  # 2자리수 카운팅
                shout.clip_draw_to_origin(shout_randidx * 40, 0, 40, 40, 330, 400, 130, 130)
                if count1 != 0:  # 1의 자리가 0이 아닐때 -> 1,2자리수 모두 표시
                    number.clip_draw_to_origin((count2 - 1) * 25 + 9 * 25, 0, 25, 25, 350, 440, 50, 50)
                    number.clip_draw_to_origin((count1 - 1) * 25, 0, 25, 25, 395, 440, 50, 50)
                else:  # 1의 자리수가 0일때 -> 2의 자리수만 중앙에 표시
                    number.clip_draw_to_origin((count2 - 1) * 25 + 9 * 25, 0, 25, 25, 370, 440, 50, 50)
            elif frame == 1800 and count1 != 0:  # 카운팅이 1~9일때
                shout.clip_draw_to_origin(shout_randidx * 40, 0, 40, 40, 330, 400, 130, 130)
                number.clip_draw_to_origin((count1 - 1) * 25, 0, 25, 25, 370, 440, 50, 50)

    def Me_Click(self):
        global count1, count2, me_shout_randidx, correct, p_key
        if count2 > 0:  # 2자리수 카운팅
            me_shout.clip_draw_to_origin(me_shout_randidx * 40, 0, 40, 40, 180, 400, 65, 65)
            if count1 != 0:  # 1의 자리가 0이 아닐때 -> 1,2자리수 모두 표시
                number.clip_draw_to_origin((count2 - 1) * 25 + 9 * 25, 0, 25, 25, 185, 420, 25, 25)
                number.clip_draw_to_origin((count1 - 1) * 25, 0, 25, 25, 205, 420, 25, 25)
            else:  # 1의 자리수가 0일때 -> 2의 자리수만 중앙에 표시
                number.clip_draw_to_origin((count2 - 1) * 25 + 9 * 25, 0, 25, 25, 200, 420, 25, 25)
        elif count1 != 0:  # 카운팅이 1~9일때
            me_shout.clip_draw_to_origin(me_shout_randidx * 40, 0, 40, 40, 180, 400, 65, 65)
            number.clip_draw_to_origin((count1 - 1) * 25, 0, 25, 25, 200, 420, 25, 25)

        if correct == True:
            me_key.clip_draw(0, 0, 70, 70, 175, 255, 60, 70)
        else:
            me_key.clip_draw(70, 0, 70, 70, 175, 255, 60, 70)

        qwer.clip_draw((p_key - 1)*25, 0, 25, 25, 175, 260, 50, 50)

    def Correct_Check(self):
        global key, p_key, frame, correct, check, last_speak
        if check is False and m_intro == False:
            if progress == goal and p_key != 0: #마지막 구호
                last_speak = True
                correct = False
                self.Wrong()
            elif progress == goal + 1 and p_key != 0: #마지막 구호
                last_speak = True
                correct = False
                self.Wrong()
            elif frame == 1800 and key == p_key:  #OK
                    correct = True
            else: #잘못된 키 입력 또는 타이밍 오차
                if progress == goal and last_speak == False: #마지막 구호 생략
                    pass
                else:
                    correct = False
                    self.Wrong()

            check = True

    def Wrong(self):
        global whistle_num, practice
        if whistle_num != 0 and intro == False:
            whistle_num -= 1
            BBick_w.play()
        # elif practice == False:
        #     gfw.push(punishment)
        #     BBick_p.play()

    def handle_event(self,e):
        global answer, ask, p_key, me_shout_time, me_shout_randidx, frame, answer_time
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_q and frame != 1600: #프레임이 1600일때는 키보드 입력 안됨
                p_key = 1
                me_shout_randidx = random.randint(0, 2)
                self.Correct_Check()
                me_shout_time = get_time()
            elif e.key == SDLK_w and frame != 1600: #프레임이 1600일때는 키보드 입력 안됨
                p_key = 2
                me_shout_randidx = random.randint(0, 2)
                self.Correct_Check()
                me_shout_time = get_time()
            elif e.key == SDLK_e and frame != 1600: #프레임이 1600일때는 키보드 입력 안됨
                p_key = 3
                me_shout_randidx = random.randint(0, 2)
                self.Correct_Check()
                me_shout_time = get_time()
            elif e.key == SDLK_r and frame != 1600: #프레임이 1600일때는 키보드 입력 안됨
                p_key = 4
                me_shout_randidx = random.randint(0, 2)
                self.Correct_Check()
                me_shout_time = get_time()
            elif e.key == SDLK_RETURN:
                self.health -= 10
                gfw.push(game_state, 2, self.health)
                if ask == True:
                    answer = True
                if ask_ == True:
                    answer_time = get_time()
            elif e.key == SDLK_SPACE:
                gfw.change(game_state,2,self.health)