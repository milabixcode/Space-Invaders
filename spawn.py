from PPlay.window import*
from PPlay.keyboard import*
from PPlay.gameimage import*
from PPlay.sprite import*
from PPlay.collision import*
from PPlay.sound import*

def spawn(matrizDeInimigos):    
    for i in range(3):
        linha = []
        for j in range(8):
            inimigo = Sprite("inimigo.png",1)
            if (j==0):
                inimigo.x = 0
            if (j==1):
                inimigo.x = 75
            if (j==2):
                inimigo.x = 150
            if (j==3):
                inimigo.x = 225
            if (j==4):
                inimigo.x = 300
            if (j==5):
                inimigo.x = 375
            if (j==6):
                inimigo.x = 450
            if (j==7):
                inimigo.x = 525
            if (i==0):
                inimigo.y = 0
            if (i==1):
                inimigo.y = 50
            if (i==2):
                inimigo.y = 100
            linha.append(inimigo)
        matrizDeInimigos.append(linha)

def draw(matrizDeInimigos):
    for i, linhaInimigo in enumerate(matrizDeInimigos):
        for j, inimigo in enumerate(linhaInimigo):
            inimigo.draw()

def moveInimigosD_E(janela, matrizDeInimigos, movimentoInimigo):
    bateu = False
    for i in matrizDeInimigos:
        for j in i:
            j.x += movimentoInimigo*janela.delta_time()
            if ((j.x >= janela.width - j.width - 5) or (j.x<0)):
                bateu = True
    if (bateu):
        movimentoInimigo *= -1
        for i in matrizDeInimigos:
            for j in i:
                j.x += movimentoInimigo*janela.delta_time()
                j.y += 50
    return movimentoInimigo

def destroiInimigo(matrizDeInimigos, listaProjeteis, pontuacao):
    for i, linhaInimigo in enumerate(matrizDeInimigos):
        for j, inimigo in enumerate(linhaInimigo):
            for k, projetil in enumerate(listaProjeteis):
                if(projetil.collided(inimigo)):
                    linhaInimigo.pop(j)
                    listaProjeteis.pop(k)
                    pontuacao += 10
        if(len(linhaInimigo) == 0):
            matrizDeInimigos.pop(i)    
    return pontuacao