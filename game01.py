import pygame

# Iniciando o pygame, *init* é iniciar.
pygame.init()

# Definir o tamanho da janela. *display.set_mode é para "ditar" o modo da janela
WIDTH, HEIGHT = 720, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption ("Nome da Janela")

# Loop principal do jogo
running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    # Atualizando a tela
    pygame.display.flip()

# Finalizando o pygame
pygame.quit()