# Importy bibliotek
import pygame
from random import randint
# from os import path

# Importy plików lokalnych
import globals
import map
import player
import enemy


class Game:
    def __init__(self):
        pygame.init()
        self.Colors = [globals.COLOR_BLACK, globals.COLOR_WHITE, globals.COLOR_RED, globals.COLOR_GREEN,
                       globals.COLOR_BLUE]
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 25)
        self.background = pygame.Surface((globals.WINDOW_X, globals.WINDOW_Y))
        self.background.fill(self.Colors[0])
        self.screen = pygame.display.set_mode((globals.WINDOW_X, globals.WINDOW_Y))
        pygame.display.set_caption("Pacman")
        # pygame.display.set_icon() # Przyda się potem

        # Obiekty gry
        self.playerObject = player.Player(globals.WINDOW_X / 2, globals.WINDOW_Y / 2 + 200)
        self.mapObject = map.Map()
        self.Enemies = []
        self.createEnemies(10)

    def drawGame(self):
        self.screen.blit(self.background, (0, 0))
        self.mapObject.drawMap(self.screen)
        self.playerObject.drawAndMove(self.screen, self.mapObject)
        self.drawEnemies()
        self.drawText()

    def createEnemies(self, numOfEnemies):
        for i in range(numOfEnemies):
            color = randint(2, 4)
            self.Enemies.append(enemy.Enemy(self.Colors[color]))

    def drawEnemies(self):
        for enemyObject in self.Enemies:
            if enemyObject.checkIfDead():
                del enemyObject
            else:
                enemyObject.drawAndMove(self.screen, self.playerObject, self.mapObject)

    def drawText(self):
        hpText = self.font.render(f"HP: {self.playerObject.hp}", True, globals.COLOR_WHITE, globals.COLOR_RED)
        self.screen.blit(hpText, (0, 0))

    def mainLoop(self):
        while True:
            globals.exitListener()
            self.drawGame()
            pygame.display.update()
            self.clock.tick(60)


Game = Game()
Game.mainLoop()
