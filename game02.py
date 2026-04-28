import pygame

pygame.int()

LARGURA, ALTURA = 720, 720
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Meu primeiro jogo")

# Variável com a cor do fundo em rgb!!
COR_FUNDO = (143, 119, 168)

running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    # Pintar o fundo da tela
    screen.fill(COR_FUNDO)
    

    pygame.display.flip()

pygame.quit()