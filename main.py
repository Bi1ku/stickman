import pygame
from classes.player import Player
from sys import exit

pygame.init()
pygame.display.set_caption("Stickman")

screen = pygame.display.set_mode((800, 400), pygame.RESIZABLE)
screen.fill((255, 255, 255))
clock = pygame.time.Clock()

player = pygame.sprite.GroupSingle(Player())

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((255, 255, 255))

    player.draw(screen)
    player.update()

    pygame.display.update()
    clock.tick(60)
