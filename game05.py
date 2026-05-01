import pygame
import os

pygame.init()

# Caminho das imagens
BASE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(BASE, "images")

def load_image(name, width, height):
    path = os.path.join(IMG, name)
    image = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(image, (width, height))

# Tela
WIDTH = 720
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game 05 - Goal")

# Imagens
character = load_image("character.png", 85, 85)
obstacle = load_image("obstacle.png", 95, 95)
goal = load_image("goal.png", 75, 75)

# Chão (controle de altura)
floor = 650

# Posições
x = 80
y = floor - 85

obstacle_x = 390
obstacle_y = floor - 80

goal_x = 620
goal_y = floor - 75

# Loop
running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    screen.fill((143, 119, 168))

    screen.blit(character, (x, y))
    screen.blit(obstacle, (obstacle_x, obstacle_y))
    screen.blit(goal, (obstacle_x, obstacle_y))

    pygame.display.flip()

pygame.quit()