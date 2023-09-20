import pygame 
import random 

class ItemColecionavel(pygame.sprite.Sprite):
    def __init__(self, imagem):
        super().__init__()
        self.image = pygame.image.load(imagem)  # Carregue a imagem do item
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, 600), random.randint(0, 640))
        

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
        if num_itens_na_tela < 8:
            probabilidades = [10,90]
            tipos_itens = ["images/velocidade.png", "images/bala.png"]
            tipo_item = random.choices(tipos_itens, weights=probabilidades)[0]
           
            novo_item = ItemColecionavel(tipo_item)
            self.itens.add(novo_item)
