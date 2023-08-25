from Constant import *
from set_key import *

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""













메인 화면















"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

bg_main_menu.play(-1)

#opening effect
main_logo1 = ScreenTxt("",pos_y= 270, size = 50)
main_logo2 = ScreenTxt("_",pos_y = 370,size= 100)

for i in "SIGMA:":
    main_logo1.value = "{}_".format(main_logo1.value[:-1] + i)
    main_logo1.show()
    pygame.display.update()
    
    pause(0.1)
    screen.fill(Background)

main_logo1.value = "SIGMA:"
main_logo2.show()
pause(0.2)

for i in "The":  
    main_logo2.value = "{}_".format(main_logo2.value[:-1] + i)
    main_logo2.show()
    main_logo1.show()    
    pygame.display.update()
    
    pause(0.1)
    screen.fill(Background)

pause(0.1)

for i in " Decoder":
    main_logo2.value = "{}_".format(main_logo2.value[:-1] + i)
    main_logo2.show()
    main_logo1.show()    
    pygame.display.update()
    
    pause(0.1)
    screen.fill(Background)

pause(0.3)
main_logo2.value = 'The Decoder'

#stage selection function
def stage_select():
    Run_stage_select = True
    
    txt_stage = ScreenTxt("아도비스", pos_y = 250,size = 80)
    img_stage = ScreenImg("img\lara staindg.webp")
    txt_content = [ScreenTxt("", pos_y = 800,size = 50),ScreenTxt("", pos_y = 860,size = 50),ScreenTxt("", pos_y = 920,size = 50)]

    info_stage_name = ["Episode 1 : 지하 감옥","Episode 2 : ","Episode 3 : ","Episode 4 : ","Episode 5 : ","Episode 6: "]
    info_stage_img = ["img\stageimg1.png","img\shiroko.png","img\lara staindg.webp","img\KakaoTalk_20230812_020054139.jpg","img\KakaoTalk_20230811_092005950.jpg","img\KakaoTalk_20230809_080748152.webp"]
    info_content = [["버려진 도시에 남아있던 낡은 지하 감옥","","지하 감옥을 탈출하자"],
                    ["And summer’s lease hath all too short a date:","","Sometime too hot the eye of heaven shines,"],
                    ["And often is his gold complexion dimmed;","And every fair from fair sometime declines,",""],
                    ["By chance or nature’s changing course untrimmed;","But thy eternal summer shall not fade",""],
                    ["Nor lose possession of that fair thou ow’st;","",""],
                    ["","So long as men can breathe or eyes can see,",""]]

    txt_larrow = ScreenTxt("<",100,250,size = 100)
    txt_rarrow = ScreenTxt(">",1820,250,size = 100)

    txt_larrow.show()
    txt_rarrow.show()
    txt_stage.show()
    img_stage.show()

    stage_point = 0

    while Run_stage_select:
        clock.tick(frame)
        screen.fill(Background)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run_stage_select = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == left_key1 and stage_point > 0 or event.key == left_key2 and stage_point > 0:
                    stage_point -= 1
                    ef_positive_button.play()

                elif event.key == right_key1 and stage_point < 5 or event.key == right_key2 and stage_point < 5:
                    stage_point += 1
                    ef_positive_button.play()

                # stage function
                elif event.key == pygame.K_RETURN or event.key == confirmation_key:
                    battle_screen()

                elif event.key == pygame.K_ESCAPE:
                    ef_positive_button.play()
                    main_menu()

        #arrow show
        if stage_point == 0:
            txt_rarrow.show()
        
        elif stage_point == 5:
            txt_larrow.show()
        
        else:
            txt_larrow.show()
            txt_rarrow.show()

        #img and stage info show
        img_stage.value = info_stage_img[stage_point]
        txt_stage.value = info_stage_name[stage_point]

        img_stage.show()
        txt_stage.show()

        for i,content in enumerate(info_content[stage_point]):
            txt_content[i].value = content
            txt_content[i].show()

        pygame.display.update()

