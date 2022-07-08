from PPlay.window import*
from PPlay.keyboard import*
from PPlay.gameimage import*
from PPlay.sprite import*
from PPlay.collision import*
from PPlay.sound import*
import rank

def spawn(numeroLinha,matrizDeInimigos):    
    for i in range(numeroLinha):
        linha = []
        for j in range(12):
            if numeroLinha < 6:
                if i == 0:
                    inimigoAtras = Sprite("inimigo.png",1)
                    inimigoAtras.x = 75 * j
                    inimigoAtras.y = 50 * i
                    linha.append(inimigoAtras)
                elif i == numeroLinha-1:
                    inimigoFrente = Sprite("inimigo.png",1)
                    inimigoFrente.x = 75 * j
                    inimigoFrente.y = 50 * i
                    linha.append(inimigoFrente)
                else:    
                    inimigoMeio = Sprite("inimigo.png",1)
                    inimigoMeio.x = 75 * j
                    inimigoMeio.y = 50 * i
                    linha.append(inimigoMeio)                
                    
            if numeroLinha >= 6:
                if i == 0:
                    inimigoAtras = Sprite("inimigo.png",1)
                    inimigoAtras.x = 75 * j
                    inimigoAtras.y = 50 * i
                    linha.append(inimigoAtras)
                elif i == numeroLinha-2:
                    inimigoFrente = Sprite("inimigo.png",1)
                    inimigoFrente.x = 75 * j
                    inimigoFrente.y = 50 * i
                    linha.append(inimigoFrente)
                else:    
                    inimigoMeio = Sprite("inimigo.png",1)
                    inimigoMeio.x = 75 * j
                    inimigoMeio.y = 50 * i
                    linha.append(inimigoMeio)
            
        matrizDeInimigos.append(linha)
    
def draw(matrizDeInimigos):
    for i in range(len(matrizDeInimigos)):
       for j in matrizDeInimigos[i]:
            j.draw()

def moveInimigos(janela, matrizDeInimigos, movimentoInimigo):
    bateu = False
    for i in matrizDeInimigos:
        for j in i:
            j.x += movimentoInimigo*janela.delta_time()
            if ((j.x >= janela.width - j.width + 5) or (j.x<-5)):
                bateu = True
    if (bateu):
        movimentoInimigo *= -1
        for i in matrizDeInimigos:
            for j in i:
                j.x += movimentoInimigo*janela.delta_time()
                j.y += 50
    return movimentoInimigo

def kill(listaProjeteis,matrizDeInimigos,score,linha,movimentoInimigo):
    for k,linhaDeInimigos in enumerate(matrizDeInimigos):
        for i,inimigo in enumerate(linhaDeInimigos):
            for j,projetil in enumerate(listaProjeteis):
                if (projetil.collided(inimigo)):
                    listaProjeteis.pop(j)
                    linhaDeInimigos.pop(i)
                    if k==0:
                        score+=30
                    elif k==linha-1:
                        score+=10
                    else:
                        score+=20
                    movimentoInimigo*=1.01
    return score, movimentoInimigo

def hit(vidas,player,listaDeInimigos,listaProjeteisInimigos,score):
    for i,projetil in enumerate(listaProjeteisInimigos):
        if (projetil.collided(player)):
            listaProjeteisInimigos.pop(i)
            vidas-=1
    
    for i,inimigo in enumerate(listaDeInimigos):
        if (inimigo.y>=player.y):
            rank.fimDoJogoDerrota(score)
    
    return vidas