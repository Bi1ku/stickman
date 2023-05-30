import pygame
from sprites.player import Player
from sys import exit

pygame.init()
pygame.display.set_caption("Stickman")

screen = pygame.display.set_mode((1920, 1080))
game_state = "main_menu"
screen.fill((255, 255, 255))
clock = pygame.time.Clock()
font = pygame.font.Font('font/LDFComicSans.ttf', 50)
title_font = pygame.font.Font('font/LDFComicSans.ttf', 150)
mouse_pos = pygame.mouse.get_pos()

player = pygame.sprite.GroupSingle(Player())
exit = font.render('exit', None, 'Black')
exit_rect = exit.get_rect(topleft=(0, 0))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game_state == "main_menu":
        screen.fill((0, 0, 0))
        title = title_font.render('Stickman', None, "White")
        title_rect = title.get_rect(center=(960, 200))

        settings = font.render('Settings', None, 'White')
        settings_rect = settings.get_rect(center=(960, 450))

        play = font.render('Play Game', None, "White")
        play_rect = play.get_rect(center=(960, 350))
        screen.blit(play, play_rect)
        if play_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed() == (True, False, False):
            game_state = "ingame"

        screen.blit(title, title_rect)

        screen.blit(exit, exit_rect)
        exit = font.render('EXIT GAME', None, 'White')
        exit_rect = exit.get_rect(center=(960, 550))
        mouse_pos = pygame.mouse.get_pos()
        if exit_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed() == (True, False, False):
            pygame.quit()
            exit()

        screen.blit(settings, settings_rect)

    if game_state == "ingame":
        screen.fill((255, 255, 255))

        player.draw(screen)
        player.update()

        screen.blit(exit, exit_rect)
        mouse_pos = pygame.mouse.get_pos()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            game_state = "paused"

    if game_state == "paused":
        screen.fill((193, 205, 193))
        pause_title = title_font.render('PAUSED', None, (139, 131, 134))
        pause_title_rect = pause_title.get_rect(center=(960, 200))

        resume = font.render('Resume', None, (139, 131, 134))
        resume_rect = resume.get_rect(center=(960, 350))

        return_main_menu = font.render(
            'Return To Main Menu', None, (139, 131, 134))
        return_main_menu_rect = return_main_menu.get_rect(center=(960, 450))

        screen.blit(pause_title, pause_title_rect)

        screen.blit(resume, resume_rect)
        if resume_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed() == (True, False, False):
            game_state = "ingame"

        screen.blit(return_main_menu, return_main_menu_rect)
        if return_main_menu_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed() == (True, False, False):
            game_state = "main_menu"

    pygame.display.update()
    clock.tick(60)
