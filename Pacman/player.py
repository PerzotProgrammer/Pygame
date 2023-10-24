# Importy bibliotek
import pygame

# Importy plików lokalnych
import globals


class Player:
    def __init__(self, posX, posY):
        pygame.init()
        self.posX = posX
        self.posY = posY
        self.hp = 100
        self.speed = 2
        self.debugSize = 25  # zmienna tymczasowa, dopóki nie ma tekstury
        self.time = 0
        self.timeDelay = 10  # milisekundy
        self.surf = pygame.Surface((self.debugSize, self.debugSize))
        self.rect = self.surf.get_rect(topleft=(self.posX, self.posY))
        self.rectSize = self.rect.size
        self.surf.fill(globals.COLOR_WHITE)

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
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.posY > 0:
            self.posY -= self.speed
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.posY < globals.WINDOW_Y - self.rectSize[1]:
            self.posY += self.speed
            self.rect.y += self.speed
        if keys[pygame.K_a] and self.posX > 0:
            self.posX -= self.speed
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.posX < globals.WINDOW_X - self.rectSize[0]:
            self.posX += self.speed
            self.rect.x += self.speed
