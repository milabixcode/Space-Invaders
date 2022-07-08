from PPlay.window import *
from PPlay.mouse import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.sound import*
import pygame
from pygame import mixer

def rank():
    janela = Window(1280,720)

    teclado = janela.get_keyboard()

    espaco = GameImage("espaco.png")

    # Organizo o arquivo txt em ordem decrescente
    pontuacao = sorting('Pontuacao.txt')
    pontuacao.reverse()
    
    # Desenho o fundo
    espaco.draw()
    
    # Desenho a pontuacao
    altura = 150
    for i,conteudo in enumerate(pontuacao):
        janela.draw_text(str(i+1), (janela.width/2)-120, altura, size=36, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(("."), (janela.width/2)-100, altura, size=36, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(str(conteudo), (janela.width/2)-80, altura, size=36, font_name="Arial", bold=True,color=[255, 255, 255])
        altura += 45
        if i > 4:
            break

    while (True):
        if(teclado.key_pressed("ESC")):
            import menu
            menu.menu()

                
        # Desenha as instruçoes da janela
        janela.draw_text(("RANKING"), (janela.width / 2)-150, 50, size=48, font_name="Arial", bold=True,color=[255, 255, 255])
        
        janela.set_title("SpaceMila Invaders")
        
        janela.update()

def fimDoJogoDerrota(score):
    janela = Window(1280,720)
    
    teclado = janela.get_keyboard()
    
    espaco = GameImage("espaco.png")
    
    nome = input("Escreva seu nome: ")
    
    # Instancio o som da Derrota
    mixer.music.load("derrota.wav")
    mixer.music.set_volume(0.4)
    mixer.music.play(-1)
    
    # Abro o arquivo (leitura)
    arquivo = open('Pontuacao.txt', 'r')
    conteudo = arquivo.readlines()

    # Insiro o conteúdo
    conteudo.append(str(score) + " - " + nome + ".")
    arquivo.close()
    
    # Abre novamente o arquivo (escrita)
    arquivo = open('Pontuacao.txt', 'w')
    arquivo.writelines(conteudo)
    arquivo.close()
    
    while (True):
        # Desenho o fundo
        espaco.draw()

        # Volto pro menu
        if(teclado.key_pressed("ESC")):
            mixer.music.stop()
            import menu
            menu.MainMenu()
            
        janela.draw_text(("Você foi derrotado! Talvez vença na próxima, vacilão!"), (janela.width/2) - 400, janela.height/2 - 200, size=24, font_name="Arial", bold=True,color=[255, 255, 255])
        janela.draw_text(("Aperte 'ESC' para voltar ao menu"), (janela.width/2) - 250, (janela.height/2) - 100, size=24, font_name="Arial", bold=True,color=[255, 255, 255])
        
        # Instancio o titulo da janela  
        janela.set_title("SpaceMila Invaders")
        
        # Atualizo o GameLoop
        janela.update()
        
def sorting(file):
    arquivo = open(file)
    pontuacao = []
    for linha in arquivo:
        temp = linha.split(".")
        for i in temp:
            pontuacao.append(i)
    arquivo.close()
    pontuacao.sort()
    return pontuacao

    