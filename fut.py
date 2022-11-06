import os
import pygame
pygame.init()
os.system("cls")  
print('Começando o jogo de futebol')

largura = 453
altura = 612
tamanho = (largura,altura) #tupla imutavel
display = pygame.display.set_mode(tamanho)
fps = pygame.time.Clock()
pygame.display.set_caption("Jogo de Futebol")


branco = (255,255,255)
preto = (0,0,0)
cor = (170, 50, 7)
#Red Green Blue

fundo = pygame.image.load("assets/campo.jpg")
bola = pygame.image.load("assets/bola.png")
tamanhoxbola = 50
tamanhoybola = 50
posicaobolax = 225
posicaobolay = 305
movimentobolax = 0
movimentobolay = 0
velocidade = 5
#looping para ficar rodando o jogo
jogando = True

while jogando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                movimentobolax = velocidade * -1
            elif evento.key == pygame.K_RIGHT:
                movimentobolax = velocidade
            elif evento.key == pygame.K_UP:
                movimentobolay = velocidade * -1
            elif evento.key == pygame.K_DOWN:
                movimentobolay = velocidade
        elif evento.type == pygame.KEYUP:
            movimentobolax = 0
            movimentobolay = 0

    if posicaobolax + movimentobolax + tamanhoxbola < largura and posicaobolax + movimentobolax > 0:
        posicaobolax = posicaobolax + movimentobolax
   
    if posicaobolay + movimentobolay + tamanhoybola < altura and posicaobolay + movimentobolay >0:
        posicaobolay = posicaobolay + movimentobolay

    display.fill(branco)
    display.blit(fundo, (0, 0))
    posicao = (posicaobolax, posicaobolay)
    display.blit(bola, (posicaobolax, posicaobolay))
    #pygame.draw.circle(display, preto, posicao, 10)
    
    pygame.display.update()
    fps.tick(60)


print("Volte sempre")

