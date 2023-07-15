from classes.entity import Entity
from constants import SCREEN_WIDTH
from abc import ABC, abstractmethod


class Moveable(Entity, ABC):
    def __init__(self, image, pos, speed, direction):
        super().__init__(image, pos)
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
        if self.rect.left >= SCREEN_WIDTH or self.rect.right <= 0:
            self.kill()

    def move(self):
        if self.direction == "r":
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed

    @abstractmethod
    def update(self):
        pass
