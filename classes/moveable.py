from classes.entity import Entity
from constants import SCREEN_WIDTH
from abc import ABC, abstractmethod
import pygame


class Moveable(Entity, ABC):
    def __init__(self, image, pos, direction):
        super().__init__(image, pos)
        self.frame = 0
        self.gravity = 0
        self.direction = direction

        # Player Variables
        self.speed = 5
        self.dashing = 5
        self.last_dash = 0

    def apply_gravity(self):
        self.gravity += 1
        self.rect.bottom += self.gravity
        if self.rect.bottom >= 600:
            self.rect.bottom = 600

    def destroy(self):
        if self.rect.left >= SCREEN_WIDTH or self.rect.right <= 0:
            self.kill()

    def move(self):
        keys = pygame.key.get_pressed()
        dash = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]
        time = pygame.time.get_ticks()

        if int(self.dashing):
            if self.direction == "r":
                self.rect.x -= 20
            else:
                self.rect.x += 20

        else:
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.rect.x -= self.speed
                self.direction = "r"
            elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.rect.x += self.speed
                self.direction = "l"
            elif dash and time - self.last_dash >= 5000:
                self.last_dash = time
                self.dashing = 5

    @abstractmethod
    def update(self):
        pass
