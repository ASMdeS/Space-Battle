import pygame
from pygame.locals import *
from sys import exit
from Player import *
from Botao import *

pygame.init()
screen = pygame.display.set_mode((600, 640))
menu = pygame.image.load('images/menu.png')
musica_de_fundo = pygame.mixer.music.load('sounds/CXR ATK - Dimensions.mp3')
pygame.mixer.music.play(-1)

class Obstaculo():
    def __init__(self, imagem, x, y):
        self.imagem = pygame.image.load(imagem)
        img = self.imagem
        self.x = x
        self.y = y
        self.retangulo = pygame.Rect(x, y, img.get_width(), img.get_height())


    def mostrar_obstaculo(self, screen):
        screen.blit(self.imagem, self.retangulo)


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

    obstaculo1 = Obstaculo('images/obstaculo-1.png', 268, 140)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        player1.movimento(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
        player2.movimento(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)

        player1.mostrar_player(screen)
        player2.mostrar_player(screen)

        obstaculo1.mostrar_obstaculo(screen)

        pygame.display.update()
        screen.blit(mapa_background, (0, 0))


menu_principal()
