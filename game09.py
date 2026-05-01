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
pygame.display.set_caption("Game 08 - FINISHED GAME")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Tamanhos ajustados
SIZE_CHARACTER = 120
WIDTH_OBSTACLE = 90
HEIGHT_OBSTACLE = 100
SIZE_GOAL = 120

# Imagens
background = load_image("background.png", 720, 720)
character = load_image("character.png", SIZE_CHARACTER, SIZE_CHARACTER)
obstacle_img = load_image("obstacle.png", WIDTH_OBSTACLE, HEIGHT_OBSTACLE)
goal_img = load_image("goal.png", SIZE_GOAL, SIZE_GOAL)

# Chão visual do cenário
floor = 600

# Personagem
x = 70
y = floor - SIZE_CHARACTER
speed = 5

# Pulo
jumping = False
speed_jump = 0
strenght_jump = -25
gravity = 0.9

# Obstáculo e objetivo
obstacle_rect = pygame.Rect(
    360,
    floor - HEIGHT_OBSTACLE,
    WIDTH_OBSTACLE,
    HEIGHT_OBSTACLE
)

goal_rect = pygame.Rect(
    590,
    floor - SIZE_GOAL,
    SIZE_GOAL,
    SIZE_GOAL
)

message = ""
running = True

while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Movimento para direita
    if keys[pygame.K_RIGHT]:
        x += speed

    # Movimento para esquerda
    if keys[pygame.K_LEFT]:
        x -= speed

    # Pulo
    if keys[pygame.K_SPACE] and not jumping:
        jumping = True
        speed_jump = strenght_jump

    # Aplicando gravidade
    if jumping:
        y += speed_jump
        speed_jump += gravity

        if y >= floor - SIZE_CHARACTER:
            y = floor - SIZE_CHARACTER
            jumping = False

    # Caixa de colisão do personagem
    player = pygame.Rect(
        x + 25,
        y + 20,
        70,
        90
    )

    # Colisão com obstáculo
    if player.colliderect(obstacle_rect):
        x = 70
        y = floor - SIZE_CHARACTER
        message = "Tente novamente"

    # Colisão com objetivo
    if player.colliderect(goal_rect):
        message = "Você venceu"

    # Desenhar cenário
    screen.blit(background, (0, 0))
    screen.blit(obstacle_img, (obstacle_rect.x, obstacle_rect.y))
    screen.blit(goal_img, (goal_rect.x, goal_rect.y))
    screen.blit(character, (x, y))

    # Mostrar mensagem
    if message:
        text = font.render(message, True, (204, 0, 0))
        screen.blit(text, (30, 30))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()