#main menu function
def main_menu():

    main_logo1.show()
    main_logo2.show()

    select_point = 0

    #select button effect
    txt_game_start1 = ScreenTxt("{ START }",size = 70,pos_y= 740, txt_color = Blue)
    txt_game_start2 = ScreenTxt("START",size = 30,pos_y= 640,txt_color=Gray)

    txt_exit1 = ScreenTxt("EXIT",size = 30,pos_y= 840,txt_color=Gray)
    txt_exit2 = ScreenTxt("{ EXIT }",size = 70,pos_y= 740, txt_color = Blue)

    Run_main_menu = True
    #selection
    while Run_main_menu:
        clock.tick(frame)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run_main_menu = False

            elif event.type == pygame.KEYDOWN:
                if event.key == down_key1 and select_point < 1 or event.key == down_key2 and select_point < 1:
                    select_point += 1
                    ef_positive_button.play()

                elif event.key == up_key1 and select_point > 0 or event.key == up_key2 and select_point > 0:
                    select_point -= 1
                    ef_positive_button.play()

                elif event.key == pygame.K_RETURN or event.key == confirmation_key:
                    
                    # 스테이지 선택 함수랑 함께 쌓여버리는 버그 있음
                    if select_point == 0:
                        ef_positive_button.play()
                        stage_select()

                    elif select_point == 1:
                        sys.exit()

        pygame.draw.rect(screen,Background,(0,500,1920,440))

        if select_point == 0:
            txt_game_start1.show()
            txt_exit1.show()
        
        elif select_point == 1:
            txt_game_start2.show()
            txt_exit2.show()

        pygame.display.update()

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""













일시 정지창 및 설정창















