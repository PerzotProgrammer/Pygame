# Importy bibliotek
import pygame
from sys import exit
# from os import path

# Importy plików lokalnych
import globals
import player
import enemy


def exitListener():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.background = pygame.Surface((globals.WINDOW_X, globals.WINDOW_Y))
        self.background.fill(globals.COLOR_BLACK)
        self.screen = pygame.display.set_mode((globals.WINDOW_X, globals.WINDOW_Y))
        pygame.display.set_caption("Pacman")
        # pygame.display.set_icon() # Przyda się potem

        # Obiekty gry
        self.playerObject = player.Player(100, 100)
        self.enemy1 = enemy.Enemy(globals.COLOR_RED)
        self.enemy2 = enemy.Enemy(globals.COLOR_GREEN)
        self.enemy3 = enemy.Enemy(globals.COLOR_BLUE)

    def drawGame(self):
        self.screen.blit(self.background, (0, 0))
        self.playerObject.drawAndMove(self.screen)
        self.enemy1.drawAndMove(self.screen)
        self.enemy2.drawAndMove(self.screen)
        self.enemy3.drawAndMove(self.screen)

    def mainLoop(self):
        while True:
            exitListener()
            self.drawGame()
            pygame.display.update()
            self.clock.tick(60)


Game = Game()
Game.mainLoop()
