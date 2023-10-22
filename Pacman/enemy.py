# Importy bibliotek
import pygame
from random import randint

# Importy plików lokalnych
import globals


class Enemy:
    def __init__(self, color):
        pygame.init()
        self.posX = randint(0, globals.WINDOW_X - 25)
        self.posY = randint(0, globals.WINDOW_Y - 25)
        self.speed = 5
        self.debugSize = 25  # zmienna tymczasowa, dopóki nie ma tekstury
        self.time = 0
        self.timeDelay = 10  # milisekundy
        self.surf = pygame.Surface((self.debugSize, self.debugSize))
        self.rect = self.surf.get_rect(topleft=(self.posX, self.posY))
        self.rectSize = self.rect.size
        self.surf.fill(color)

    def drawAndMove(self, screen):
        screen.blit(self.surf, (self.posX, self.posY))
        if self.deltaTime():
            self.movementControls()

    def deltaTime(self):
        ticks = pygame.time.get_ticks()
        if ticks - self.time > self.timeDelay:
            self.time = ticks
            return True
        return False

    def movementControls(self):
        pass
