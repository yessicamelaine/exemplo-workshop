import pygame
import speech_recognition as sr   #Speect to text
from gtts import gTTS            #text to speech
from pygame import mixer
import random
import time

display_width = 1024
display_height = 768

blue = (0,0,200)
black = (0,0,0)
white = (255,255,255)
red=(200,0,0)
green=(0,200,0)
bright_red=(255,0,0)
bright_green=(0,255,0)
yellow=(255,255,0)
light_yellow=(255,255,204)

pontos = 0
intro = True
falouAlf = False


alf = 'abcdefghijklmnopqrstuvwxyz'
alfMaisc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
textIntro = "Bem vindo ao Jogo chamado Seguinte! Clique TAB para selecionar sua opção Começar, ou TAB para sua opção Sobre o jogo , ou TAB para opção sair. Lembre-se de pressionar ENTER para confirmar a opção selecionada."
acertouu = "Acertou! Continua? Clique TAB para selecionar Sim para continuar, ou TAB para selecionar Não e sair do jogo. Pressione ENTER para confirmar a opção selecionada."
errouu = "Errou! Continua? Clique TAB para selecionar Sim para continuar, ou TAB para selecionar Não e sair do jogo. Pressione ENTER para confirmar a opção selecionada."
sobree = "Sobre o jogo: Tem como objetivo estimular a alfabetização e o conhecimento de comandos de informática. Será falado uma letra e a pessoa deve falar a letra seguinte. Este jogo foi criado por Yessica Melaine Palomino Castillo. Clique TAB para selecionar sua opção e ENTER para confirmar."

pygame.init()

felizImg = pygame.image.load('feliz.png')
tristeImg = pygame.image.load('triste.png')
introImg = pygame.image.load('capa.jpg')
loopImg = pygame.image.load('loop.jpg')
fundoImg = pygame.image.load('fundo.jpg')
jogoIcon = pygame.image.load('icon.jpg')

