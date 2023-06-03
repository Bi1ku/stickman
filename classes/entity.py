import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, image, pos, direction="r"):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.frame = 0
        self.gravity = 0
        self.direction = direction

    def apply_gravity(self):
        self.gravity += 1
        self.rect.bottom += self.gravity
        if self.rect.bottom >= 600:
            self.rect.bottom = 600
