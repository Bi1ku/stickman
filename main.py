import pygame
from sprites.player import Player
from sys import exit

pygame.init()
pygame.display.set_caption("Stickman")

screen = pygame.display.set_mode((1920, 1080))
screen.fill((255, 255, 255))
clock = pygame.time.Clock()
font = pygame.font.Font('font/LDFComicSans.ttf', 50)

player = pygame.sprite.GroupSingle(Player())
exit = font.render('exit', None, 'Black')
exit_rect = exit.get_rect(topleft=(500, 500))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((255, 255, 255))

    player.draw(screen)
    player.update()

    screen.blit(exit, exit_rect)
    mouse_pos = pygame.mouse.get_pos()
    if exit_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed() == (True, False, False):
        pygame.quit()
        exit()

    pygame.display.update()
    clock.tick(60)
