import pygame
import random
from os import path
from sys import exit


pygame.init()

window_x = 800
window_y = 1000

player_x = 200
player_y = 250

player_grav = 0
wall_speed = 5
wall_up_gap = 100

background = pygame.image.load(path.dirname(__file__) + "/res/Background.png")

font = pygame.font.Font(path.dirname(__file__) + "/res/font.ttf",50)
font_color = "#222222"
score = font.render("Score:" + "0",False,font_color)
score_num = 0

player_surf = pygame.image.load(path.dirname(__file__) + "/res/Flapper.png")
player_rect = player_surf.get_rect(topleft = (player_x, player_y))

floortop_surf = pygame.image.load(path.dirname(__file__) + "/res/Floortop.png")
top_rect = floortop_surf.get_rect(topleft = (0, 0))
floor_rect = floortop_surf.get_rect(topleft = (0, window_y - 64))
rand = 0

wall_surf = pygame.image.load(path.dirname(__file__) + "/res/Wall.png")
wall_up_rect = wall_surf.get_rect(topleft = (window_x, -600 - wall_up_gap))
wall_dn_rect = wall_surf.get_rect(topleft = (window_x, 600))
# ODLEGŁOŚĆ MIĘDZY RURAMI 75px

deadFlap_surf = pygame.image.load(path.dirname(__file__) + "/res/DeadFlapper.png")
deadFlap_rect = deadFlap_surf.get_rect(topleft = (window_x + 500, 600))
vent_surf = pygame.image.load(path.dirname(__file__) + "/res/Vent.png")
vent_rect = vent_surf.get_rect(topleft = (window_x + 200, 200))

screen = pygame.display.set_mode((window_x,window_y))
pygame.display.set_caption("Flapper")
pygame.display.set_icon(player_surf)
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

#STEROWANIE
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w] or keys[pygame.K_SPACE]:
            player_grav = -5
    else:
        player_grav += 0.5

    player_rect.y += player_grav


#RUCH RUR
    wall_up_rect.x -= wall_speed
    wall_dn_rect.x -= wall_speed

#RUCH TŁA
#TODO RUCH WODY
    deadFlap_rect.x -= 2.5
    vent_rect.x -= 2.5
    floor_rect.x -= 2.5
    top_rect.x -= 2.5


    if deadFlap_rect.x <= -500:
        deadFlap_rect.x = window_x + 500

    if vent_rect.x <= -250:
        vent_rect.x = window_x + 200

    if floor_rect.x <= -575:
        floor_rect.x = 0
        top_rect.x = 0

#PRAWIDŁOWE PRZESUWANIE RUR
    if wall_up_rect.x <= 0 - wall_up_rect.width:
# W DÓŁ
        if rand <= 0 and wall_dn_rect.y < window_y - floor_rect.height - 300 - wall_up_gap:
            rand = random.randint(1, 300)
# W GÓRĘ
        elif rand > 0 and wall_dn_rect.y > top_rect.height + 300 + wall_up_gap: 
            rand = random.randint(-300, 1)
        else:
            rand = random.randint(-300, 300)
            wall_up_rect.y = -600 - wall_up_gap
            wall_dn_rect.y = 600

        wall_up_rect.x = window_x
        wall_up_rect.y += rand
        wall_dn_rect.x = window_x
        wall_dn_rect.y += rand

#PUNKTACJA
    if wall_dn_rect.x == window_x:
        score_num += 1
        score = font.render("Score:" + str(score_num),False, font_color)
        if score_num % 10 == 0:
            wall_speed += 1

#WARUNKI PRZEGRANEJ
    if player_rect.colliderect(floor_rect) or player_rect.colliderect(top_rect) or player_rect.colliderect(wall_up_rect) or player_rect.colliderect(wall_dn_rect):
        wall_up_rect.x = window_x
        wall_dn_rect.x = window_x
        player_grav = 0
        player_rect.y = player_y
        score_num = 0
        wall_speed = 5
        wall_up_rect.y = -650
        wall_dn_rect.y = 600
        score = font.render("Score:" + str(score_num),False, font_color)

    screen.blit(background, (0,0))    
    screen.blit(deadFlap_surf, deadFlap_rect)
    screen.blit(vent_surf, vent_rect)
    screen.blit(score,(0, 875))

    screen.blit(player_surf, player_rect)
    
    screen.blit(wall_surf, wall_up_rect)
    screen.blit(wall_surf, wall_dn_rect)
    screen.blit(floortop_surf, floor_rect)
    screen.blit(floortop_surf, top_rect)



    pygame.display.update()
    clock.tick(60)

    #DEBUG
    # print("Player",player_rect)
    # print("Floor",floor_rect)
    # print("Top",top_rect)
    # print("wallUP",wall_up_rect)
    # print("wallDN",wall_dn_rect)
    # print(rand)
    # print(top_rect.x)