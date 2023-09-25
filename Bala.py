import pygame
class Bala:
    def __init__(self):


# Teremos três estados de bala: pronto (preparado), (recarregando) e (vazio)

bulletImg = pygame.image.load('images/bala.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

if bullet_state == "preparado":
    # Bala não aparecerá na tela
    # Posicao da bala será igual a do Player
if bullet_state == "recarregando":
    # Bala estará aparecendo na tela
    bulletY_change = 10
if bullet_state == "vazio":
    # Não há balas e não será possível atirar
