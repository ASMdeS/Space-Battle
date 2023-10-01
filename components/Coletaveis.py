import pygame
import random

possiveis_posicoes_spawnaveis = [
    (111, 471),
    (500, 122),
    (378, 595),
    (235, 577),
    (36, 448),
    (485, 567),
    (329, 62),
    (541, 614),
    (137, 483),
    (82, 226),
    (111, 451),
    (502, 122),
    (378, 595),
    (235, 577),
    (36, 448),
    (485, 567),
    (329, 62),
    (541, 614),
    (137, 483),
    (82, 226),
    (385, 293),
    (135, 165),
    (247, 453),
    (264, 80),
    (175, 524),
    (58, 289),
    (221, 43),
    (552, 418),
    (450, 18),
    (396, 618),
    (321, 225),
    (491, 611),
    (589, 343),
    (530, 67),
    (376, 490),
    (9, 464),
    (141, 334)
]

class ItemColecionavel(pygame.sprite.Sprite):
    def __init__(self, name, imagem):
        super().__init__()
        self.name = name
        self.image = pygame.image.load(imagem)  # Carregue a imagem do item
        self.rect = self.image.get_rect()
        self.rect.center = (random.choice(possiveis_posicoes_spawnaveis))

    def update(self):
        # Você pode adicionar lógica adicional aqui se os itens colecionáveis precisarem ser atualizados
        pass

# Classe para gerenciar os itens colecionáveis
class GerenciadorItensColecionaveis:
    def __init__(self):
        self.itens = pygame.sprite.Group()

    def gerar_item(self):
        # Verifique o número atual de itens colecionáveis na tela
        num_itens_na_tela = len(self.itens)

        # Limite o número máximo de itens colecionáveis na tela a 8
        if num_itens_na_tela < 2:
            probabilidades = [10, 80, 10]
            tipos_itens = ["images/velocidade.png", "images/bala.png", "images/coracao_coletavel.png"]
            tipo_item = random.choices(tipos_itens, weights=probabilidades)[0]
            novo_item = ItemColecionavel(tipo_item, tipo_item)
            self.itens.add(novo_item)
