# Importy bibliotek
import pygame

# Importy plików lokalnych
import globals


class Player:
    def __init__(self, posX, posY, speed):
        pygame.init()
        self.posX = posX
        self.posY = posY
        self.speed = speed
        self.surf = pygame.Surface((25, 25))
        self.rect = self.surf.get_rect(topleft=(posX, posY))
        self.surf.fill(globals.COLOR_WHITE)

    def drawAndMove(self, screen=pygame.display.set_mode((globals.WINDOW_X, globals.WINDOW_Y))):
        screen.blit(self.surf, (self.posX, self.posY))
        self.controls()

    def controls(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.posX > 0:
            self.posY -= self.speed
        if keys[pygame.K_s] and self.posX < globals.WINDOW_Y:
            self.posY += self.speed
        if keys[pygame.K_a] and self.posY > 0:
            self.posX -= self.speed
        if keys[pygame.K_d] and self.posY < globals.WINDOW_X:
            self.posX += self.speed
