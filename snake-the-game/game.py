import pygame
import sys

from snake import Snake

# config
WIDTH = 20
HEIGHT = WIDTH
SCALE = 15
FPS = 5

# init 
pygame.init()
pygame.display.set_caption("snake the game")
screen = pygame.display.set_mode((WIDTH * SCALE, HEIGHT * SCALE))
clock = pygame.time.Clock()

running = True

snake = Snake(WIDTH)

while running:        
    # - EVENTOS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            snake.change_direction(event.key)

    snake.move()

    # - RENDERIZAR
    screen.fill((0,0,0))

    for y, x in snake.body_sections:
        pygame.draw.rect(
                    screen,
                    (255,255,255), 
                    (x * SCALE, y * SCALE, SCALE, SCALE)
                )

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
