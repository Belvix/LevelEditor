import pygame, sys
from pygame.locals import *
from tkinter import *
import Elder as StartBox
import box as bb
import settings

settings.init()

pygame.init()

grass = pygame.image.load("Images/Grass.png")
dirt = pygame.image.load("Images/Dirt.png")
tile_size = grass.get_height()
changed = False
level = []
current_block = 1

rel = pygame.Vector2()


def create_level():
    for i in range(n_height):
        level.append([])
        for j in range(n_width):
            level[i].append('0')

WINDOW_SIZE = (1280, 720)
screen = pygame.display.set_mode(WINDOW_SIZE)
grass = grass.convert()
dirt = dirt.convert()

clock = pygame.time.Clock()

tiles = []
level_size = [0, 0, 0, 0]

camera = pygame.math.Vector2()
camera.x = 0
camera.y = 0
isdrag = False

player_location = [WINDOW_SIZE[0] / 2 - 32, WINDOW_SIZE[1] / 2 - 32]
player_w_location = []

run = True

tile_sizeZ = 32
grassre = pygame.transform.scale(grass, (tile_sizeZ, tile_sizeZ))
dirtre = pygame.transform.scale(dirt, (tile_sizeZ, tile_sizeZ))


def create_tile():
    y = 0
    for layer in level:
        x = 0
        level_size[2] = len(layer) * tile_size
        for tile in layer:
            if tile == '0':
                tiles.append(['dirt', [x , y]])
            if tile == '1':
                tiles.append(['grass', [x , y]])
            x += 1
        level_size[3] += tile_size
        y += 1


def block_change(x, y, c_block, level_pos, tile_size):
    global changed
    for tile in tiles:
        t_x = tile[1][0]*tile_size + level_pos[0]
        t_y = tile[1][1]*tile_size + level_pos[1]
        t_w = t_x + tile_size
        t_h = t_y + tile_size
        if t_x < x < t_w and t_y < y < t_h:
            if c_block == 1:
                tile[0] = 'dirt'
            if c_block == 2:
                tile[0] = 'grass'
    changed = False


def drag(x, y, level_s, dif):
    if 0-level_s[2]/2 < x-dif.x < WINDOW_SIZE[0] - level_s[2]/2:
        camera.x = -(x - dif.x)
        camera.y = -(y - dif.y)


# def zoom(num):
#     global tile_sizeZ
#
#
#     def lsizeupdate(size):
#         if level_size[2] != len(level[0] * size):
#             level_size[2] = len(level[0]) * size
#             camera.x += (num*len(level[0]))/2
#         if level_size[3] != len(level) * size:
#             level_size[3] = len(level) * size
#             camera.y += (num * len(level))/2
#     if tile_sizeZ>4 and tile_sizeZ + num!=0 and num<0:
#         tile_sizeZ = tile_sizeZ + num
#         lsizeupdate(tile_sizeZ)
#     elif tile_sizeZ < 128 and tile_sizeZ + num!=0 and num>0:
#         tile_sizeZ = tile_sizeZ + num
#         lsizeupdate(tile_sizeZ)


def zoom(num):
    global level_image
    global dirt
    level_image = pygame.transform.scale(temp_image,(level_image.get_width()+num*len(level[0]),level_image.get_height()+num*len(level)))
    camera.x += num*len(level[0])/2
    camera.y += num*len(level)/2
    level_size[2]=level_image.get_width()
    level_size[3]=level_image.get_height()
    #tile_sizeZ += num*len(level)


def get_input():
    global current_block
    global isdrag
    global grassre
    global dirtre
    global tile_sizeZ
    keys = pygame.key.get_pressed()
    mouse = [pygame.mouse.get_pressed(), pygame.mouse.get_pos()]
    if keys[pygame.K_a]:
        if l_size[0] + l_size[2] < WINDOW_SIZE[0]:
            camera.x -= 10
    if keys[pygame.K_d]:
        if l_size[0] > 0:
            camera.x += 10
    if keys[pygame.K_w]:
        if WINDOW_SIZE[1] > l_size[1] + l_size[3]:
            camera.y -= 10
    if keys[pygame.K_s]:
        if l_size[1] > 0:
            camera.y += 10

    if keys[pygame.K_1]:
        current_block = 1
    if keys[pygame.K_2]:
        current_block = 2

    if mouse[0][0] == 1:
        block_change(mouse[1][0], mouse[1][1], current_block, (level_size[0], level_size[1]), tile_sizeZ)

    #if level_size[0] + level_size[2] > mouse[1][0] > level_size[0] and level_size[1] + level_size[3] > mouse[1][1] > level_size[1]:
    if mouse[0][2]==1:
        if isdrag == False:
            rel.x = mouse[1][0] - level_size[0]
            rel.y = mouse[1][1] - level_size[1]
            isdrag = True

    if mouse[0][2] == 0:
        isdrag = False
    if isdrag:
        drag(mouse[1][0], mouse[1][1], level_size, rel)
    if keys[pygame.K_q]:
        zoom(-1)

    if keys[pygame.K_e]:
        zoom(1)

    if keys[pygame.K_p]:
        b = bb.Box()
        b.root.protocol("WM_DELETE_WINDOW", b.root.destroy)
        b.root.mainloop()
        #levelimage = screen.subsurface(level_size)
        #pygame.image.save(levelimage,"level.png")


def draw():
    global tiles
    global camera
    for tile in tiles:
        tilex = [tile[1][0]*tile_size, tile[1][1]*tile_size]
        if tile[0] == 'dirt':
            level_image.blit(dirt, tilex)
            print(tilex)

        if tile[0] == 'grass':
            level_image.blit(grass, tilex)
    for tile in tiles:
        tilex = [tile[1][0]*tile_size, tile[1][1]*tile_size]
        if tile[0] == 'dirt':
            temp_image.blit(dirt, tilex)
            print(tilex)

        if tile[0] == 'grass':
            temp_image.blit(grass, tilex)

def resize_level():
    while level_size[2:3]>list(WINDOW_SIZE):
        zoom(-1)
        #print(tile_sizeZ)
        #grassre = pygame.transform.scale(grass, (tile_sizeZ, tile_sizeZ))
        #dirtre = pygame.transform.scale(dirt, (tile_sizeZ, tile_sizeZ))


def tki():
    e = StartBox.Elder()
    e.root.mainloop()


def levelupdate(l_size):
    l_size[0] = -camera.x
    l_size[1] = -camera.y


tki()

n_height = settings.n_height
n_width = settings.n_width
create_level()
create_tile()
level_image = pygame.Surface((len(level[0])*tile_size,len(level)*tile_size))
temp_image = pygame.Surface((len(level[0])*tile_size,len(level)*tile_size))
print(level_size[2:4])
#resize_level()
camera.x = -(WINDOW_SIZE[0] / 2 - level_size[2] / 2)
camera.y = -(WINDOW_SIZE[1] / 2 - level_size[3] / 2)
while run:
    l_size = level_size
    screen.fill((0, 0, 0))
    levelupdate(l_size)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if changed == False:
        draw()
        changed=True
    screen.blit(level_image,[l_size[0],l_size[1]])
    pygame.display.update()
    get_input()
    clock.tick(60)
