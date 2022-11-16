import pygame
from time import sleep
from sys import exit
import os

pygame.init()
#Zmień jeżeli inna roździelczość
window_x = 1920
window_y = 1080
color = "#ffffff"


GameSpeed = 5


player1_x = 100
player1_y = window_y/2 - 100

player2_x = window_x - 100
player2_y = window_y/2 - 100

pxSize = 10
pySize = 200

ball_x = window_x/2
ball_y = window_y/2

ball_xv = GameSpeed
ball_yv = GameSpeed


pSpeed = GameSpeed + 10

p1 = 0
p2 = 0

pInit = pygame.font.Font(os.path.dirname(__file__) + "/res/font.ttf",100)

screen = pygame.display.set_mode((window_x,window_y),pygame.FULLSCREEN)
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()


background = pygame.Surface((window_x,window_y))
background.fill(("#000000"))

p1w = pInit.render("0",False,color)
p2w = pInit.render("0",False,color)

player1 = pygame.Surface((pxSize,pySize))
player1rect = player1.get_rect(topleft = (player1_x,player1_y))
player1.fill((color))

player2 = pygame.Surface((pxSize,pySize))
player2rect = player2.get_rect(topleft = (player2_x,player2_y))
player2.fill((color))

ball = pygame.Surface((15,15))
ballrect = ball.get_rect(topleft = (ball_x,ball_y))
ball.fill((color))

line = pygame.Surface((5,window_y))
line.fill((color))

PongBounce = pygame.mixer.Sound(os.path.dirname(__file__) + "/res/PongBounce.mp3")
PongScore = pygame.mixer.Sound(os.path.dirname(__file__) + "/res/PongScore.mp3")



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(background, (0,0))    
    screen.blit(line ,(window_x/2-2.5,0))
    screen.blit(player1, (player1_x,player1_y))
    screen.blit(player2, (player2_x,player2_y))
    screen.blit(ball, (ball_x,ball_y))
    screen.blit(p1w,(window_x-window_x/2+350,50))
    screen.blit(p2w,(window_x-window_x/2-450,50))




    keys = pygame.key.get_pressed()

    if keys[pygame.K_s] and player1_y < window_y - pySize:
        player1_y += pSpeed
        player1rect.y += pSpeed
    if keys[pygame.K_w] and player1_y > 0: 
        player1_y -= pSpeed
        player1rect.y -= pSpeed
    if keys[pygame.K_DOWN] and player2_y < window_y - pySize: 
        player2_y += pSpeed
        player2rect.y += pSpeed
    if keys[pygame.K_UP] and player2_y > 0: 
        player2_y -= pSpeed
        player2rect.y -= pSpeed

    if keys[pygame.K_ESCAPE]: 
        pygame.quit()
        exit()

    ball_x += ball_xv
    ballrect.x += ball_xv
    ball_y += ball_yv
    ballrect.y += ball_yv
    

    if player1rect.colliderect(ballrect) or player2rect.colliderect(ballrect):
        PongBounce.play()
        ball_xv *= -1

    if ball_y <= 0 or ball_y >= window_y:
        PongBounce.play()
        ball_yv *= -1

    if ball_x <= 0:
        ball_x = window_x/2
        ball_y = window_y/2 
        ballrect.x = ball_x
        ballrect.y = ball_y
        p1 += 1
        p1w = pInit.render(str(p1),False,color)
        PongScore.play()
        sleep(1)

    if ball_x >= window_x:
        ball_x = window_x/2
        ball_y = window_y/2
        ballrect.x = ball_x
        ballrect.y = ball_y
        p2 += 1
        p2w = pInit.render(str(p2),False,color)
        PongScore.play()
        sleep(1)
    
    
    pygame.display.update()
    clock.tick(60)