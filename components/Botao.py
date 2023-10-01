import pygame

pygame.init()


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
