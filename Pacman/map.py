import pygame
import globals


class Map:

    def __init__(self):
        pygame.init()
        self.debugSize = 25
        self.surface = pygame.Surface((self.debugSize, self.debugSize))
        self.surface.fill(globals.COLOR_WHITE)
        self.colliders = []
        self.makeColliders()

    def makeColliders(self):
        posX = 0
        posY = 0
        for i in range(len(globals.lvlMap)):
            for j in range(len(globals.lvlMap[i])):
                if globals.lvlMap[i][j] == 1:
                    rect = self.surface.get_rect(topleft=(posX, posY))
                    self.colliders.append(rect)
                posX += self.debugSize
            posY += self.debugSize
            posX = 0

    def drawMap(self, screen):
        posX = 0
        posY = 0
        for i in range(len(globals.lvlMap)):
            for j in range(len(globals.lvlMap[i])):
                if globals.lvlMap[i][j] == 1:
                    screen.blit(self.surface, (posX, posY))
                posX += self.debugSize
            posY += self.debugSize
            posX = 0
