import pygame

class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y, direcao, img):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direcao = direcao
        self.velocidade = 10

    def update(self):
        if self.direcao == "esquerda":
            self.rect.x -= self.velocidade
        elif self.direcao == "direita":
            self.rect.x += self.velocidade
        elif self.direcao == "cima":
            self.rect.y -= self.velocidade
        elif self.direcao == "baixo":
            self.rect.y += self.velocidade
