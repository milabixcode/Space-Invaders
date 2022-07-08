from PPlay.window import*
from PPlay.keyboard import*
from PPlay.gameimage import*
from PPlay.gameobject import*
from PPlay.sprite import*
from PPlay.collision import*
import Player
import inimigo
import tiro
import pygame
from pygame import mixer

def game(vidas,movimento,movimentoInimigo,velocidadeProjetil,velocidadeProjetilInimigo,delay,delayInimigo,linha):
    #Tamanho da janela
    janela = Window(1280,720)

    #Teclado
    teclado = janela.get_keyboard()

    #Objetos do jogo
    espaco = GameImage("espaco.png")
    player = Sprite("nave.png",1)
    playerInvencible = Sprite("naveInvencivel.png",1)
   
    #Definição da posição do player
    player.x = janela.width/2
    player.y = janela.height - player.height - 20

    # Instancio o som do jogo
    mixer.music.load("music.wav")
    mixer.music.set_volume(0.3)
    mixer.music.play(-1)

    # Defino o fps
    FPS = 60
    clock = pygame.time.Clock()

    # Criação do vetor de projeteis do inimigo
    listaProjeteis = []
    listaProjeteisInimigos = [] 

    # Criação do vetor de inimigos
    matrizDeInimigos = []

    # Crio a pontuaçao que os aliens dão e o delay de invencibilidade
    score = 0
    delayInvencible = 0
    TomeiDano=False 

    #GameLoop
    while (True):
        # Desenho o fundo
        espaco.draw()

        # Conto FPS
        clock.tick(FPS)  

        # Volta para o menu do jogo
        if(teclado.key_pressed("ESC")):
            mixer.music.stop()
            import menu
            menu.menu()

      # Faço a movimentação do personagem
        Player.player(janela,teclado,player,movimento)
        
        # Crio os inimigos
        if (len(matrizDeInimigos)==0):
            inimigo.spawn(linha,matrizDeInimigos)

        # Recrio a matriz apos matar todos os aliens
        for i in matrizDeInimigos:
            if (len(i) == 0):
                vazio = True
            else:
                vazio = False
                break
        if vazio:    
            matrizDeInimigos.clear()
            player.x = janela.width/2-player.width/2
            delayInvencible = 180
            if linha < 6:
                linha += 1
                movimentoInimigo*=1.02
            if linha<6:
                inimigo.spawn(linha,matrizDeInimigos)

        # Faço o movimento dos inimigos
        movimentoInimigo = inimigo.moveInimigos(janela, matrizDeInimigos, movimentoInimigo)
            
        # Chamo a funçao que irá lidar com a criaçao dos tiros
        if (teclado.key_pressed("SPACE") and delay==0):
            tiro.recarga(janela, player,listaProjeteis)
            delay = tiro.delay(linha,delay)
        if (delayInimigo == 0):
            for i in matrizDeInimigos:
                for j in i:
                    tiro.recargaInimiga(j,listaProjeteisInimigos)
            delayInimigo = tiro.delayInimigo(linha ,delayInimigo)
            
        # Faço o movimento dos tiros
        tiro.tiroPlayer(janela,listaProjeteis,velocidadeProjetil)
        tiro.tiroInimigo(janela,listaProjeteisInimigos,velocidadeProjetilInimigo)
        if delay > 0:
            delay -= 1
        if delayInimigo > 0:
            delayInimigo-=1
        
        if delayInvencible > 0:
            delayInvencible -= 1
            playerInvencible.x = player.x
            playerInvencible.y = player.y
            playerInvencible.draw()
        else:
            player.draw()

         # Verifico se alguem tomou hit
        vidasAntes = vidas
        score, movimentoInimigo = inimigo.kill(listaProjeteis,matrizDeInimigos,score,linha,movimentoInimigo)
        if (vidas>0 and delayInvencible==0):
            for i in matrizDeInimigos:
                vidas = inimigo.hit(vidas, player, i, listaProjeteisInimigos,score)
                if vidas != vidasAntes:
                    TomeiDano=True
        if TomeiDano:
            player.x= janela.width/2-player.width/2
            delayInvencible=180
            TomeiDano=False
        
       # Desenho os inimigos
        inimigo.draw(matrizDeInimigos)
        
        # Perco o jogo
        if (vidas <= 0):
            mixer.music.stop()
            import rank
            rank.fimDoJogoDerrota(score) 
        
         # Desenho a pontuação
        janela.draw_text(("Score: "), janela.width-130, 0, size=20, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(str(score), janela.width-50, 0, size=20, font_name="Arial", bold=True,color=[255, 255, 255])
        
        # Desenho a vida
        janela.draw_text(("Vidas: "), 0, 0, size=24, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(str(vidas), 75, 0, size=24, font_name="Arial", bold=True,color=[255, 0, 0])

        # Instancio o titulo da janela  
        janela.set_title("SpaceMila Invaders")
        
        # Finalizo o Gameloop
        janela.update()


       