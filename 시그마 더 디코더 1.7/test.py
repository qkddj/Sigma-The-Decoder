from Constant import *

screen.fill(Background)

Run = True

#주인공 이름 설정
name = 'prota'

#캐릭터 대사 및 스탠딩 이미지 정보
info_character = [[name],["yui"]]
info_standing = [["img\standing\protagonist\prota1.png"],
                 ["img\lara staindg.webp"]]

#대본 불러오기
file_txt = open("script/episode1/first.txt","r", encoding="UTF8")
info_script = [txt[:-1] for txt in file_txt.readlines()]

#대본 출력
for i,txt in enumerate(info_script):
    sc_cirum = ScriptCircum()
    sc_talk = ScriptTalk()

    cont = []

    #상황 설명 일때
    if txt == "circum":

        for j in range(3):
            if info_script[i+j+1] is None or info_script[i+j+1] == "Null":
                cont.append("")
            
            else:
                cont.append(info_script[i+j+1])
        
        sc_cirum.cont1 = cont[0]
        sc_cirum.cont2 = cont[1]
        sc_cirum.cont3 = cont[2]

        sc_cirum.show()    

        Run = True  

        while Run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        Run =False

    #대사를 읽는 부분 일때
    elif txt == "talk":
        index_character = int(info_script[i+1][0])
        index_standing = int(info_script[i+1][1])
        
        character_name = info_character[index_character][0]
        standing = info_standing[index_character][index_standing]

        for j in range(3):
            if info_script[i+j+2] is None or info_script[i+j+2] == "Null":
                cont.append("")
            
            else:
                cont.append(info_script[i+j+2])
        
        sc_talk.name.value = character_name
        sc_talk.standing.value = standing
        sc_talk.cont1 = cont[0]
        sc_talk.cont2 = cont[1]
        sc_talk.cont3 = cont[2]

        sc_talk.show()    

        Run = True  

        while Run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        Run =False
    else:
        pass
    

