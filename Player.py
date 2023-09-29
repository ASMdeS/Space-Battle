import pygame
from Bala import *

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
        self.balas_totais = 0
        self.vidas_totais = 5
        self.velocidade_total = 10
        self.pode_atirar = False
        self.atirando = False
        self.x_bala = 0
        self.y_bala = 0
        self.direcao_bala = "parado"
        self.foi_atingido = False
        self.balas_group = pygame.sprite.Group()


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
            if self.balas > 0 and len(self.balas_group) == 0:
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
            if self.rect.colliderect(obstaculo.rect):
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

    def atirar(self, screen, imagem_bala, som_tiro):
        if self.pode_atirar:
            x_bala = self.quadrado.x + 16
            y_bala = self.quadrado.y + 16
            direcao_bala = self.direcao
            bala = Bala(x_bala, y_bala, direcao_bala, imagem_bala)
            self.balas_group.add(bala)
            self.pode_atirar = False
            self.balas -= 1
            som_tiro.play()
            

    def atirando_bala(self, screen, imagem_bala, lst_obst, player, som_colisao):
        self.balas_group.update()
        self.balas_group.draw(screen)
        
        for bala in self.balas_group.copy():
            if not pygame.Rect(0, 0, 600, 640).colliderect(bala.rect):
                self.balas_group.remove(bala)
            
            for obst in lst_obst:
                if pygame.sprite.collide_rect(bala, obst):
                    print('colidiu com obstáculo')
                    self.balas_group.remove(bala)
                    
            if pygame.sprite.collide_rect(bala, player) and player.foi_atingido == False:
                player.vidas -= 1
                som_colisao.play()
                print('colidiu com player')
                player.foi_atingido = True
                self.balas_group.remove(bala)

        self.quadrado_bala = pygame.Rect(self.x_bala, self.y_bala, 8, 8)
        if not self.quadrado_bala.colliderect(player.quadrado):
            player.foi_atingido = False

