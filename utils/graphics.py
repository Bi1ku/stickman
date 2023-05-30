import pygame


def load_graphic(path):
    return pygame.transform.rotozoom(pygame.image.load(path).convert_alpha(), 0, 0.25)
