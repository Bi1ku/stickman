from classes.barrier import Barrier
from classes.player import Player
import pygame
from sys import exit
from classes.tile import Tile
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
pygame.display.set_caption("Stickman")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((255, 255, 255))
clock = pygame.time.Clock()

pygame.mixer.Sound("sounds/music.mp3").play(loops=-1)

tiles = pygame.sprite.Group()
tiles.add(Tile((500, 600)))

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

    tiles.draw(screen)

    player_group.draw(screen)
    player_group.update()

    barrier.check_collisions()

    pygame.display.update()
    clock.tick(60)