font = pygame.font.Font('freesansbold.ttf', 32) 
smallText = pygame.font.Font("freesansbold.ttf",20)
text = font.render(textIntro, True, green, blue) 
textRect = text.get_rect() 
textRect.center = (display_width // 2, display_height// 2) 

pygame.display.set_caption("Seguinte")
gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()
pygame.display.set_icon(jogoIcon)

def quitgame():
    pygame.quit()
    quit()

def muda_cor(msg,x,y,w,h,ic):
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
        smallText = pygame.font.Font("freesansbold.ttf",35)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        gameDisplay.blit(textSurf, textRect)    
    
def button(msg,x,y,w,h,ic,ac,action=None):
        muda_cor(msg,x,y,w,h,ic)

def buttonNome(msi): 
    mixer.init()
    mixer.music.load(msi)
    mixer.music.play()   
        
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def mostra_letra_atual(text):
    hugeText = pygame.font.Font('freesansbold.ttf',200)
    TextSurf, TextRect = text_objects(text, hugeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    
def linha_text(mtxt,f,t,w,h):
    TextSurfDesc, TextRectDesc = text_objects(mtxt, pygame.font.SysFont(f,t))
    TextRectDesc = (w,h)
    gameDisplay.blit(TextSurfDesc, TextRectDesc)    

def imagem(qualImg,x,y):
    gameDisplay.blit(qualImg,(x,y))

def pcDiz(msg): #TEXT TO SPEECH
    if msg == intro or msg == textIntro:
        strr = "intro"
    elif msg == sobree:
        strr = "sobre"    
    elif msg == acertouu:
        strr = "acertou"
    elif msg == errouu:
        strr = "errou"     
    else:
        strr = "pontos"    
    
    pcFala = gTTS(text=msg, lang="pt", slow=False) 
    pcFala.save(strr+".mp3") 
    mixer.init()
    mixer.music.load(strr+".mp3")
    mixer.music.play()

def pontuacao(pontos):
    font=pygame.font.SysFont(None,30)
    text= font.render("Pontos: "+str(pontos), True , black)
    gameDisplay.blit(text, (0,25)) 
    
def sobre():
    count = 0
    enter = False
    caps = False
    shift = False
    ctrl = False
    destaqV=False
    destaqSa = False
    pcDiz(sobree)
    time.sleep(28.3) 
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
                count+=1
                if count > 0:
                    if count%2 == 1:
                        print("Clicou "+format(count)+" vezes")
                        print("Clicou Voltar")
                        buttonNome("bvoltar.mp3")
                        time.sleep(1) 
                        destaqV=True
                        destaqSa = False
                    if count%2 == 0:
                        print("Clicou "+format(count)+" vezes")
                        print("Clicou SAIR")
                        buttonNome("bsair.mp3")
                        time.sleep(1) 
                        destaqV=False
                        destaqSa = True
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER)  :
                enter = True
                caps=False
                shift = False
                ctrl = False
                print("Clicou ENTER")
                if count > 0:
                    if count%2 == 1 and enter == True:
                        game_intro()
                    if count%2 == 0 and  enter == True:
                        quitgame()    
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_CAPSLOCK)  :
                enter = False
                caps=True
                shift = False
                ctrl = False
                print("Clicou CAPS")
                buttonNome("bcaps.mp3")
                time.sleep(1.23)
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT)  :
                enter = False
                caps = False
                shift=True
                ctrl = False
                print("Clicou SHIFT") 
                buttonNome("bshift.mp3")
                time.sleep(1.24)
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL)  :
                enter = False
                caps = False
                shift = False
                ctrl=True
                print("Clicou CONTROL")
                buttonNome("bcontrol.mp3")
                time.sleep(1.24)  
                 
        gameDisplay.fill(white)
        imagem(loopImg,0,0)
        largeText = pygame.font.SysFont('comicsansms',50)
        TextSurf, TextRect = text_objects("Seguinte", largeText)
        TextRect.center = ((display_width/2),(display_height/4.5))
        gameDisplay.blit(TextSurf, TextRect)
    
        linha_text("Este jogo tem como objetivo estimular alfabetização ",'comicsansms',27,(display_width/6),(display_height/3))
        linha_text("e aprender comandos básicos de informática. ",'comicsansms',27,(display_width/6),(display_height/2.7))
        linha_text("O jogo vai falar a letra atual e você deve falar",'comicsansms',27,(display_width/6),(display_height/2.1))
        linha_text("a letra seguinte.",'comicsansms',27,(display_width/6),(display_height/1.9))
        linha_text("Autora do jogo: Yessica Melaine Palomino Castillo",'comicsansms',15,(display_width/3),(display_height-(display_height/12)))
       
        mixer.music.pause()
        
        button("Voltar",(display_width/10),(display_height-(display_height/6)),200,100,green,bright_green,game_intro)
        button("Sair",(display_width/10)+650,(display_height-(display_height/6)),200,100,red,bright_red,quitgame)
        if destaqV == True: 
            pygame.draw.rect(gameDisplay, bright_green,((display_width/10),(display_height-(display_height/6)),200,100),20)
        if destaqSa == True:
            pygame.draw.rect(gameDisplay, bright_red,((display_width/10)+650,(display_height-(display_height/6)),200,100),20)
        
        pygame.display.update()      

def acertou(pt): 
    x = (display_width * 0.38)
    y = (display_height * 0.15)   
    enterr = False
    caps=False
    shift = False
    ctrl = False
    countA = 0
    destaqS = False
    destaqN = False

    mixer.music.load("aplauso.mp3")
    mixer.music.play()
    time.sleep(4)         
    pontoss ="Pontuação total: "+format(pt)
    pcDiz(pontoss)
    time.sleep(4)    
    pcDiz(acertouu)
    time.sleep(17)
        
    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
                countA+=1
                if countA > 0:
                    if countA%2 == 1:
                        print("Clicou "+format(countA)+" vezes")
                        print("Clicou SIM")
                        destaqS = True
                        destaqN = False
                        buttonNome("bsim.mp3")
                        time.sleep(1) 
                    if countA%2 == 0:
                        print("Clicou "+format(countA)+" vezes")
                        print("Clicou NAO")
                        destaqS = False
                        destaqN = True
                        buttonNome("bnao.mp3")
                        time.sleep(1)
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER ) :
                enterr = True
                caps=False
                shift = False
                ctrl = False
                print("Clicou ENTER")
                if countA > 0:
                    if countA%2 == 1 and enterr == True:
                        game_loop()
                    if countA%2 == 0 and enterr == True:
                        quitgame()
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_CAPSLOCK)  :
                enterr = False
                caps=True
                shift = False
                ctrl = False
                print("Clicou CAPS")
                buttonNome("bcaps.mp3")
                time.sleep(1.23)
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT)  :
                enterr = False
                caps = False
                shift=True
                ctrl = False
                print("Clicou SHIFT") 
                buttonNome("bshift.mp3")
                time.sleep(1.24)
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL)  :
                enterr = False
                caps = False
                shift = False
                ctrl=True
                print("Clicou CONTROL")
                buttonNome("bcontrol.mp3")
                time.sleep(1.24)                    
                
        gameDisplay.fill(white)  
        imagem(loopImg,0,0)
        imagem(felizImg,x,y)
        TextSurfLetra, TextRectLetra = text_objects("Pontos: "+format(pontos), pygame.font.SysFont('comicsansms',60))
        TextRectLetra.center = ((display_width/2),(display_height/1.8))
        gameDisplay.blit(TextSurfLetra, TextRectLetra)
        largeText = pygame.font.SysFont('comicsansms',50)
        TextSurf, TextRect = text_objects("Acertou! Continua?", largeText)
        TextRect.center = ((display_width/2),(display_height/1.4))
        gameDisplay.blit(TextSurf, TextRect)
        
        mixer.music.pause()
        
        button("Sim",(display_width/10),(display_height-(display_height/6)),200,100,green,bright_green,game_loop)
        button("Não",(display_width/10)+650,(display_height-(display_height/6)),200,100,red,bright_red,quitgame)
        if destaqS == True :
            pygame.draw.rect(gameDisplay, bright_green,((display_width/10),(display_height-(display_height/6)),200,100),20)
        if destaqN == True:
            pygame.draw.rect(gameDisplay, bright_red,((display_width/10)+650,(display_height-(display_height/6)),200,100),20)
        
        pygame.display.update()


