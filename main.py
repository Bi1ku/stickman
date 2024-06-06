from pygame.rect import Rect
from classes.barrier import Barrier
from classes.player import Player
import pygame
from sys import exit
from classes.tile import Tile
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import random

pygame.init()
pygame.display.set_caption("Stickman")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((255, 255, 255))
clock = pygame.time.Clock()

# pygame.mixer.Sound("sounds/music.mp3").play(loops=-1)

tiles = pygame.sprite.Group()
tiles.add(Tile((450, 550), "l"))
tiles.add(Tile((300, 500), "l"))
tiles.add(Tile((200, 425), "l"))
tiles.add(Tile((300, 500), "l"))

player = Player()
player_group = pygame.sprite.GroupSingle()
player_group.add(player)

barrier = Barrier(player, tiles)

map = [[0] * 8] * 8
print(map)


def col(index):
    return [row[index] for row in map]


def procedural_generation():
    # KEY: 0 = EMPTY; 1 = WALL; 2 = PLAYER; 3 = ENEMY; 4 = COIN

    offset_x = SCREEN_WIDTH / 8
    offset_y = SCREEN_HEIGHT / 8
    for row in range(8, 0, -1):
        for column in range(8, 0, -1):
            mid_point = (offset_x * column - offset_x /
                         2, offset_y * row - offset_y / 2)
            rect = Rect(0, 0, 5, 5)
            rect.center = (round(mid_point[0]), round(mid_point[1]))

            pygame.draw.rect(screen, "black", rect)

            gap = random.randint(0, 3)
            up = random.randint(0, 2)
            down = random.randint(0, 2)

            if column > 5 and row <= 7:
                # if up probability, the point y down 100 is less than player y or there's a tile already that can lead up, and there's no tile in that column yet
                if up == 1 and (player.rect.y < mid_point[1] + 100 or map[row - 2][column - 2] == 1) and not 1 in col(column - 2):
                    map[row - 1][column - 1] = 1
                    tiles.add(Tile(mid_point, "l"))


procedural_generation()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((255, 255, 255))

    barrier.check_collisions()

    player_group.draw(screen)
    player_group.update()

    tiles.draw(screen)
    tiles.update()

    pygame.display.update()
    clock.tick(60)
