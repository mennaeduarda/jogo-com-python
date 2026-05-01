import pygame
import os

pygame.init()

# Caminho para a pasta de imagens
BASE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(BASE, "images")

# Função para carregar a imagem
def load_image(name, width, height):
    path = os.path.join(IMG, name)
    image = pygame.image.load(path).convert_alpha()
    image = pygame.transform.scale(image, (width, height))
    return image

# Criar a janela
WIDTH = 720
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game 03 - Character")

# Carregar personagem
character = load_image("character.png", 85, 85)

# Posição inicial do personagem
x = 80
y = 600 # mais embaixo

# Loop principal
running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    # Cor de Fundo
    screen.fill((143, 119, 168))

    # Desenhar personagem
    screen.blit(character, (x,y))

    # Atualizar tela
    pygame.display.flip()

# Encerrar
pygame.quit()