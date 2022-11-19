import pygame, csv
from os import path
from sys import exit


pygame.init()

window_x = 512
window_y = 256

player_x = window_x/2
player_y = window_y/2

tile_size = 16

screen = pygame.display.set_mode((window_x,window_y))
clock = pygame.time.Clock()

background = pygame.Surface((window_x,window_y))
background.fill(("#03f0ff"))

player_surf = pygame.image.load(path.dirname(__file__) + "/textures/player.png")
player_rect = player_surf.get_rect(topleft = (player_x, player_y))

mapname = path.dirname(__file__) + "/lvl/TestLvl.csv"

grass_img = pygame.image.load(path.dirname(__file__) + "/textures/grass.png")
dirt_img = pygame.image.load(path.dirname(__file__) + "/textures/dirt.png")
stone_img = pygame.image.load(path.dirname(__file__) + "/textures/stone.png")

game_map = []
tile_rects = []

def read_map(mapname):
    with open(mapname) as data:
        data = csv.reader(data,delimiter=",")
        for row in data:
            game_map.append(row)
        return game_map

read_map(mapname)

def render_map():
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            if tile == '3':
                screen.blit(grass_img, (x * tile_size, y * tile_size))
            elif tile == '4':
                screen.blit(dirt_img, (x * tile_size, y * tile_size))
            elif tile == '5':
                screen.blit(stone_img, (x * tile_size, y * tile_size))
            if tile != '-1':
                tile_rects.append(pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size))
            x += 1 
        y += 1


#TODO
def collisions(rect, tiles):
    hit_list =[]
    for tile in tiles:
        if rect.coliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect, movement, tiles):
    collision_types = {"top":False, "bot":False, "right":False, "left":False}
    rect.x = movement[0]
    hit_list = collisions(rect,tile)

    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types["right"] = True

        elif movement[0] < 0:
            rect.left = tile.right
            collision_types["left"] = True

    rect.y += movement[1]
    hit_list = collisions(rect, tile)

    for tile in hit_list:
        if movement[1] > 0:
            rect.bot = tile.top
            collision_types["bot"] = True

        elif movement[1] < 0:
            rect.top = tile.bot
            collision_types["top"] = True

    return rect, collision_types

while True:
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        player_rect.y -= 4
    if keys[pygame.K_a]:
        player_rect.x -= 2
    if keys[pygame.K_d]:
        player_rect.x += 2

    if player_rect.y > 128:
        player_rect.y += 0
    else:
        player_rect.y += 2

    screen.blit(background, (0,0))

    screen.blit(player_surf,player_rect)
    render_map()

  
    
    pygame.display.update()
    clock.tick(60)