"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def key_setting_screen1():
    global up_key1
    global up_key1_str
    global down_key1
    global down_key1_str
    global left_key1
    global left_key1_str
    global right_key1
    global right_key1_str
    global companion_skill_1
    global companion_skill_1_str
    global companion_skill_2
    global companion_skill_2_str
    global companion_skill_3
    global companion_skill_3_str
    global confirmation_key
    global confirmation_key_str
    global back_completely
    global back_completely_str
    global go_back_key_str
    global go_back_key
    global Settings_window_frame_variable1
    global Settings_window_frame_variable2
    global frame
    global volume
    global bg_menu
    global bg_main_menu

    key_setting_screen_variable = [1, 1]

    key_setting_screen2()

    pygame.draw.rect(screen, Red, [-455 + 600 * key_setting_screen_variable[0], -25 + 170 * key_setting_screen_variable[1], 460, 110],5)
    pygame.draw.rect(screen, Blue, [1200 + 110 * Settings_window_frame_variable1, 210, 100, 80],5)

    pygame.display.flip()
    pygame.display.update()


    run1 = True
    while run1:
        clock.tick(frame)
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    run1 = False
                
                elif event.key == up_key1 or event.key == up_key2:
                    if key_setting_screen_variable[1] > 1:
                        key_setting_screen_variable[1] -= 1
                        
                elif event.key == down_key1 or event.key == down_key2:
                    if key_setting_screen_variable[1] < 5 and key_setting_screen_variable != [3, 4]:
                        key_setting_screen_variable[1] += 1
                
                elif event.key == left_key1 or event.key == left_key2:
                    if key_setting_screen_variable[0] > 1:
                        key_setting_screen_variable[0] -= 1
                
                elif event.key == right_key1 or event.key == right_key2:
                    if key_setting_screen_variable == [2, 5]:
                        key_setting_screen_variable = [3, 4]

                    elif key_setting_screen_variable[0] < 3:
                        key_setting_screen_variable[0] += 1

                elif event.key == confirmation_key:

                    if key_setting_screen_variable == [1, 1]:
                        up_key1, up_key1_str = set_key_function()

                    elif key_setting_screen_variable == [2, 1]:
                        down_key1, down_key1_str = set_key_function()

                    elif key_setting_screen_variable == [1, 2]:
                        left_key1, left_key1_str = set_key_function()
                    
                    elif key_setting_screen_variable == [2, 2]:
                        right_key1, right_key1_str = set_key_function()

                    elif key_setting_screen_variable == [1, 3]:
                        back_completely, back_completely_str = set_key_function()
                    
                    elif key_setting_screen_variable == [2, 3]:
                        go_back_key, go_back_key_str = set_key_function()

                    elif key_setting_screen_variable == [1, 4]:
                        confirmation_key, confirmation_key_str = set_key_function()
                    
                    elif key_setting_screen_variable == [2, 4]:
                        companion_skill_1, companion_skill_1_str = set_key_function()

                    elif key_setting_screen_variable == [1, 5]:
                        companion_skill_2, companion_skill_2_str = set_key_function()
                    
                    elif key_setting_screen_variable == [2, 5]:
                        companion_skill_3, companion_skill_3_str = set_key_function()

                    elif key_setting_screen_variable == [3, 1]:
                        run2 = True
                        while run2:
                            clock.tick(frame)
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:

                                    if event.key == pygame.K_ESCAPE:
                                        run2 = False
                                    
                                    elif event.key == left_key1 or event.key == left_key2:
                                        if Settings_window_frame_variable1 > 1:
                                            Settings_window_frame_variable1 -= 1

                                    elif event.key == right_key1 or event.key == right_key2:
                                        if Settings_window_frame_variable1 < 4:
                                            Settings_window_frame_variable1 += 1

                                    elif event.key == confirmation_key:
                                        Settings_window_frame_variable2 = Settings_window_frame_variable1
                                        run2 = False

                                    key_setting_screen_location_variable2 = 0

                                    for x in range(4):
                                        pygame.draw.rect(screen, Black, [1310 + key_setting_screen_location_variable2, 210, 100, 80],5)
                                        key_setting_screen_location_variable2 += 110
                                    
                                    pygame.draw.rect(screen, Blue, [1200 + 110 * Settings_window_frame_variable1, 210, 100, 80],5)

                                    pygame.display.flip()
                                    pygame.display.update()

                        Settings_window_frame_variable1 = Settings_window_frame_variable2

                        if Settings_window_frame_variable2 == 1:
                            frame = 10

                        elif Settings_window_frame_variable2 == 2:
                            frame = 30

                        elif Settings_window_frame_variable2 == 3:
                            frame = 60

                        else:
                            frame = 120

                    elif key_setting_screen_variable == [3, 2]:
                        run3 = True
                        while run3:
                            clock.tick(frame)
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:

                                    if event.key == pygame.K_ESCAPE:
                                        run3 = False
                                    
                                    elif event.key == left_key1 or event.key == left_key2:
                                        if volume > 0:
                                            volume -= 1

                                    elif event.key == right_key1 or event.key == right_key2:
                                        if volume < 10:
                                            volume += 1

                                    elif event.key == confirmation_key:
                                        run3 = False
                                    
                                    bg_main_menu.set_volume(volume/10)
                                    bg_menu.set_volume(volume/10)
                                    pygame.draw.rect(screen, (120,120,120), [1300, 400, 450, 100])
                                    pygame.draw.rect(screen, Red, [1295, 395, 460, 110],5)
                                    volume_txt = "<"+str(volume)+">"
                                    txt_answer = ScreenTxt(volume_txt, pos_central = False, pos_x = 1600, pos_y = 420, size = 65)
                                    txt_answer.show()
                                    txt_answer = ScreenTxt("노래 소리:", pos_central = False, pos_x = 1335, pos_y = 425, size = 50)
                                    txt_answer.show()
                                    pygame.display.flip()
                                    pygame.display.update()

                    key_setting_screen2()

                key_setting_screen3()

                if key_setting_screen_variable[0] < 3:
                    pygame.draw.rect(screen, Red, [-455 + 600 * key_setting_screen_variable[0], -25 + 170 * key_setting_screen_variable[1], 460, 110],5)

                else:
                    pygame.draw.rect(screen, Red, [1295, -5 + 200 * key_setting_screen_variable[1], 460, 110],5) 
                
                pygame.draw.rect(screen, Blue, [1200 + 110 * Settings_window_frame_variable1, 210, 100, 80],5)

                pygame.display.flip()
                pygame.display.update()


