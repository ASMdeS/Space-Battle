import pygame

pygame.init()

clock = pygame.time.Clock()


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

    def movimento(self, tecla_cima, tecla_baixo, tecla_esquerda, tecla_direita):
        self.tecla_cima = tecla_cima
        self.tecla_baixo = tecla_baixo
        self.tecla_esquerda = tecla_esquerda
        self.tecla_direita = tecla_direita

        keys = pygame.key.get_pressed()

        delta_time = clock.tick(60)
        # além de movimentar o jogador
        # essa funcao muda o atributo direcao do jogador
        # a partir da tecla que foi usada
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

        # mantem o jogador dentro da tela
        if self.quadrado.y < 0:
            self.quadrado.y = 0
        if self.quadrado.bottom > 640:
            self.quadrado.bottom = 640
        if self.quadrado.x < 0:
            self.quadrado.x = 0
        if self.quadrado.x > 568:
            self.quadrado.x = 568

    def mostrar_player(self, screen):
        """
        Método de desenhar bala,pontuacao, player e a vida
        """
        screen.blit(self.imagem, self.rect)
