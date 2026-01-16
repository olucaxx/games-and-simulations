import pygame
import sys

# config
WIDTH = 50
HEIGHT = 50
SCALE = 15
FPS = 5

# init 
pygame.init()
pygame.display.set_caption("snake the game")
screen = pygame.display.set_mode((WIDTH * SCALE, HEIGHT * SCALE))
clock = pygame.time.Clock()

running = True

class Snake:
    def __init__(self):
        self.body_sections = [(24,22),(24,23),(24,24),(24,25),(24,26)]
        self.mov_direction = (0,-1)

    def change_direction(self, key):
        if key == pygame.K_UP:
            self.mov_direction = (-1, 0)
            return 
        if key == pygame.K_DOWN:
            self.mov_direction = (1, 0)
            return
        if key == pygame.K_LEFT:
            self.mov_direction = (0, -1)
            return
        if key == pygame.K_RIGHT:
            self.mov_direction = (0, 1)
            return

    def move(self):
        self.body_sections.insert(0, 
                                  (self.body_sections[0][0] + self.mov_direction[0],
                                   self.body_sections[0][1] + self.mov_direction[1])
        )
        self.body_sections.pop()

snake = Snake()

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

    for y,x in snake.body_sections:
        pygame.draw.rect(
                    screen,
                    (255,255,255), 
                    (x * SCALE, y * SCALE, SCALE, SCALE)
                )

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
