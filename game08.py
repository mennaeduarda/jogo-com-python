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
pygame.display.set_caption("Game 08 - Finished game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Imagens
background = load_image("background.png", 720, 720)
character = load_image("character.png", 80, 80)
obstacle_img = load_image("obstacle.png", 80, 80)
goal_img = load_image("goal.png", 75, 75)

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

# Obstáculo e objetivo
obstacle = pygame.Rect(390, floor - 80, 80, 80)
goal = pygame.Rect(620, floor - 75, 75, 75)

message = ""
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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

    player = pygame.Rect(x + 18, y + 12, 50, 68)

    if player.colliderect(obstacle):
        x = 80
        y = floor - 85
        message = "Tente novamente"

    if player.colliderect(goal):
        message = "Você venceu!"

    screen.blit(background, (0, 0))
    screen.blit(obstacle_img, (obstacle.x, obstacle.y))
    screen.blit(goal_img, (goal.x, goal.y))
    screen.blit(character, (x, y))

    if message:
        text = font.render(message, True, (204, 0, 0))
        screen.blit(text, (30, 30))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()