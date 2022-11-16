import pygame
from sys import exit
import os

screen_x = int(input("Window x size(px): "))
screen_y = int(input("Window y size(px): "))

# WINDOW CONFIG
pygame.init()
#screen_x = 1000
#screen_y = 600
screen = pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

# BACKGROUND CONFIG
bg = pygame.Surface((screen_x,screen_y))
bg.fill('#000000')


# PLAYER CONFIG
player = pygame.image.load(os.path.dirname(__file__) +'/DVD-logo.png')

player_x = 0
player_y = 0
player_xv = 3
player_yv = 3


# MAIN LOOP (RENDER)
while True:
    
    #CLOSING ON X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # RENDER
    screen.blit(bg,(0,0))
    screen.blit(player,(player_x,player_y))
  
    # MOVEMENT
    player_x += player_xv
    player_y += player_yv

    if player_x <= 0 or player_x >= screen_x -160:
        player_xv *= -1

    if player_y <= 0 or player_y >= screen_y -115:
        player_yv *= -1


    #UPDATE
    pygame.display.update()
    clock.tick(60)