def errou(pt,letra):
    x = (display_width * 0.38)
    y = (display_height * 0.15)   
    enterrr = False
    caps=False
    shift = False
    ctrl = False
    destaqS = False
    destaqN = False
    countB = 0
    corrige = "Letra correta: "+letra+"  "
    
    mixer.init()
    mixer.music.load("wahwah.wav")
    mixer.music.play()
    time.sleep(4) 
    pontoss ="Pontuação total: "+format(pt)+"   "
    pcDiz(pontoss)
    time.sleep(4.5)
    pcCorrige = gTTS(text=corrige, lang="pt", slow=False) 
    pcCorrige.save("corrige.mp3") 
    mixer.init()
    mixer.music.load("corrige.mp3")
    mixer.music.play()
    time.sleep(4.1)
    pcDiz(errouu)
    time.sleep(16.2)
   
    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
                countB+=1
                if countB > 0:
                    if countB%2 == 1:
                        print("Clicou "+format(countB)+" vezes")
                        print("Clicou SIM")  
                        destaqS = True
                        destaqN = False
                        buttonNome("bsim.mp3")
                        time.sleep(1)
                    if countB%2 == 0:
                        print("Clicou "+format(countB)+" vezes")
                        print("Clicou NAO")  
                        destaqS = False
                        destaqN = True
                        buttonNome("bnao.mp3")
                        time.sleep(1) 
                    
            if event.type == pygame.KEYDOWN and( event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER)  :
                enterrr = True
                caps=False
                shift = False
                ctrl = False
                print("Clicou ENTER")  
                if countB > 0:
                    if countB%2 == 1 and enterrr == True:
                        game_loop()
                    if countB%2 == 0 and enterrr == True:
                        quitgame()    
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_CAPSLOCK)  :
                enterrr = False
                caps=True
                shift = False
                ctrl = False
                print("Clicou CAPS")
                buttonNome("bcaps.mp3")
                time.sleep(1.23)
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT)  :
                enterrr = False
                caps = False
                shift=True
                ctrl = False
                print("Clicou SHIFT") 
                buttonNome("bshift.mp3")
                time.sleep(1.24)
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL)  :
                enterrr = False
                caps = False
                shift = False
                ctrl=True
                print("Clicou CONTROL")
                buttonNome("bcontrol.mp3")
                time.sleep(1.24) 
                
        gameDisplay.fill(white)
        imagem(loopImg,0,0)
        imagem(tristeImg,x,y)
        TextSurfLetra, TextRectLetra = text_objects("Pontos: "+format(pontos), pygame.font.SysFont('comicsansms',60))
        TextRectLetra.center = ((display_width/2),(display_height/1.9))
        gameDisplay.blit(TextSurfLetra, TextRectLetra)
        TextSurfLetra, TextRectLetra = text_objects(corrige, pygame.font.SysFont('comicsansms',52))
        TextRectLetra.center = ((display_width/2),(display_height/1.6))
        gameDisplay.blit(TextSurfLetra, TextRectLetra)
        largeText = pygame.font.SysFont('comicsansms',50)
        TextSurf, TextRect = text_objects("Errou! Continua?", largeText)
        TextRect.center = ((display_width/2),(display_height/1.4))
        gameDisplay.blit(TextSurf, TextRect)
        
        mixer.music.pause()
        
        button("Sim",(display_width/10),(display_height-(display_height/6)),200,100,green,bright_green,game_loop)
        button("Não",(display_width/10)+650,(display_height-(display_height/6)),200,100,red,bright_red,quitgame)
        
        if destaqS == True: 
            pygame.draw.rect(gameDisplay, bright_green,((display_width/10),(display_height-(display_height/6)),200,100),20)
        if destaqN == True:
            pygame.draw.rect(gameDisplay, bright_red,((display_width/10)+650,(display_height-(display_height/6)),200,100),20)
       
        pygame.display.update()

def falaAlfabeto():
    frase0 = 'Vamos relembrar o alfabeto?'+"          "+'A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z'
    pcLetra = gTTS(text=frase0, lang="pt", slow=False) 
    pcLetra.save("frase0.mp3")
    mixer.init()
    mixer.music.load("frase0.mp3")
    mixer.music.play()
    time.sleep(22) 
    return True

