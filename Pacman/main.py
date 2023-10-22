# Importy bibliotek
import pygame
from sys import exit
# from os import path

# Importy plików lokalnych
import globals
import player

pygame.init()

clock = pygame.time.Clock()

background = pygame.Surface((globals.WINDOW_X, globals.WINDOW_Y))
background.fill(globals.COLOR_BLACK)

screen = pygame.display.set_mode((globals.WINDOW_X, globals.WINDOW_Y))
pygame.display.set_caption("Pacman")
# pygame.display.set_icon() # Przyda się potem

Pacman = player.Player(100, 100, 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # PĘTLA GRY
    # -----------------
    screen.blit(background, (0, 0))
    Pacman.drawAndMove(screen)
    # -----------------
    pygame.display.update()
    clock.tick(60)
