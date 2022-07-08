from PPlay.window import *
from PPlay.mouse import *
from PPlay.gameimage import *
from PPlay.sprite import *

def sair():
    janela = Window(1280,720)

    teclado = janela.get_keyboard()

    mouseClick = janela.get_mouse()

    simButton = Sprite("yes.png", 1)
    naoButton = Sprite("no.png", 1)

    while (True):
        if(teclado.key_pressed("ESC")):
            import menu
            menu.menu()
            
        janela.draw_text(("DESEJA MESMO SAIR?"), (janela.width / 2)-280, 150, size=48, font_name="Arial", bold=True,color=[255, 255, 255])
        if(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(simButton)):
            janela.close()
        if(mouseClick.is_button_pressed(1) and mouseClick.is_over_object(naoButton)):
            import menu
            menu.menu()

        simButton.set_position((janela.width/2) -200, (janela.height/2)+100)
        naoButton.set_position((janela.width/2) +50, (janela.height/2)+100)
        simButton.draw()
        naoButton.draw()
        janela.update()