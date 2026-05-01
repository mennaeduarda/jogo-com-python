import pygame
import os

pygame.init()

BASE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(BASE, "images")

def load_image(name, width, height):
    path = os.path.join(IMG, name)
    image = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(image, (width, height))

WIDTH = 720
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game 06 - Moves")

character = load_image("character.png", 85, 85)
obstacle = load_image("obstacle.png", 95, 95)
goal = load_image("goal.png", 75, 75)

floor = 650

x = 80
y = floor - 85
speed = 5

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

    screen.fill((143, 119, 168))

    screen.blit(character, (x, y))
    screen.blit(obstacle, (obstacle_x, obstacle_y))
    screen.blit(goal, (goal_x, goal_y))

    pygame.display.flip()