import pygame

pygame.init()


class Player:
    def __init__(self, imagem, x, y, tecla_cima, tecla_baixo, tecla_esquerda, tecla_direita, tecla_tiro):
        self.x = x
        self.y = y
        self.quadrado = pygame.Rect(x, y, 32, 32)
        self.rect = self.quadrado
        self.imagem_original = pygame.image.load(imagem)
        self.imagem = self.imagem_original
        self.tecla_cima = tecla_cima
        self.tecla_baixo = tecla_baixo
        self.tecla_esquerda = tecla_esquerda
        self.tecla_direita = tecla_direita
        self.tecla_tiro = tecla_tiro
        self.velocidade = 10
        self.direcao = "parado"
        self.vidas = 5
        self.balas = 0
        self.pode_atirar = False
        self.atirando = False
        self.x_bala = 0
        self.y_bala = 0
        self.direcao_bala = "parado"

    def rotacionar_imagem(self, angle):
        # Rotaciona a imagem atual do jogador
        self.imagem = pygame.transform.rotate(self.imagem_original, angle)

    def movimento(self, tecla_cima, tecla_baixo, tecla_esquerda, tecla_direita, lista_obst):
        self.tecla_cima = tecla_cima
        self.tecla_baixo = tecla_baixo
        self.tecla_esquerda = tecla_esquerda
        self.tecla_direita = tecla_direita

        old_position = self.rect.copy()
        keys = pygame.key.get_pressed()

        # além de movimentar o jogador
        # essa funcao muda o atributo direcao do jogador
        # a partir da tecla que foi usada
        if keys[self.tecla_esquerda]:
            self.direcao = "esquerda"
            self.quadrado.x -= self.velocidade
            self.rotacionar_imagem(90)  # Rotação para a esquerda

        if keys[self.tecla_direita]:
            self.quadrado.x += self.velocidade
            self.direcao = "direita"
            self.rotacionar_imagem(-90)  # Rotação para a direita

        if keys[self.tecla_cima]:
            self.quadrado.y -= self.velocidade
            self.direcao = "cima"
            self.rotacionar_imagem(0)  # Sem rotação

        if keys[self.tecla_baixo]:
            self.quadrado.y += self.velocidade
            self.direcao = "baixo"
            self.rotacionar_imagem(180)  # Rotação para baixo

        if keys[self.tecla_tiro]:
            if self.balas > 0:
                self.pode_atirar = True

        # mantem o jogador dentro da tela
        if self.quadrado.y < 0:
            self.quadrado.y = 0
        if self.quadrado.bottom > 640:
            self.quadrado.bottom = 640
        if self.quadrado.x < 0:
            self.quadrado.x = 0
        if self.quadrado.x > 568:
            self.quadrado.x = 568

        for obstaculo in lista_obst:
            if self.rect.colliderect(obstaculo.retangulo):
                if keys[tecla_esquerda]:
                    self.rect.left = old_position.left
                if keys[tecla_direita]:
                    self.rect.right = old_position.right
                if keys[tecla_cima]:
                    self.rect.top = old_position.top
                if keys[tecla_baixo]:
                    self.rect.bottom = old_position.bottom

    # A Função Colisão não é chamada. Discutir se deve ser remvovida 25/09
    def colisao(self, obj):
        if self.rect.colliderect(obj):
            return True
        return False

    def mostrar_player(self, screen):
        screen.blit(self.imagem, self.rect)

    def atirar(self, screen, imagem_bala):
        if self.pode_atirar:
            self.x_bala = self.quadrado.x + 16
            self.y_bala = self.quadrado.y + 16
            screen.blit(imagem_bala, (self.x_bala, self.y_bala))
            self.atirando = True
            self.pode_atirar = False
            self.direcao_bala = self.direcao
            self.balas -= 1

    def atirando_bala(self, screen, imagem_bala):
        if self.atirando:
            screen.blit(imagem_bala, (self.x_bala, self.y_bala))
            if self.direcao_bala == "esquerda":
                self.x_bala -= 10
            if self.direcao_bala == "direita":
                self.x_bala += 10
            if self.direcao_bala == "baixo":
                self.y_bala += 10
            if self.direcao_bala == "cima":
                self.y_bala -= 10
