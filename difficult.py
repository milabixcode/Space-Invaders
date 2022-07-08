from PPlay.window import *
from PPlay.keyboard import *
from PPlay.mouse import *
from PPlay.sprite import *
import main

def diff():
    janela = Window(1280,720)

    teclado = janela.get_keyboard()

    mouseClick = janela.get_mouse()

    easy = Sprite("easy.png", 1)
    medium = Sprite("medium.png", 1)
    hard = Sprite("hard.png", 1)

    while (True):
        if(teclado.key_pressed("ESC")):
            import menu
            menu.menu()

        if(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(easy)):
            velocidadeOponente = 1
            velocidadePlayer = 2
            main.game(vidas = 3, movimento=100*velocidadePlayer,movimentoOponente=100*velocidadeOponente,velocidadeProjetil=800,velocidadeProjetilInimigo=400,delay=0)
            
        elif(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(medium)):
            velocidadeOponente = 3
            velocidadePlayer = 2
            main.game(vidas = 3, movimento=100*velocidadePlayer,movimentoOponente = 100*velocidadeOponente,velocidadeProjetil=800, velocidadeProjetilInimigo=600, delay=0)
            
        elif(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(hard)):
            velocidadeOponente = 5
            velocidadePlayer = 2
            main.game(vidas=3, movimento=100*velocidadePlayer,movimentoOponente=100*velocidadeOponente,velocidadeProjetil=800,velocidadeProjetilInimigo=800, delay=0)
        
        easy.set_position(550, 400)
        medium.set_position(550, 470)
        hard.set_position(550, 540)
        
        janela.draw_text(("DIFICULDADE"), (janela.width / 2)-225, 150, size=48, font_name="Arial", bold=True,color=[255, 255, 255])
        easy.draw()
        medium.draw()
        hard.draw()
        
        janela.set_title("SpaceMila Invaders")

        janela.update()


