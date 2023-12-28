from settings import *
import pygame,random
class Line_board:
    def __init__(self):
        self.length = 100
        self.color = "green"
        self.coord_x_random = random.randint(450, screenX - self.length)
        self.coord_y = screenY - 2 * indentation

    def static(self):
        pygame.draw.rect(screen, self.color, [self.coord_x_random, self.coord_y, self.length, self.length], 6)
        # pygame.draw.line(screen, "green", [self.coord_x_random, self.coord_y], [self.coord_x_random + self.length, self.coord_y], 5)