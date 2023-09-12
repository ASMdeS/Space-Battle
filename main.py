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
menu = pygame.image.load('images/menu.png')
musica_de_fundo = pygame.mixer.music.load('sounds/CXR ATK - Dimensions.mp3')
pygame.mixer.music.play(-1)
clock = pygame.time.Clock()

# # Player 1
# playerwhite_Img = pygame.image.load('images/nave_1.png')
# playerwhite_X = 284
# playerwhite_Y = 50
# playerwhiteX_change = 0
# playerwhiteY_change = 0


# def player_white(x, y):
#     screen.blit(playerwhite_Img, (x, y))


# # Player 2
# playerred_Img = pygame.image.load('images/nave_2.png')
# playerred_X = 284
# playerred_Y = 558
# playerredX_change = 0
# playerredY_change = 0


# def player_red(x, y):
#     screen.blit(playerred_Img, (x, y))


# FUNÇÃO QUE MOSTRA O MENU PRINCIPAL
def menu_principal():
    while True:
        clock.tick(30) 
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
    player1 = Player('images/nave_1.png', 260, 530, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_f )
    player2 = Player('images/nave_2.png', 260, 70, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_RCTRL )
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerwhiteX_change = -5
                if event.key == pygame.K_RIGHT:
                    playerwhiteX_change = 5
                #if event.key == pygame.K_SPACE:
                    #if bullet_state == "ready":
                        #bulletX = playerX
                        #fire_bullet(bulletX, bulletY)
            #if event.type == pygame.KEYUP:
                #if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0
        screen.fill((0, 0, 0))

        playerwhite_X += playerwhiteX_change

        if playerX < 0:
            playerX = 0
        elif playerX > 736:
            playerX = 736

        player_white(playerwhite_X, playerwhite_Y)
        player_red(playerred_X, playerred_Y)
        pygame.display.update()


menu_principal()