def key_setting_screen2():
    key_setting_screen_location_variable1 = 0
    key_setting_screen_location_variable2 = 0

    pygame.draw.rect(screen, Blue, [95, 95, 1730, 890],5)
    pygame.draw.rect(screen, (170,170,170), [100, 100, 1720, 880])

    for x in range(10):

        pygame.draw.rect(screen, (120,120,120), [150 + key_setting_screen_location_variable2, 150 + key_setting_screen_location_variable1, 450, 100])
        pygame.draw.rect(screen, Black, [145 + key_setting_screen_location_variable2, 145+key_setting_screen_location_variable1, 460, 110],5)
        pygame.draw.rect(screen, (70,70,70), [390 + key_setting_screen_location_variable2, 160 + key_setting_screen_location_variable1, 195, 80])
        pygame.draw.rect(screen, Black, [385 + key_setting_screen_location_variable2, 155 + key_setting_screen_location_variable1, 205, 90],5)

        key_setting_screen_location_variable1 += 170
        
        if x == 4:
            key_setting_screen_location_variable2 += 600
            key_setting_screen_location_variable1 = 0

    key_setting_screen_location_variable1 = 0

    for x in range(4):

        pygame.draw.rect(screen, (120,120,120), [1300, 200 + key_setting_screen_location_variable1, 450, 100])
        pygame.draw.rect(screen, Black, [1295, 195+key_setting_screen_location_variable1, 460, 110],5)

        key_setting_screen_location_variable1 += 200

    key_setting_screen_location_variable2=0

    for x in range(4):
        pygame.draw.rect(screen, (80,80,80), [1310 + key_setting_screen_location_variable2, 210, 100, 80])
        pygame.draw.rect(screen, Black, [1310 + key_setting_screen_location_variable2, 210, 100, 80],5)
        key_setting_screen_location_variable2 += 110
    
    txt_answer = ScreenTxt("노래 소리:", pos_central = False, pos_x = 1335, pos_y = 425, size = 50)
    txt_answer.show()
    volume_txt = "<"+str(volume)+">"
    txt_answer = ScreenTxt(volume_txt, pos_central = False, pos_x = 1600, pos_y = 420, size = 65)
    txt_answer.show()

    txt_answer = ScreenTxt("위", pos_central = False, pos_x = 170, pos_y = 175, size = 50)
    txt_answer.show()
    txt_answer = ScreenTxt(up_key1_str, pos_central = False, pos_x = 480, pos_y = 175, size = 60)
    txt_answer.show()
    txt_answer = ScreenTxt("아래", pos_central = False, pos_x = 770, pos_y = 175, size = 50)
    txt_answer.show()
    txt_answer = ScreenTxt(down_key1_str, pos_central = False, pos_x = 1080, pos_y = 175, size = 60)
    txt_answer.show()
    txt_answer = ScreenTxt("왼쪽", pos_central = False, pos_x = 170, pos_y = 345, size = 50)
    txt_answer.show()
    txt_answer = ScreenTxt(left_key1_str, pos_central = False, pos_x = 480, pos_y = 345, size = 60)
    txt_answer.show()
    txt_answer = ScreenTxt("오른쪽", pos_central = False, pos_x = 770, pos_y = 345, size = 50)
    txt_answer.show()
    txt_answer = ScreenTxt(right_key1_str, pos_central = False, pos_x = 1080, pos_y = 345, size = 60)
    txt_answer.show()
    txt_answer = ScreenTxt("리셋", pos_central = False, pos_x = 170, pos_y = 515, size = 50)
    txt_answer.show()
    txt_answer = ScreenTxt(back_completely_str, pos_central = False, pos_x = 480, pos_y = 515, size = 60)
    txt_answer.show()
    txt_answer = ScreenTxt("뒤로가기", pos_central = False, pos_x = 770, pos_y = 515, size = 50)
    txt_answer.show()
    txt_answer = ScreenTxt(go_back_key_str, pos_central = False, pos_x = 1080, pos_y = 515, size = 60)
    txt_answer.show()
    txt_answer = ScreenTxt("결정", pos_central = False, pos_x = 170, pos_y = 685, size = 50)
    txt_answer.show()
    txt_answer = ScreenTxt(confirmation_key_str, pos_central = False, pos_x = 420, pos_y = 685, size = 60)
    txt_answer.show()
    txt_answer = ScreenTxt("동료 스킬1", pos_central = False, pos_x = 770, pos_y = 685, size = 40)
    txt_answer.show()
    txt_answer = ScreenTxt(companion_skill_1_str, pos_central = False, pos_x = 1080, pos_y = 685, size = 60)
    txt_answer.show()
    txt_answer = ScreenTxt("동료 스킬2", pos_central = False, pos_x = 170, pos_y = 855, size = 40)
    txt_answer.show()
    txt_answer = ScreenTxt(companion_skill_2_str, pos_central = False, pos_x = 480, pos_y = 855, size = 60)
    txt_answer.show()
    txt_answer = ScreenTxt("동료 스킬3", pos_central = False, pos_x = 770, pos_y = 855, size = 40)
    txt_answer.show()
    txt_answer = ScreenTxt(companion_skill_3_str, pos_central = False, pos_x = 1080, pos_y = 855, size = 60)
    txt_answer.show()
    txt_answer = ScreenTxt("10", pos_central = False, pos_x= 1335, pos_y= 225, size = 50)
    txt_answer.show()
    txt_answer = ScreenTxt("30", pos_central = False, pos_x= 1445, pos_y= 225, size = 50)
    txt_answer.show()
    txt_answer = ScreenTxt("60", pos_central = False, pos_x= 1555, pos_y= 225, size = 50)
    txt_answer.show()
    txt_answer = ScreenTxt("120", pos_central = False, pos_x= 1655, pos_y= 225, size = 50)
    txt_answer.show()

    pygame.display.flip()
    pygame.display.update()
    
