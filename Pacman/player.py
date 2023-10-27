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
        self.direction = 4
        self.speed = 2
        self.debugSize = 25  # zmienna tymczasowa, dopóki nie ma tekstury
        self.time = 0
        self.timeDelay = 10  # milisekundy
        self.surf = pygame.Surface((self.debugSize, self.debugSize))
        self.rect = self.surf.get_rect(topleft=(self.posX, self.posY))
        self.rectSize = self.rect.size
        self.surf.fill(globals.COLOR_YELLOW)

    def drawAndMove(self, screen, mapObj):
        screen.blit(self.surf, (self.posX, self.posY))
        if self.deltaTime():
            self.collisionWithMapDetection(mapObj)
            self.movementControls()

    def deltaTime(self):
        ticks = pygame.time.get_ticks()
        if ticks - self.time > self.timeDelay:
            self.time = ticks
            return True
        return False

    def movementControls(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction = 0
        if keys[pygame.K_s]:
            self.direction = 1
        if keys[pygame.K_a]:
            self.direction = 2
        if keys[pygame.K_d]:
            self.direction = 3

        if self.direction == 0:
            self.posY -= self.speed
            self.rect.y -= self.speed
        if self.direction == 1:
            self.posY += self.speed
            self.rect.y += self.speed
        if self.direction == 2:
            self.posX -= self.speed
            self.rect.x -= self.speed
        if self.direction == 3:
            self.posX += self.speed
            self.rect.x += self.speed

    def collisionWithMapDetection(self, mapObj):
        for i in range(len(mapObj.colliders)):
            if mapObj.colliders[i].colliderect(self.rect):
                if self.direction == 0:
                    self.posY += self.speed
                    self.rect.y += self.speed
                if self.direction == 1:
                    self.posY -= self.speed
                    self.rect.y -= self.speed
                if self.direction == 2:
                    self.posX += self.speed
                    self.rect.x += self.speed
                if self.direction == 3:
                    self.posX -= self.speed
                    self.rect.x -= self.speed
