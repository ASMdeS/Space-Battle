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


class Player():
    def __init__(self, imagem, x, y, tecla_cima, tecla_baixo, tecla_esquerda, tecla_direita, tecla_tiro):
        self.x = x
        self.y = y        
        self.quadrado = pygame.Rect(x, y, 30, 30)
        self.rect = self.quadrado
        self.imagem = pygame.image.load(imagem)
        self.tecla_cima = tecla_cima
        self.tecla_baixo = tecla_baixo
        self.tecla_esquerda = tecla_esquerda
        self.tecla_direita = tecla_direita
        self.tecla_tiro = tecla_tiro
        self.velocidade = 10

    def movimento(self, tecla_cima, tecla_baixo, tecla_esquerda,tecla_direita):
        self.tecla_cima = tecla_cima
        self.tecla_baixo = tecla_baixo
        self.tecla_esquerda = tecla_esquerda
        self.tecla_direita = tecla_direita

        keys = pygame.key.get_pressed()

        delta_time = clock.tick(60)
        #além de movimentar o jogador
        #essa funcao muda o atributo direcao do jogador
        #a partir da tecla que foi usada
        if keys[self.tecla_esquerda]:
            self.direcao = "esquerda"
            self.quadrado.x -= self.velocidade


        if keys[self.tecla_direita]:
            self.quadrado.x += self.velocidade
            self.direcao = "direita"


        if keys[self.tecla_cima]:
            self.quadrado.y -= self.velocidade
            self.direcao = "cima"


        if keys[self.tecla_baixo]:
            self.quadrado.y += self.velocidade
            self.direcao = "baixo"

        #mantem o jogador dentro da tela
        if self.quadrado.y<0:
            self.quadrado.y=0
        if self.quadrado.bottom>640:
            self.quadrado.bottom=640
        if self.quadrado.x<0:
            self.quadrado.x=0
        if self.quadrado.x>568:
            self.quadrado.x=568


    def mostrar_player(self, screen):
        """
        Método de desenhar bala,pontuacao, player e a vida
        """
        screen.blit(self.imagem, self.rect)

pygame.init()
screen = pygame.display.set_mode((600, 640))
menu = pygame.image.load('images/menu.png')
musica_de_fundo = pygame.mixer.music.load('sounds/CXR ATK - Dimensions.mp3')
pygame.mixer.music.play(-1)
clock = pygame.time.Clock()

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
    player1 = Player('images/nave_1.png', 260, 530, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_f )
    player2 = Player('images/nave_2.png', 260, 70, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_RCTRL )
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        player1.movimento(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
        player2.movimento(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)

        player1.mostrar_player(screen)
        player2.mostrar_player(screen)

        pygame.display.update()
        screen.blit(mapa_background, (0, 0))

menu_principal()
