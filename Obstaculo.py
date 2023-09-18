import pygame

pygame.init()
grupo_obstaculos = pygame.sprite.Group()

class Obstaculo():
    def __init__(self, imagem, x, y):
        self.imagem = pygame.image.load(imagem)
        img = self.imagem
        self.x = x
        self.y = y
        self.retangulo = pygame.Rect(x, y, img.get_width(), img.get_height())


    def mostrar_obstaculo(self, screen):
        screen.blit(self.imagem, self.retangulo)