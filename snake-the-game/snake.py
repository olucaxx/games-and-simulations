import pygame

class Snake:
    def __init__(self):
        self.body_sections = [(24,22),(24,23),(24,24),(24,25),(24,26)]
        self.mov_direction = (0,-1)

    def get_new_direction(self, key):
        if key == pygame.K_UP:
            return (-1, 0)
        if key == pygame.K_DOWN:
            return (1, 0)
        if key == pygame.K_LEFT:
            return (0, -1)
        if key == pygame.K_RIGHT:
            return (0, 1)
        
    def change_direction(self, key) -> bool:
        new_direction = self.get_new_direction(key)

        if new_direction != (-self.mov_direction[0], -self.mov_direction[1]):
            self.mov_direction = new_direction

    def move(self):
        self.body_sections.insert(0, 
                                  (self.body_sections[0][0] + self.mov_direction[0],
                                   self.body_sections[0][1] + self.mov_direction[1])
        )
        self.body_sections.pop()