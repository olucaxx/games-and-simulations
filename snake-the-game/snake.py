import pygame

# mapeamento dos botoes
KEY_MAP = {
    pygame.K_UP:    (-1, 0),
    pygame.K_DOWN:  (1, 0),
    pygame.K_LEFT:  (0, -1),
    pygame.K_RIGHT: (0, 1),
} 

class Snake:
    def __init__(self):
        self.body_sections = [(24,22),(24,23),(24,24),(24,25),(24,26)]
        self.mov_direction = (0,-1)

    def change_direction(self, key) -> bool:
        new_direction = KEY_MAP.get(key)

        # garante que tenhamos um movimento valido
        if new_direction is not None: 
            # garante que voce nao consiga andar de volta em si mesmo
            if new_direction != (-self.mov_direction[0], -self.mov_direction[1]):
                self.mov_direction = new_direction

    def move(self):
        self.body_sections.insert(0, 
                                  (self.body_sections[0][0] + self.mov_direction[0],
                                   self.body_sections[0][1] + self.mov_direction[1])
        )
        self.body_sections.pop()