from Constant import *

confirmation_key = pygame.K_SPACE
confirmation_key_str = "SPACE"
up_key1 = pygame.K_w
up_key1_str = "W"
up_key2 = pygame.K_UP
down_key1 = pygame.K_s
down_key1_str = "s"
down_key2 = pygame.K_DOWN
right_key1 = pygame.K_d
right_key1_str = "d"
right_key2 = pygame.K_RIGHT
left_key1 = pygame.K_a
left_key1_str = "a"
left_key2 = pygame.K_LEFT
go_back_key = pygame.K_q
go_back_key_str = "Q"
back_completely = pygame.K_e
back_completely_str = "e"
companion_skill_1 = pygame.K_1
companion_skill_1_str = "1"
companion_skill_2 = pygame.K_2
companion_skill_2_str = "2"
companion_skill_3 = pygame.K_3
companion_skill_3_str = "3"

def set_key_function():
    pygame.draw.rect(screen, (80,80,80), [660, 440, 600, 200])
    pygame.draw.rect(screen, Blue, [655, 435, 610, 210],5)
    txt_answer = ScreenTxt("설정 할 키를 누르세요.", pos_central = False, pos_x = 700, pos_y = 515, size = 50)
    txt_answer.show()
    pygame.display.flip()
    pygame.display.update()
    run3 = True
    while run3:
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                
                key_to_change_str = event.unicode
                key_to_change = event.key
                if event.key == 1073742048:
                    key_to_change_str = "Ctrl"
                elif event.key == 1073742049:
                    key_to_change_str = "Shift"
                elif event.key == 27:
                    key_to_change_str = "Esc"
                elif event.key == 32:
                    key_to_change_str = "Space"
                run3 = False

    return key_to_change, key_to_change_str

