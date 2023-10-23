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
        self.speed = 2
        self.direction = randint(0, 3)
        self.debugSize = 25  # zmienna tymczasowa, dopóki nie ma tekstury
        self.time = 0
        self.timeDelay = 10  # milisekundy
        self.timeToChangeDirection = randint(0, 100)  # Delta time nie działa tak, jak bym chciał
        self.surf = pygame.Surface((self.debugSize, self.debugSize))
        self.rect = self.surf.get_rect(topleft=(self.posX, self.posY))
        self.rectSize = self.rect.size
        self.surf.fill(color)

    def drawAndMove(self, screen, playerRect):
        screen.blit(self.surf, (self.posX, self.posY))
        if self.deltaTime():
            self.movementControls()
            self.collisionDetection(playerRect)
            self.timeToChangeDirection += 1

    def deltaTime(self):
        ticks = pygame.time.get_ticks()
        if ticks - self.time > self.timeDelay:
            self.time = ticks
            return True
        return False

    def movementControls(self):
        if self.timeToChangeDirection == 100:
            self.direction = randint(0, 3)  # 0 - W, 1 - S, 2 - A, 3 - D
            self.timeToChangeDirection = 0
        if self.direction == 0 and self.posY > 0:
            self.posY -= self.speed
            self.rect.y -= self.speed
        if self.direction == 1 and self.posY < globals.WINDOW_Y - self.rectSize[1]:
            self.posY += self.speed
            self.rect.y += self.speed
        if self.direction == 2 and self.posX > 0:
            self.posX -= self.speed
            self.rect.x -= self.speed
        if self.direction == 3 and self.posX < globals.WINDOW_X - self.rectSize[0]:
            self.posX += self.speed
            self.rect.x += self.speed

    def collisionDetection(self, playerRect):
        if self.rect.colliderect(playerRect):
            print("COLLIDED")
