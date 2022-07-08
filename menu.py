from PPlay.window import *
from PPlay.mouse import *
from PPlay.gameimage import *
from PPlay.sprite import *
import main
import difficult
import rank
import sair

def menu():
   
    janela = Window(1280,720)

    mouseClick = janela.get_mouse()

    playButton = Sprite("play.png")
    difficultButton = Sprite("difficult.png")
    rankingButton = Sprite("ranking.png")
    exitButton = Sprite("exit.png")

    while (True):
        if(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(playButton)):
            main.game(vidas = 3, movimento=200,movimentoInimigo=100,velocidadeProjetil=800,velocidadeProjetilInimigo=100,delay=0,delayInimigo=100,linha=4)
        if(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(difficultButton)):
            difficult.diff()
        if(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(rankingButton)):
            rank.rank()
        if(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(exitButton)):
            sair.sair()
        
        playButton.set_position(500, 190)
        difficultButton.set_position(500, 300)
        rankingButton.set_position(500, 410)
        exitButton.set_position(500, 520)

        janela.set_background_color([0,0,0])
        
        playButton.draw()
        difficultButton.draw()
        rankingButton.draw()
        exitButton.draw()
        
        janela.set_title("SpaceMila Invaders")

        janela.update()

menu()

