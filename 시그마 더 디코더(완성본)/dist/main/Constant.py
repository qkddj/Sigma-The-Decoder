import time
import pygame
import time
import random
import numpy
import sys
import os

#프레임 설정
clock = pygame.time.Clock()
frame = 60

#프레임 설청 창 변수
Settings_window_frame_variable1 = 3
Settings_window_frame_variable2 = 3

#base set
pygame.init()

size_x = 1920
size_y = 1080

screen = pygame.display.set_mode((size_x,size_y))
# buffer = pygame.Surface((size_x,size_y))
pygame.display.set_caption("SIGMA : THE DECODER")
logo = pygame.image.load("symbol.png")
pygame.display.set_icon(logo)

#Bgm load
bg_menu = pygame.mixer.Sound("bgm\Game Time.mp3")
bg_main_menu = pygame.mixer.Sound("bgm\Aylex - Information Flow (freetouse.com).mp3")
volume = 7
bg_main_menu.set_volume(volume/10)
bg_menu.set_volume(volume/10)

#effect sound load
ef_positive_button = pygame.mixer.Sound("effect\positive_button.wav")
ef_negatvie_button = pygame.mixer.Sound("effect/negative_button.wav")

#color
Black = (12,12,12)
White = (255,255,255)
Red = (233,100,100)
Green = (60,179,113)
Blue = (74,168,216)
PowderBlue = (176,224,230)
Gray = (128,128,128)
DarkGray =  (60,58,57)
Background = (246,246,246)
Gold = (255,215,0)

############
#class zone#
############

#interface
class interface: 
    def Hpbar(hpbar_coordinate, hp, color):

        pygame.draw.rect(screen, (80,80,80), hpbar_coordinate)
        pygame.draw.rect(screen, color, [hpbar_coordinate[0], hpbar_coordinate[1], hp, hpbar_coordinate[3]])
        # pygame.draw.rect(screen, (0,0,0), [hpbar_coordinate[0]-4, hpbar_coordinate[1]-4, hpbar_coordinate[2]+8, hpbar_coordinate[3]+8], 4)

        hp_bar_img = pygame.image.load("img/interface/hp_bar2.png")
        screen.blit(hp_bar_img, (hpbar_coordinate[0],hpbar_coordinate[1]))
    
    def itembar(itembar_coordinate, skill_available, skill_icon, Colleague_Activation):
        pygame.draw.rect(screen, (200,200,200), itembar_coordinate)
        pygame.draw.rect(screen, (50,50,50),[itembar_coordinate[0], itembar_coordinate[1], itembar_coordinate[2]/2, itembar_coordinate[3]])
        pygame.draw.rect(screen, (0,0,0),[itembar_coordinate[0]-4, itembar_coordinate[1]-4, itembar_coordinate[2]+8, itembar_coordinate[3]+8], 4)

        myfont = pygame.font.SysFont(None, itembar_coordinate[3])
        mytext = myfont.render(str(skill_available), True, (0,0,0))

        screen.blit(mytext, (itembar_coordinate[0]+itembar_coordinate[2]/1.60,itembar_coordinate[1]+itembar_coordinate[3]/5))

        if Colleague_Activation:
            skill_icon = pygame.image.load(skill_icon)
        else:
            skill_icon = pygame.image.load("img/interface/스킬 아이콘/unknown.png")

        screen.blit(skill_icon, (itembar_coordinate[0], itembar_coordinate[1]))

# one blcok in the field creator
class Block:
    def __init__(self,pos = (0,0),wide = 100, value = 0,fill_color = (255,255,255),line_color = (0,0,0),surface = screen):
        self.value = value
        self.pos = pos
        self.txt = ScreenTxt(str(self.value),self.pos[0],self.pos[1], txt_color = White)
        self.fill_color = fill_color
        self.line_color = line_color
        self.wide = wide
        self.surface = surface
        self.check = 0
        self.unactivated_blcok = ScreenImg("img/interface/unactivated_blcok.png", self.pos[0], self.pos[1])
        self.activated_blcok = ScreenImg("img\interface/activated_block.png", self.pos[0], self.pos[1])
    
    def show(self):
        if self.check == 0:
            self.unactivated_blcok.show()
            self.txt.show()
        else:
            self.activated_blcok.show()
            self.txt.show()
        
# activated_block = ScreenImg("img\interface/activated_block.png", (self.pos[0]-int(self.wide/2), self.pos[1]-int(self.wide/2)))