def key_setting_screen3():
    key_setting_screen_location_variable1 = 0
    key_setting_screen_location_variable2 = 0

    for x in range(10):

        pygame.draw.rect(screen, Black, [145 + key_setting_screen_location_variable2, 145 + key_setting_screen_location_variable1, 460, 110],5)

        key_setting_screen_location_variable1 += 170
        if x == 4:
            key_setting_screen_location_variable2 += 600
            key_setting_screen_location_variable1 = 0
    
    key_setting_screen_location_variable1 = 0

    for x in range(4):

        pygame.draw.rect(screen, Black, [1295, 195 + key_setting_screen_location_variable1, 460, 110],5)

        key_setting_screen_location_variable1 += 200

    pygame.display.flip()
    pygame.display.update()

def pause2():
    pause_variable = 1
    run = True

    pygame.draw.rect(screen, Gray, [700, 300, 400, 600])
    pygame.draw.rect(screen, Blue, [695, 295, 410, 610],5)
    pygame.draw.rect(screen, Blue, [750, 350, 300, 100])
    pygame.draw.rect(screen, Blue, [750, 500, 300, 100])
    pygame.draw.rect(screen, Blue, [750, 650, 300, 100])
    pygame.draw.rect(screen, Red, [745, 345, 310, 110],5)
    pygame.draw.rect(screen, Black, [745, 495, 310, 110],5)
    pygame.draw.rect(screen, Black, [745, 645, 310, 110],5)

    txt_answer = ScreenTxt("게임 재게", pos_central = False, pos_x = 770, pos_y = 370, size = 60)
    txt_answer.show()
    txt_answer = ScreenTxt("게임 설정", pos_central = False, pos_x = 770, pos_y = 520, size = 60)
    txt_answer.show()
    txt_answer = ScreenTxt("메인 메뉴", pos_central = False, pos_x = 770, pos_y = 670, size = 60)
    txt_answer.show()

    pygame.display.flip()
    pygame.display.update()

    while run:
        clock.tick(frame)
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    run = False

                elif event.key == up_key1 or event.key == up_key2:
                    if pause_variable > 1:
                        pause_variable -= 1
                        
                elif event.key == down_key1 or event.key == down_key2:
                    if pause_variable < 3:
                        pause_variable += 1

                elif event.key == confirmation_key:
                    if pause_variable == 1:
                        run = False

                    elif pause_variable == 2:
                        key_setting_screen1()
                        run = False

                    else:
                        run = False
                        global Run
                        Run = False

                if pause_variable == 1:
                    pygame.draw.rect(screen, Red, [745, 345, 310, 110],5)
                    pygame.draw.rect(screen, Black, [745, 495, 310, 110],5)
                    pygame.draw.rect(screen, Black, [745, 645, 310, 110],5)

                elif pause_variable == 2:
                    pygame.draw.rect(screen, Black, [745, 345, 310, 110],5)
                    pygame.draw.rect(screen, Red, [745, 495, 310, 110],5)
                    pygame.draw.rect(screen, Black, [745, 645, 310, 110],5)
                else:
                    pygame.draw.rect(screen, Black, [745, 345, 310, 110],5)
                    pygame.draw.rect(screen, Black, [745, 495, 310, 110],5)
                    pygame.draw.rect(screen, Red, [745, 645, 310, 110],5)

        pygame.display.flip()
        pygame.display.update()

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""













전투 화면















