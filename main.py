import pygame
from pygame.locals import *
from sys import exit
from Player import *
from Botao import *
from Obstaculo import *
from Coletaveis import * 
import random

pygame.init()
screen = pygame.display.set_mode((600, 640))
menu = pygame.image.load('images/menu.png')
musica_de_fundo = pygame.mixer.music.load('sounds/CXR ATK - Dimensions.mp3')
pygame.mixer.music.play(-1)

# FUNÇÃO QUE MOSTRA O MENU PRINCIPAL
def menu_principal():
    while True:
        pygame.display.set_caption('Menu Principal')
        # CRIAÇÃO DOS BOTÕES
        botao_jogar = Botao('images/play_button.png', 195, 330)
        botao_sair = Botao('images/leave_button.png', 195, 455)
        botao_jogar.mostrar_botao(screen)
        botao_sair.mostrar_botao(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if botao_jogar.apertado(mouse_x, mouse_y, 330, 415):
                    # RODAR O JOGO
                    print('jogar')
                    jogar()
                if botao_sair.apertado(mouse_x, mouse_y, 455, 540):
                    # FECHA A JANELA
                    print('sair')
                    pygame.quit()
                    exit()
        pygame.display.update()
        screen.blit(menu, (0, 0))


def jogar():
    mapa_background = pygame.image.load('images/map_background.png')
    player1 = Player('images/nave_1.png', 260, 530, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_f)
    player2 = Player('images/nave_2.png', 260, 70, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT,
                     pygame.K_RCTRL)


    obstaculo1 = Obstaculo('images/obstaculo-1.png', 500, 280)
    obstaculo2 = Obstaculo('images/obstaculo-2.png', 450, 60)
    obstaculo2_2 = Obstaculo('images/obstaculo-2.png', 100, 410)
    obstaculo4_1 = Obstaculo('images/obstaculo-4.png', 368, 500)
    obstaculo4_2 = Obstaculo('images/obstaculo-4.png', 168, 100)
    obstaculo3 = Obstaculo('images/obstaculo-3.png', 284, 324)

    gerenciador_itens = GerenciadorItensColecionaveis()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        if random.random() < 0.009:  # Ajuste a probabilidade conforme necessário
            gerenciador_itens.gerar_item()

        player1.movimento(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
        player2.movimento(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)

        player1.mostrar_player(screen)
        player2.mostrar_player(screen)

        obstaculo1.mostrar_obstaculo(screen)
        obstaculo2.mostrar_obstaculo(screen)
        obstaculo2_2.mostrar_obstaculo(screen)
        obstaculo4_1.mostrar_obstaculo(screen)
        obstaculo4_2.mostrar_obstaculo(screen)
        obstaculo3.mostrar_obstaculo(screen)

        itens_colecionados = pygame.sprite.spritecollide(player1, gerenciador_itens.itens, True)
        itens_colecionados = pygame.sprite.spritecollide(player1, gerenciador_itens.itens, True)
        
        gerenciador_itens.itens.update()
        gerenciador_itens.itens.draw(screen)

        pygame.display.update()
        screen.blit(mapa_background, (0, 0))


menu_principal()