#link object creator
class LinkBlock:
    def __init__(self,pre_pos = (0,0),post_pos = (0,120),surface = screen):
        self.pre_pos = pre_pos
        self.post_pos = post_pos
        self.surface = surface

    # def show(self):

#create txt object
class ScreenTxt:
    def __init__(self,value = None, pos_x = size_x/2, pos_y = size_y/2, pos_central = True,font = "NeoDunggeunmoPro-Regular.ttf",size = 30,txt_color = Black,txt_background = None,bold = False, italic = False,antialias= True):
        self.value = value
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_central = pos_central
        self.txt_color = txt_color
        self.txt_background = txt_background
        self.bold = bold
        self.antialias = antialias
        self.font = pygame.font.Font(font,size)
        
        if pos_central == True:
            self.object = self.font.render(value,antialias,txt_color)
            self.pos_object = self.object.get_rect()
            self.pos_object.center = (self.pos_x,self.pos_y)
        
        elif pos_central == False:
            self.object = self.font.render(value,antialias,txt_color)
            self.pos_object =  self.object.get_rect()
            self.pos_object.x = self.pos_x
            self.pos_object.y = self.pos_y
    
    def show(self):
            self.value = self.value
            self.pos_x = self.pos_x
            self.pos_y = self.pos_y
            self.pos_central = self.pos_central
            self.txt_color = self.txt_color
            self.txt_background = self.txt_background
            self.bold = self.bold
            self.antialias = self.antialias
            self.pos_central = self.pos_central
            
            if self.pos_central == True:
                self.object = self.font.render(self.value,self.antialias,self.txt_color)
                self.pos_object = self.object.get_rect()
                self.pos_object.center = (self.pos_x,self.pos_y)
            
            elif self.pos_central == False:
                self.object = self.font.render(self.value,self.antialias,self.txt_color)
                self.pos_object =  self.object.get_rect()
                self.pos_object.x = self.pos_x
                self.pos_object.y = self.pos_y

            if self.pos_central == True:

                screen.blit(self.object,self.pos_object)
            elif self.pos_central == False:
                screen.blit(self.object,self.pos_object)

#load img,easy to show
class ScreenImg:
    def __init__(self,value = None, pos_x = size_x/2, pos_y = size_y/2, pos_central = True):
        self.value = value
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_central = pos_central

        if pos_central == True:
            self.object = pygame.image.load(value)
            self.pos_object = self.object.get_rect()
            self.pos_object.center = (self.pos_x,self.pos_y)

        elif pos_central == False:
            self.object = pygame.image.load(value)
            self.pos_object =  self.object.get_rect()
            self.pos_object.x = self.pos_x
            self.pos_object.y = self.pos_y
               
    def show(self):
        self.value = self.value
        self.pos_x = self.pos_x
        self.pos_y = self.pos_y

        if self.pos_central == True:
            self.object = pygame.image.load(self.value)
            self.pos_object = self.object.get_rect()
            self.pos_object.center = (self.pos_x,self.pos_y)

        elif self.pos_central == False:
            self.object = pygame.image.load(self.value)
            self.pos_object =  self.object.get_rect()
            self.pos_object.x = self.pos_x
            self.pos_object.y = self.pos_y

        if self.pos_central == True:
            screen.blit(self.object,self.pos_object)
        elif self.pos_central == False:
            screen.blit(self.object,self.pos_object)

#script when informing circumstances 
class ScriptCircum:
    def __init__(self,cont1 = "",cont2= "Thou art more lovely and more temperate.",cont3="",is_typing = True,per_time = 0.03):
        # limit character per line
        # -korean : 37
        # -english (capital): 40
        # -english (small letter) : 54
        # -number : 30
        self.cont1 = cont1
        self.cont2 = cont2
        self.cont3 = cont3

        self.txt1 = ScreenTxt("",pos_y=740,size = 50,txt_color=White)
        self.txt2 = ScreenTxt("",pos_y=825,size = 50,txt_color=White)
        self.txt3 = ScreenTxt("",pos_y=920,size = 50,txt_color=White)

        #if is_typing is true, the the character of each txt line will be shown one by one
        self.is_typing = is_typing
        #this variable is time showing one character
        self.per_time = per_time

    def show(self):
        if self.is_typing:
            for i in self.cont1:
                self.txt1.value += i

                pause(self.per_time)

                conversation_window = pygame.image.load("img\interface\대화 창.png")
                screen.blit(conversation_window, (100,680))
                
                self.txt1.show()

                pygame.display.update()
        
            for i in self.cont2:
                self.txt2.value += i

                pause(self.per_time)

                conversation_window = pygame.image.load("img\interface\대화 창.png")
                screen.blit(conversation_window, (100,680))
                
                self.txt1.show()
                self.txt2.show()

                pygame.display.update()
            
            for i in self.cont3:
                self.txt3.value += i

                pause(self.per_time)

                conversation_window = pygame.image.load("img\interface\대화 창.png")
                screen.blit(conversation_window, (100,680))

                self.txt1.show()
                self.txt2.show()
                self.txt3.show()

                pygame.display.update()
        else:
            conversation_window = pygame.image.load("img\interface\대화 창.png")
            screen.blit(conversation_window, (100,680))

            self.txt1.value = self.cont1
            self.txt2.value = self.cont2
            self.txt3.value = self.cont3

            self.txt1.show()
            self.txt2.show()
            self.txt3.show()

            pygame.display.update()