def game_loop():
    global pontos
    gameExit= False
    global falouAlf
    
    if falouAlf == False :
        falouAlf = falaAlfabeto()
    else:
        time.sleep(0.01)
   
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
    
        gameDisplay.fill(white)
        imagem(loopImg,0,0)
        
        letraAtual = random.choice(alf)
        if letraAtual == "z":
            letraSeg = "a"
            letraSegMaisc = "A"
        else:    
            letraSeg = alf[alf.find(letraAtual)+1]
            letraSegMaisc = alfMaisc[alf.find(letraAtual)+1]
     
        frase1 = 'A letra é         '+"          "+ letraAtual +" ...         "
        pcLetra = gTTS(text=frase1, lang="pt", slow=False) 
        pcLetra.save(letraAtual+".mp3")
        mixer.init()
        mixer.music.load(letraAtual+".mp3")
        mixer.music.play()
        time.sleep(1.5)
                        
        frase2 = 'Qual é a letra seguinte?'
        pcLetra = gTTS(text=frase2, lang="pt", slow=False) 
        pcLetra.save("perguntaLetra.mp3")
        mixer.init()
        mixer.music.load("perguntaLetra.mp3")
        mixer.music.play()
        
        
        time.sleep(0.2)
        pontuacao(pontos)    
        mostra_letra_atual(letraAtual) 
        
        microfone  = sr.Recognizer()
                            
        with sr.Microphone() as source:
            #Chama um algoritmo de reducao de ruidos no som
            microfone.adjust_for_ambient_noise(source)
            time.sleep(0.01)
            audio = microfone.listen(source)
            time.sleep(0.752)
            
            try:
                pessoaFalou = microfone.recognize_google(audio,language="pt-BR")
           
                letraFalada = format(pessoaFalou)
               
                print("pessoaFalou: " + pessoaFalou)
                
                if letraFalada == letraSeg or letraFalada == letraSegMaisc :
                    pontos+=1
                    acertou(pontos)
                    print("Total : "+pontos)
                elif letraFalada != letraSeg or letraFalada != letraSegMaisc :
                    if letraSeg == "a" :
                        if letraFalada == "ah" or letraFalada == "A" or letraFalada == "á" or letraFalada == "Á":
                            pontos+=1
                            acertou(pontos)
                            print("Total : "+pontos)
                    if letraSeg == "b" :
                        if letraFalada == "be" or letraFalada == "bee" or letraFalada == "bê" or letraFalada == "Be" or letraFalada == "Bê" or letrafalada == "BE" or letraFalada == "BÊ":
                            pontos+=1
                            acertou(pontos)
                            print("Total : "+pontos)
                    if letraSeg == "c" :
                        if letraFalada == "ce"  or letraFalada == "ssê" or letraFalada == "cê" or letraFalada == "Ce" or letraFalada == "Cê" or letrafalada == "CE" or letraFalada == "CÊ":
                            pontos+=1
                            acertou(pontos)
                            print("Total : "+pontos)
                    if letraSeg == "d" :
                        if letraFalada == "de" or letraFalada == "dê" or letraFalada == "De" or letraFalada == "Dê" or letrafalada == "DE" or  letraFalada == "DÊ":
                            pontos+=1
                            acertou(pontos)
                            print("Total : "+pontos) 
                    if letraSeg == "e" :
                        if letraFalada == "ee" or letraFalada == "É" or letraFalada == "é" or letraFalada == "ê" or letraFalada == "eh" or letraFalada == "Ê" or letraFalada == "EE" :
                            pontos+=1
                            acertou(pontos)
                            print("Total : "+pontos)         
                    if letraSeg == "f" :
                        if letraFalada == "ef" or letraFalada == "éf" or letraFalada == "éfi" or letraFalada == "EF" or letraFalada == "EFE":
                            pontos+=1
                            acertou(pontos)
                            print("Total : "+pontos)
                    if letraSeg == "g" :
                        if letraFalada == "ge" or letraFalada == "gê" or letraFalada == "Ge" or letraFalada == "Gê" or letraFalada == "GÊ" or letrafalada == "GE":
                            pontos+=1
                            acertou(pontos)
                            print("Total : "+pontos)
                    if letraSeg == "h" :
                        if letraFalada == "agá" or letraFalada == "AGÁ":
                            pontos+=1
                            acertou(pontos)
                            print("Total : "+pontos)
                    if letraSeg == "i" :
                        if letraFalada == "ii" or letraFalada == "ih" or letraFalada == "í" or letraFalada == "íh"or letraFalada == "Í":
                            pontos+=1
                            acertou(pontos)
                            print("Total : "+pontos)        
                    if letraSeg == "j" :
                        if letraFalada == "jota" or letraFalada == "joota" or letraFalada == "Jota" or letraFalada == "JOTA" or letraFalada == "jóta" or letraFalada == "Jóta" or letrafalada == "JÓTA":
                            pontos+=1
                            acertou(pontos)
                            print("Total : "+pontos)
                    if letraSeg == "k" :
                        if letraFalada == "ca" or letraFalada == "cá" or letraFalada == "CA" or letraFalada == "CÁ" or letraFalada == "ka" or  letraFalada == "kah" or letrafalada == "KA" or letrafalada == "K":
                            pontos+=1
                            acertou(pontos)
                            print("Total : "+pontos)
                    if letraSeg == "l" :
                        if letraFalada == "éli" or letraFalada == "ÉLI" or letraFalada == "éle" or letraFalada == "ÉLE":
                            pontos+=1
                            acertou(pontos)
                            print("Total : "+pontos)
                    if letraSeg == "m" :
                        if letraFalada == "ême" or letraFalada == "Ême" or letraFalada == "ÊME" or letraFalada == "eme" or letraFalada == "Eme" or letrafalada == "EME":
                            pontos+=1
                            acertou(pontos)
                            print("Total : "+pontos)
                    if letraSeg == "n" :
                        if letraFalada == "êne" or letraFalada == "Êne" or letraFalada == "ÊNE" or letraFalada == "ene" or letraFalada == "Ene" or letrafalada == "ENE":
                            pontos+=1
                            acertou(pontos)
                            print("Total : "+pontos)
                    if letraSeg == "o" :
                        if letraFalada == "o" or letraFalada == "O" or letraFalada == "oh" or letraFalada == "ó" or letraFalada == "Ó" :
                            pontos+=1
                            acertou(pontos)
                            print("Total : "+pontos)        
                    if letraSeg == "p" :
                        if letraFalada == "pe" or letraFalada == "Pe" or letraFalada == "PE" or letraFalada == "pê" or letraFalada == "Pê" or letrafalada == "PÊ":
                            pontos+=1
                            acertou(pontos)
                            print("Total : "+pontos)
                    if letraSeg == "q" :
                        if letraFalada == "quê" or letraFalada == "Q" or letraFalada == "quÊ" or letraFalada == "Quê" or  letraFalada == "QUÊ" or letraFalada == "QUE" or letraFalada == "que":
                            pontos+=1
                            acertou(pontos)
                            print("Total : "+pontos)
                    if letraSeg == "r" :
                        if letraFalada == "eeri" or letraFalada == "érre"  or letraFalada == "erre" or letraFalada == "ERRE" or letraFalada == "Erre" or letraFalada == "Érre" or letrafalada == "ÉRRE":
                            pontos+=1
                            acertou(pontos)
                            print("Total : "+pontos)
                    if letraSeg == "s" :
                        if letraFalada == "ésse" or letraFalada == "Ésse" or letraFalada == "ÉSSE" or letraFalada == "éssi" or letraFalada == "Éssi" or letraFalada == "ÉSSI" :
                            pontos+=1
                            acertou(pontos)
                            print("Total : "+pontos) 
                    if letraSeg == "t" :
                        if letraFalada == "té" or letraFalada == "tê" or letraFalada == "Té" or letraFalada == "Tê" or letraFalada == "TÉ" or letraFalada == "TÊ" :
                            pontos+=1
                            acertou(pontos)
                            print("Total : "+pontos)
                    if letraSeg == "v" :
                        if letraFalada == "vê" or letraFalada == "Vê" or letraFalada == "VÊ" or letraFalada == "ver" :
                            pontos+=1
                            acertou(pontos)
                            print("Total : "+pontos)
                    if letraSeg == "w" :
                        if letraFalada == "dáblio" or letraFalada == "Dáblio" or letraFalada == "DÁblio" or letraFalada == "DÁBLIO" :
                            pontos+=1
                            acertou(pontos)
                            print("Total : "+pontos)
                    if letraSeg == "y" :
                        if letraFalada == "ípsilon" or letraFalada == "Ípsilon" or letraFalada == "ÍPsilon" or letraFalada == "ÍPSILON" or letraFalada == "ipsilon" or letraFalada == "ipsilon" or letraFalada == "IPsilon" or letraFalada == "IPSILON" :
                            pontos+=1
                            acertou(pontos)
                            print("Total : "+pontos)
                    if letraSeg == "z" :
                        if letraFalada == "zê" or letraFalada == "Zê" or letraFalada == "ZÊ" :
                            pontos+=1
                            acertou(pontos)
                            print("Total : "+pontos)        
                    pontos-=1
                    errou(pontos,letraSegMaisc)
                    print("Total : "+pontos)
                    
            except:
                mixer.init()
                mixer.music.load("hein.mp3")
                mixer.music.play()
                time.sleep(1) 
              
        pygame.display.update()
        clock.tick(60)

