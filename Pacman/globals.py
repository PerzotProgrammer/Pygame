import pygame
from sys import exit


WINDOW_X = 800
WINDOW_Y = 800

COLOR_BLACK = "#000000"
COLOR_WHITE = "#FFFFFF"
COLOR_RED = "#FF0000"
COLOR_GREEN = "#00FF00"
COLOR_BLUE = "#0000FF"
COLOR_YELLOW = "#FFFF00"


def exitListener():
    pygame.init()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
