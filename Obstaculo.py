import pygame

pygame.init()
grupo_obstaculos = pygame.sprite.Group()

class Obstaculo():
    def __init__(self, imagem, x, y):
        self.imagem = pygame.image.load(imagem)
        img = self.imagem
        self.imagem_original = self.imagem
        self.x = x
        self.y = y
        self.retangulo = pygame.Rect(x, y, img.get_width(), img.get_height())
    
    def rotacionar_imagem(self, angle):
        # Rotaciona a imagem atual do jogador
        self.imagem = pygame.transform.rotate(self.imagem_original, angle)


    def mostrar_obstaculo(self, screen):
        screen.blit(self.imagem, self.retangulo)

    
obstaculo1 = Obstaculo('images/obstaculo-1.png', 100, 200)
obstaculo2 = Obstaculo('images/obstaculo-2.png', 450, 60)
obstaculo2_2 = Obstaculo('images/obstaculo-2.png', 100, 410)
obstaculo3 = Obstaculo('images/obstaculo-3.png', 284, 324)
obstaculo4_1 = Obstaculo('images/obstaculo-4.png', 168, 100)
obstaculo4_2 = Obstaculo('images/obstaculo-4.png', 110, 100)
obstaculo4_3 = Obstaculo('images/obstaculo-4.png', 52, 100)
obstaculo4_4 = Obstaculo('images/obstaculo-4.png', 368, 500)
obstaculo4_5 = Obstaculo('images/obstaculo-4.png', 426, 500)
obstaculo4_6 = Obstaculo('images/obstaculo-4.png', 484, 500)
obstaculo4_7 = Obstaculo('images/obstaculo-4.png', 450, 308)
obstaculo4_8 = Obstaculo('images/obstaculo-4.png', 450, 250)
obstaculo4_7.rotacionar_imagem(90)
obstaculo4_8.rotacionar_imagem(90)

lista_obstaculos = [obstaculo1, obstaculo2, obstaculo2_2, obstaculo3, obstaculo4_1, obstaculo4_2, obstaculo4_3, obstaculo4_4, obstaculo4_5, obstaculo4_6, obstaculo4_7, obstaculo4_8]

def gerar_lista_obstaculos():
    return lista_obstaculos