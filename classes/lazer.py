from classes.entity import Entity
import pygame


class Lazer(Entity):
    def __init__(self, pos, direction):
        self.image = pygame.Surface((10, 5))
        self.image.fill((255, 0, 0))
        super().__init__(self.image, pos, direction)

    def update(self):
        self.move()
        self.destroy()