"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def battle_screen():
    global Run
    global start

    bg_main_menu.stop()
    bg_menu.play(-1)

    
    #체력 및 동료 바
    hpbar_coordinate1 = [515, 100, 400, 30]
    hpbar_coordinate2 = [1250, 100, 400, 30]
    hacker_hp = hpbar_coordinate1[2]
    enemy_hp = hpbar_coordinate1[2]

    itembar_coordinate1 = [1000, 900, 100, 50]
    itembar_coordinate2 = [1200, 900, 100, 50]
    itembar_coordinate3 = [1400, 900, 100, 50]

    skill_available1 = "O"
    skill_available2 = "O"
    skill_available3 = "O"

    #create field
    field = []

    field_value = field_array(7)

    for i in range(7):
        para = []

        start_point_x = 150
        start_point_y = 200

        for j in range(7):
            x = start_point_x+i*120
            y = start_point_y+j*120
            
            k = Block((x,y),value = field_value[i][j])
            para.append(k) 

        field.append(para)

    #start coordinate
    point_x = 3
    point_y = 3

    #check coordinate
    passed = []
    link = []

    #moving in the field

    #answer
    answer = random.randint(20,500)
    txt_answer = ScreenTxt("맞춰야 하는 합:{}".format(answer),pos_central = False, pos_x= 0, pos_y= 0,size= 50)
    txt_answer.show()

    #sum
    sum = 0
    txt_sum = ScreenTxt("현재 합:{}".format(sum),pos_central = False, pos_x= 0, pos_y= 70,size= 50)
    sum += field[point_x][point_y].value

    Run = True

    while Run:

        clock.tick(frame)

        screen.fill(Gray)
        txt_answer.show()

        txt_sum.value = "현재 합:{}".format(sum)

        txt_sum.show()

        if (point_x,point_y) not in passed:
            passed.append((point_x,point_y))

        ##set the Blocks' line color
        if abs(answer- sum) < 10:
            lining_color = Red

        elif abs(answer- sum) == 0:
            lining_color = Gold

        else:
            lining_color = Blue

        #coloring the Blocks
        for point in passed:
            field[point[0]][point[1]].fill_color = (181,214,146)
            field[point[0]][point[1]].line_color = lining_color

        #show the Blocks
        for i in field:
            for j in i:
                j.show()
        
        if len(passed) > 1:
            for pre,post in zip(passed[0:-1],passed[1:]):
                        wide = 20
                        pygame.draw.rect(screen,lining_color,((field[pre[0]][pre[1]].pos[0]+field[post[0]][post[1]].pos[0])//2-wide//2,(field[pre[0]][pre[1]].pos[1]+field[post[0]][post[1]].pos[1])//2-wide//2,wide,wide))                       

        interface.Hpbar(hpbar_coordinate1, hacker_hp, Blue)
        interface.Hpbar(hpbar_coordinate2, enemy_hp, Red)

        interface.itembar(itembar_coordinate1, skill_available1)
        interface.itembar(itembar_coordinate2, skill_available2)
        interface.itembar(itembar_coordinate3, skill_available3)

        #moving ,start selecting,checking whether correct
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False

            
            elif event.type == pygame.KEYDOWN:
                if (event.key == left_key1 or event.key == left_key2) and point_x > 0 and (point_x-1,point_y) not in passed:
                    point_x -= 1
                    sum += field[point_x][point_y].value

                elif (event.key == right_key1 or event.key == right_key2) and point_x < 6 and (point_x+1,point_y) not in passed:
                    point_x += 1
                    sum += field[point_x][point_y].value
                    
                elif (event.key == up_key1 or event.key == up_key2) and point_y > 0 and (point_x,point_y-1) not in passed:
                    point_y -= 1
                    sum += field[point_x][point_y].value

                elif (event.key == down_key1 or event.key == down_key2) and point_y < 6 and (point_x,point_y+1) not in passed:
                    point_y += 1               
                    sum += field[point_x][point_y].value   
                            
                elif event.key == go_back_key:
                    if len(passed) > 1:
                        sum -= field[passed[-1][0]][passed[-1][1]].value

                        point_x = passed[-2][0]
                        point_y = passed[-2][1]

                        field[passed[-1][0]][passed[-1][1]].fill_color = (255,255,255)
                        field[passed[-1][0]][passed[-1][1]].line_color = Black

                        passed = passed[:-1]

                        break
                    
                    else:
                        print(1)

                elif event.key == back_completely:
                    if len(passed) > 1:
                        sum = field[passed[0][0]][passed[0][1]].value

                        point_x = passed[0][0]
                        point_y = passed[0][1]
                        
                        reverse_passed = list(reversed(passed))

                        for i in reverse_passed[:-1]:
                            start = time.time()
                            field[i[0]][i[1]].fill_color = (255,255,255)
                            field[i[0]][i[1]].line_color = Black
                            field[i[0]][i[1]].show()
                            pygame.display.update()
                            passed = passed[:-1]

                            screen.fill(Gray)
                            txt_answer.show()

                            txt_sum.value = "현재 합:{}".format(sum)

                            txt_sum.show()

                            for i in field:
                                for j in i:
                                    j.show()

                            if len(passed) > 1:
                                for pre,post in zip(passed[0:-1],passed[1:]):
                                    pygame.draw.rect(screen,lining_color,((field[pre[0]][pre[1]].pos[0]+field[post[0]][post[1]].pos[0])//2-10,(field[pre[0]][pre[1]].pos[1]+field[post[0]][post[1]].pos[1])//2-10,20,20))  
                            
                            interface.Hpbar(hpbar_coordinate1, hacker_hp, Blue)
                            interface.Hpbar(hpbar_coordinate2, enemy_hp, Red)

                            interface.itembar(itembar_coordinate1, skill_available1)
                            interface.itembar(itembar_coordinate2, skill_available2)
                            interface.itembar(itembar_coordinate3, skill_available3)
                            pause(0.01)
                    else:
                        print(2)
                
                # elif event.key == confirmation_key:  
                #     print("오차:{}".format(answer-sum))
                
                elif event.key == pygame.K_ESCAPE:
                    pause2()
                
                elif event.key == pygame.K_SPACE:
                    if sum <= answer:
                        enemy_hp -= sum / answer * 100
                        print(sum / answer* 100)
                    else:
                        enemy_hp -= answer / sum * 100
                        print(answer / sum * 100)
                    
                    hacker_hp -= random.randint(10, 100)

                    field_value = field_array(7)
                    #answer
                    answer = random.randint(20, 500)
                    txt_answer = ScreenTxt("맞춰야 하는 합:{}".format(answer),pos_central = False, pos_x= 0, pos_y= 0,size= 50)
                    txt_answer.show()

                    #sum
                    sum = 0
                    txt_sum = ScreenTxt("현재 합:{}".format(sum),pos_central = False, pos_x= 0, pos_y= 70,size= 50)
                    sum += field[point_x][point_y].value

                    if len(passed) > 1:
                        sum = field[passed[0][0]][passed[0][1]].value

                        point_x = passed[0][0]
                        point_y = passed[0][1]
                        
                        reverse_passed = list(reversed(passed))

                        for i in reverse_passed[:-1]:
                            start = time.time()
                            field[i[0]][i[1]].fill_color = (255,255,255)
                            field[i[0]][i[1]].line_color = Black
                            field[i[0]][i[1]].show()
                            pygame.display.update()
                            passed = passed[:-1]

                            screen.fill(Gray)
                            txt_answer.show()

                            txt_sum.value = "현재 합:{}".format(sum)

                            txt_sum.show()

                            for i in field:
                                for j in i:
                                    j.show()

                            if len(passed) > 1:
                                for pre,post in zip(passed[0:-1],passed[1:]):
                                    pygame.draw.rect(screen,lining_color,((field[pre[0]][pre[1]].pos[0]+field[post[0]][post[1]].pos[0])//2-10,(field[pre[0]][pre[1]].pos[1]+field[post[0]][post[1]].pos[1])//2-10,20,20))  
                            interface.Hpbar(hpbar_coordinate1, hacker_hp, Blue)
                            interface.Hpbar(hpbar_coordinate2, enemy_hp, Red)

                            interface.itembar(itembar_coordinate1, skill_available1)
                            interface.itembar(itembar_coordinate2, skill_available2)
                            interface.itembar(itembar_coordinate3, skill_available3)
                            pause(0.01)
                    else:
                        print(2)
                
                elif event.key == companion_skill_1:
                    if skill_available1 == "O":
                        skill_available1 = "X"

                elif event.key == companion_skill_2:
                    if skill_available2 == "O":
                        skill_available2 = "X"

                elif event.key == companion_skill_3:
                    if skill_available3 == "O":
                        skill_available3 = "X"

        pygame.display.flip()

    bg_menu.stop()
    bg_main_menu.play(-1)

main_menu()
# battle_screen()