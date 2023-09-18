import pygame 
import random 

class ItemColecionavel(pygame.sprite.Sprite):
    def __init__(self, imagem, valor):
        super().__init__()
        self.image = pygame.image.load(imagem)  # Carregue a imagem do item
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, 600), random.randint(0, 640))
        self.valor = valor  # Um valor pa

    def update(self):
        # Você pode adicionar lógica adicional aqui se os itens colecionáveis precisarem ser atualizados
        pass

# Classe para gerenciar os itens colecionáveis
class GerenciadorItensColecionaveis:
    def __init__(self):
        self.itens = pygame.sprite.Group()

    def gerar_item(self):
        tipo_item = random.choice(["images/velocidade.png", "images/bala.png"])
        valor_item = 0

        if tipo_item == "images/velocidade.png":
            valor_item = 10
        elif tipo_item == "images/bala.png":
            valor_item = 90

        novo_item = ItemColecionavel(tipo_item, valor_item)
        self.itens.add(novo_item)
