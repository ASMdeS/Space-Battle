import pygame
from pygame.locals import *
from sys import exit
from  components.Player import *
from  components.Botao import *
from  components.Obstaculo import *
from  components.Coletaveis import *
import random
import pygame.mixer

pygame.init()
pygame.mixer.init()
# Icone do Jogo
icone_jogo = pygame.image.load('images/menu.png')
pygame.display.set_icon(icone_jogo)
# Iniciar Tela
screen = pygame.display.set_mode((600, 640))
menu = pygame.image.load('images/menu.png')
# Musica de Fundo
musica_de_fundo = pygame.mixer.music.load('sounds/CXR ATK - Dimensions.mp3')
pygame.mixer.music.play(-1)
som_bala = pygame.mixer.Sound('sounds/smw_kick.wav')
som_vida = pygame.mixer.Sound('sounds/smw_power-up.wav')
som_velocidade = pygame.mixer.Sound('sounds/smw_hit_while_flying.wav')
som_tiro = pygame.mixer.Sound('sounds/smw_blaster-firing.wav')
som_gameover = pygame.mixer.Sound('sounds/game-over-arcade-6435.mp3')
som_colisao = pygame.mixer.Sound('sounds/smw_yoshi_fire.wav')
som_inicio = pygame.mixer.Sound('sounds/smw_keyhole_exit.wav')

# Fonte
fonte = pygame.font.SysFont('arial', 15, False, False)


# MENU DE INÍCIO DO JOGO
def menu_principal():
    while True:
        pygame.display.set_caption('Menu Principal')
        # CRIAÇÃO DOS BOTÕES
        botao_jogar = Botao('images/play_button.png', 195, 330)
        botao_sair = Botao('images/leave_button.png', 195, 455)
        botao_jogar.mostrar_botao(screen)
        botao_sair.mostrar_botao(screen)

        # FIM DE JOGO
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if botao_jogar.apertado(mouse_x, mouse_y, 330, 415):
                    # RODAR O JOGO
                    print('jogar')
                    # wsom_inicio.play()
                    jogar()
                if botao_sair.apertado(mouse_x, mouse_y, 455, 540):
                    # FECHA A JANELA
                    print('sair')
                    pygame.quit()
                    exit()

        pygame.display.update()
        screen.blit(menu, (0, 0))