def game_intro():
    count = 0
    enter = False
    caps = False
    shift = False
    ctrl = False
    destaqC = False
    destaqSo = False
    destaqSa = False
   
    pcDiz(textIntro)
    pygame.event.wait()
    
    while True:
          
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
                count = count + 1
                print("Clicou TAB")
                if count == 1 :
                    print("clicou "+format(count)+" vezes")
                    destaqC = True
                    destaqSo = False
                    destaqSa = False
                    buttonNome("bcomeca.mp3")
                    time.sleep(0.9) 
                if count == 2 :
                    print("clicou "+format(count)+" vezes")
                    print("clicou sobre")
                    destaqSo = True
                    destaqC = False
                    destaqSa = False
                    buttonNome("bsobre.mp3")
                    time.sleep(0.8)
                if count == 3 :
                    print("clicou "+format(count)+" vezes")
                    destaqSa = True
                    destaqC = False
                    destaqSo = False
                    buttonNome("bsair.mp3")
                    time.sleep(0.75)
                    print("clicou sair")
                if count > 3:
                    if  count%3 == 1:
                        print("clicou "+format(count)+" vezes")
                        destaqC = True
                        destaqSo = False
                        destaqSa = False
                        buttonNome("bcomeca.mp3")
                        time.sleep(0.9)
                        print("clicou comeca")
                    if  count%3 == 2:
                        print("clicou "+format(count)+" vezes")
                        print("clicou sobre")
                        destaqSo = True
                        destaqC = False
                        destaqSa = False
                        buttonNome("bsobre.mp3")
                        time.sleep(0.8) 
                    if  count%3 == 0 :
                        print("clicou "+format(count)+" vezes")
                        destaqSa = True
                        destaqC = False
                        destaqSo = False
                        buttonNome("bsair.mp3")
                        time.sleep(0.75) 
                        print("clicou sair")
                      
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER)  :
                enter = True
                caps = False
                shift = False
                ctrl = False
                print("Clicou ENTER")
                if count == 1 and enter == True:
                        game_loop() 
                if count == 2 and enter == True:
                        sobre()
                if count == 3 and  enter == True:
                        quitgame()
                if count > 3:
                    if  count%3 == 1 and enter == True:
                        game_loop()
                    if  count%3 == 2 and enter == True:
                        sobre()
                    if  count%3 == 0 and enter == True:
                        quitgame() 
   
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_CAPSLOCK)  :
                enter = False
                caps=True
                shift = False
                ctrl = False
                print("Clicou CAPS")
                buttonNome("bcaps.mp3")
                time.sleep(1.23)
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT)  :
                enter = False
                caps = False
                shift=True
                ctrl = False
                print("Clicou SHIFT") 
                buttonNome("bshift.mp3")
                time.sleep(1.24)
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL)  :
                enter = False
                caps = False
                shift = False
                ctrl=True
                print("Clicou CONTROL")
                buttonNome("bcontrol.mp3")
                time.sleep(1.24)
                
        gameDisplay.fill(white)
        imagem(introImg,0,0)
        button("Começar",((display_width/10)-25),(display_height-(display_height/5)),200,100,green,bright_green,game_loop)
        button("Sobre",((display_width/10)+325),(display_height-(display_height/5)),200,100,yellow,light_yellow,sobre)
        button("Sair",((display_width/10)+650),(display_height-(display_height/5)),200,100,red,bright_red,quitgame)
        if destaqC == True:
            pygame.draw.rect(gameDisplay, bright_green,(((display_width/10)-25),(display_height-(display_height/5)),200,100),25)
        if destaqSo == True:
            pygame.draw.rect(gameDisplay, light_yellow,(((display_width/10)+325),(display_height-(display_height/5)),200,100),25)
        if destaqSa == True:
            pygame.draw.rect(gameDisplay, bright_red,(((display_width/10)+650),(display_height-(display_height/5)),200,100),25)  
        pygame.display.update()
            
game_intro()
sobre()
game_loop()
quitgame()           