#script when talking
class ScriptTalk:
    def __init__(self,standing = "img\standing\남주\남주 평소.png",name = "한",cont1 = "Shall i compare thee to a summer's day?",cont2= "Thou art more  lovelyand more temperate.",cont3="Rough winds do shake the darling buds of May",is_typing = True,per_time = 0.03):
        # img size : 320 * 275
        self.standing = ScreenImg(standing,300,830)
        self.name = ScreenTxt(name,520,712,size= 50, pos_central= False, txt_color=White)
    
        # limit character per line
        # -korean : 37
        # -english (capital): 40
        # -english (small letter) : 54
        # -number : 30
        self.cont1 = cont1
        self.cont2 = cont2
        self.cont3 = cont3

        self.txt1 = ScreenTxt("",520,795,size = 40,pos_central= False, txt_color=White)
        self.txt2 = ScreenTxt("",520,850,size = 40,pos_central= False, txt_color=White)
        self.txt3 = ScreenTxt("",520,905,size = 40,pos_central= False, txt_color=White)

        #if is_typing is true, the the character of each txt line will be shown one by one
        self.is_typing = is_typing
        #this variable is time showing one character
        self.per_time = per_time

    def show(self):

        if self.is_typing:
            for i in self.cont1:
                self.txt1.value += i

                pause(self.per_time)

                conversation_window = pygame.image.load("img\interface\대화 창.png")
                screen.blit(conversation_window, (100,680))
                pygame.draw.rect(screen,White,(500,760,self.name.object.get_size()[0] + 50,5))
                
                self.standing.show()
                self.name.show()

                self.txt1.show()

                pygame.display.update()
        
            for i in self.cont2:
                self.txt2.value += i

                pause(self.per_time)

                conversation_window = pygame.image.load("img\interface\대화 창.png")
                screen.blit(conversation_window, (100,680))
                pygame.draw.rect(screen,White,(500,760,self.name.object.get_size()[0] + 50,5))
                
                self.standing.show()
                self.name.show()

                self.txt1.show()
                self.txt2.show()

                pygame.display.update()
            
            for i in self.cont3:
                self.txt3.value += i

                pause(self.per_time)

                conversation_window = pygame.image.load("img\interface\대화 창.png")
                screen.blit(conversation_window, (100,680))
                pygame.draw.rect(screen,White,(500,760,self.name.object.get_size()[0] + 50,5))
                
                self.standing.show()
                self.name.show()

                self.txt1.show()
                self.txt2.show()
                self.txt3.show()

                pygame.display.update()
        else:
            conversation_window = pygame.image.load("img\interface\대화 창.png")
            screen.blit(conversation_window, (100,680))
            pygame.draw.rect(screen,White,(500,760,self.name.object.get_size()[0] + 50,5))

            self.txt1.value = self.cont1
            self.txt2.value = self.cont2
            self.txt3.value = self.cont3

            self.standing.show()
            self.name.show()

            self.txt1.show()
            self.txt2.show()
            self.txt3.show()

            pygame.display.update()

##########
#function#
##########

#pause function
def pause(sec : int):
    
    #this function is for pasue the pygame window while able to off it
    #sec : int / time for pause (second)
    
    start = time.time()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if time.time() - start > sec:
            break

#랜던 배열 만들기
def field_array(n,start_value,end_value):
    size = n * n
    variable = 0
    numpy_array = []

    random_array = numpy.random.choice(range(start_value,end_value+1), size, replace= True)

    for _ in range(n):
        variable += n
        numpy_array.append(random_array[variable - n : variable])

    numpy_array = numpy.array(numpy_array)

    return numpy_array