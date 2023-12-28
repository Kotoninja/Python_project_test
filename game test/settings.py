# from settings import *
import pygame, random

# setiing fot screen
screenX, screenY = 1920, 800
screen = pygame.display.set_mode((screenX, screenY))
clock = pygame.time.Clock()

indentation = 100
degree_line_indentation = 45
coord_line_stop_x = 450
y_coord_main_line = screenY - indentation
