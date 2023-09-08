import pygame
from pygame.locals import *
from sys import exit

class Botao():
    # CONSTRUTOR DA CLASSE
    def __init__(self, imagem, posx, posy): 
        self.x = posx
        self.y = posy
        self.image = pygame.image.load(imagem)
        self.rect = self.image.get_rect(center=(self.x, self.y))
    # COORDENADAS DO BOTÃO
    def coord(self):
        self.rect.topleft = self.x, self.y
    # CHECA SE HOUVE CLIQUE NA AREA DO BOTAO
    def apertado(self, mousx, mousy, top, bottom):
        if mousx in range(195, 405) and mousy in range(top, bottom):
            return True
        return False
    # MOSTRA O BOTÃO NA TELA
    def mostrar_botao(self, place):
        place.blit(self.image, (self.x, self.y))

pygame.init()
screen = pygame.display.set_mode((600, 640))
menu = pygame.image.load('Projeto_P1_aaef/images/menu.png')

# FUNÇÃO QUE MOSTRA O MENU PRINCIPAL
def menu_principal():
    while True:
        pygame.display.set_caption('Menu Principal')
        # CRIAÇÃO DOS BOTÕES
        botao_jogar = Botao('Projeto_P1_aaef/images/play_button.png', 195, 330)
        botao_sair = Botao('Projeto_P1_aaef/images/leave_button.png', 195, 455)
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
                if botao_sair.apertado(mouse_x,mouse_y, 455, 540):
                    # FECHA A JANELA
                    print('sair')
                    pygame.quit()
                    exit()
        pygame.display.update()
        screen.blit(menu, (0, 0))

menu_principal()