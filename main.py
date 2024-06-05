from classes.barrier import Barrier
from classes.player import Player
import random
import pygame
from sys import exit
from classes.tile import Tile
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
pygame.display.set_caption("Stickman")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((255, 255, 255))
clock = pygame.time.Clock()

# pygame.mixer.Sound("sounds/music.mp3").play(loops=-1)

tiles = pygame.sprite.Group()
tiles.add(Tile((450, 550), "l"))
tiles.add(Tile((300, 500), "l"))

player = Player()
player_group = pygame.sprite.GroupSingle()
player_group.add(player)

barrier = Barrier(player, tiles)

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