# JOGO EM SI
def jogar():
    som_inicio.play()
    pygame.display.set_caption('Space Battle')
    mapa_background = pygame.image.load('images/map_background.png')
    player1 = Player('images/nave_1.png', 260, 530, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_f)
    player2 = Player('images/nave_2.png', 260, 70, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT,
                     pygame.K_RCTRL)
    lista_obstaculos = gerar_lista_obstaculos()
    gerenciador_itens = GerenciadorItensColecionaveis()

    while True:
        # Clock
        pygame.time.Clock().tick(30)

        mensagem_balas_1 = f'balas: {player1.balas_totais}'
        mensagem_balas_1_formatado = fonte.render(mensagem_balas_1, True, (255,255,255))
        mensagem_balas_2 = f'balas: {player2.balas_totais}'
        mensagem_balas_2_formatado = fonte.render(mensagem_balas_2, True, (255,255,255))

        mensagem_vidas_1 = f'vidas: {player1.vidas_totais}'
        mensagem_vidas_1_formatado = fonte.render(mensagem_vidas_1, True, (255,255,255))
        mensagem_vidas_2 = f'vidas: {player2.vidas_totais}'
        mensagem_vidas_2_formatado = fonte.render(mensagem_vidas_2, True, (255,255,255))

        mensagem_velocidade_1 = f'velocidade: {player1.velocidade_total}'
        mensagem_velocidade_1_formatado = fonte.render(mensagem_velocidade_1, True, (255,255,255))
        mensagem_velocidade_2 = f'velocidade: {player2.velocidade_total}'
        mensagem_velocidade_2_formatado = fonte.render(mensagem_velocidade_2, True, (255,255,255))

        imagem_coracao_vermelho = pygame.image.load("images/life.png")
        imagem_coracao = pygame.image.load("images/coracao_coletavel.png")
        imagem_bala = pygame.image.load("images/bala.png")
        imagem_balaazul = pygame.image.load("images/bala_coletada.png")
        imagem_coracaoreduzido = pygame.transform.scale(imagem_coracao_vermelho, (20, 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if random.random() < 0.09:  # Ajuste a probabilidade conforme necessário
            gerenciador_itens.gerar_item()

        player1.movimento(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, lista_obstaculos)
        player2.movimento(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, lista_obstaculos)
        player1.atirar(screen, imagem_bala, som_tiro)
        player2.atirar(screen, imagem_bala, som_tiro)
        player1.atirando_bala(screen, imagem_bala, lista_obstaculos, player2, som_colisao)
        player2.atirando_bala(screen, imagem_bala, lista_obstaculos, player1, som_colisao)

        player1.mostrar_player(screen)
        player2.mostrar_player(screen)

        for item in gerenciador_itens.itens:
            if pygame.sprite.collide_rect(player1, item):
                if item.name == "images/velocidade.png":
                    player1.velocidade_total += 5
                    if player1.velocidade < 20:
                        som_velocidade.play()
                        player1.velocidade += 5
            if pygame.sprite.collide_rect(player2, item):
                if item.name == "images/velocidade.png":
                    player2.velocidade_total += 5
                    if player2.velocidade < 20:
                        som_velocidade.play()
                        player2.velocidade += 5
            if pygame.sprite.collide_rect(player1, item):
                if item.name == "images/coracao_coletavel.png":
                    player1.vidas_totais += 1
                    if player1.vidas < 6:
                        som_vida.play()
                        player1.vidas += 1
            if pygame.sprite.collide_rect(player2, item):
                if item.name == "images/coracao_coletavel.png":
                    player2.vidas_totais += 1
                    if player2.vidas < 6:
                        som_vida.play()
                        player2.vidas += 1
            if pygame.sprite.collide_rect(player1, item):
                if item.name == "images/bala.png":
                    player1.balas_totais += 1
                    if player1.balas < 6:
                        som_bala.play()
                        player1.balas += 1
            if pygame.sprite.collide_rect(player2, item):
                if item.name == "images/bala.png":
                    player2.balas_totais += 1
                    if player2.balas < 6:
                        som_bala.play()
                        player2.balas += 1

        pygame.sprite.spritecollide(player1, gerenciador_itens.itens, True)
        pygame.sprite.spritecollide(player2, gerenciador_itens.itens, True)

        # CONDIÇÃO DE VITÓRIA
        if player1.vidas == 0:
            som_gameover.play()
            fim_de_jogo(player2.imagem)
        elif player2.vidas == 0:
            som_gameover.play()
            fim_de_jogo(player1.imagem)

        for obstaculo in lista_obstaculos:
            obstaculo.mostrar_obstaculo(screen)

        # Vidas dos Players
        for i in range(int(player1.vidas)):
            screen.blit(imagem_coracaoreduzido, (30 + (i * 20), 590))
        for i in range(int(player2.vidas)):
            screen.blit(imagem_coracaoreduzido, (30 + (i * 20), 30))

        # Balas dos Players
        for i in range(int(player1.balas)):
            screen.blit(imagem_balaazul, (30 + (i * 10), 612))
        for i in range(int(player2.balas)):
            screen.blit(imagem_balaazul, (30 + (i * 10), 20))

        gerenciador_itens.itens.update()
        gerenciador_itens.itens.draw(screen)

        screen.blit(mensagem_balas_1_formatado,(500,550))
        screen.blit(mensagem_balas_2_formatado,(500,20))
        screen.blit(mensagem_vidas_1_formatado,(500,570))
        screen.blit(mensagem_vidas_2_formatado,(500,40))
        screen.blit(mensagem_velocidade_1_formatado,(500,590))
        screen.blit(mensagem_velocidade_2_formatado,(500,60))

        pygame.display.update()
        screen.blit(mapa_background, (0, 0))

#FIM DO JOGO 
def fim_de_jogo(winner_img):
    while True:
        pygame.display.set_caption('Fim de jogo')
        fundo = pygame.image.load('images/endgame_menu.png')

        botao_reiniciar = Botao('images/restart_button.png', 195, 330)
        botao_sair = Botao('images/leave_button.png', 195, 455)
        botao_reiniciar.mostrar_botao(screen)
        botao_sair.mostrar_botao(screen)

        screen.blit(winner_img, (230, 272))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if botao_reiniciar.apertado(mouse_x, mouse_y, 330, 415):
                    # REINICIAR O JOGO
                    print('reiniciar')
                    jogar()
                    
                if botao_sair.apertado(mouse_x, mouse_y, 455, 540):
                    # FECHA A JANELA
                    print('sair')
                    pygame.quit()
                    exit()
        
        pygame.display.update()
        screen.blit(fundo, (0, 0))

screen = pygame.display.set_mode((600, 640))
menu_principal()

