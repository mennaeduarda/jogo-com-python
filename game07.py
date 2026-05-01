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
pygame.display.set_caption("Game 07 - Jump")

clock = pygame.time.Clock()

# Imagens
character = load_image("character.png", 85, 85)
obstacle = load_image("obstacle.png", 80, 80)
goal = load_image("goal.png", 75, 75)

# Chão
floor = 700

# Personagem
x = 80
y = floor - 85
speed = 5

# Pulo
jumping = False
speed_jump = 0
strength_jump = -20
gravity = 0.9

# Objetos
obstacle_x = 390
obstacle_y = floor - 80

goal_x = 620
goal_y = floor - 75

running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        x += speed

    if keys[pygame.K_LEFT]:
        x -= speed

    if keys[pygame.K_SPACE] and not jumping:
        jumping = True
        speed_jump = strength_jump

    if jumping:
        y += speed_jump
        speed_jump += gravity

        if y >= floor - 85:
            y = floor - 85
            jumping = False

    screen.fill((143, 119, 168))

    screen.blit(character, (x, y))
    screen.blit(obstacle, (obstacle_x, obstacle_y))
    screen.blit(goal, (goal_x, goal_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()