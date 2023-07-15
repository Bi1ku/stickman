import pygame
from constants import SCREEN_WIDTH


class Entity(pygame.sprite.Sprite):
    def __init__(self, image, pos, speed=0, direction="r"):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.frame = 0
        self.gravity = 0
        self.direction = direction
        self.speed = speed

    def apply_gravity(self):
        self.gravity += 1
        self.rect.bottom += self.gravity
        if self.rect.bottom >= 600:
            self.rect.bottom = 600

    def destroy(self):
        if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
            self.kill()

    def move(self):
        if self.direction == "r":
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed
