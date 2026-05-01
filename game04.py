import pygame
import os

# Iniciar o pygame
pygame.init()

# Caminho da pasta de imagens
BASE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(BASE, "images")

# Função para carregar imagem
def load_image(name, width, height):
    path = os.path.join(IMG, name)
    image = pygame.image.load(path).convert_alpha()
    image = pygame.transform.scale(image, (width, height))
    return image

# Criar a janela
WIDTH = 720
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game 04 - Obstacle")

# Carregar imagens
character = load_image("character.png", 85, 85)
obstacle = load_image("obstacle.png", 90, 90)

# Posições
x = 80
y = 600 # mais embaixo

obstacle_x = 390
obstacle_y = 620 # alinhado com o chão

# Loop principal
running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    # Cor de fundo
    screen.fill((143, 119, 168))

    # Desenhar na tela
    screen.blit(character, (x, y))
    screen.blit(obstacle, (obstacle_x, obstacle_y))

    # Atualizar tela
    pygame.display.flip()

# Encerrar
pygame.quit()