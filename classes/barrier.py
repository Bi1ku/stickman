from classes.entity import Entity
import pygame

from classes.moveable import Moveable


class Barrier():
    def __init__(self, player, barrier):
        self.player = player
        self.barrier = barrier

    @staticmethod
    def zero_speed():
        Moveable.speed = 0
        Moveable.dash_speed = 0

    @staticmethod
    def reset_speed():
        Moveable.speed = 5
        Moveable.dash_speed = 20

    def check_collisions(self):
        collisions = pygame.sprite.spritecollide(
            self.player, self.barrier, False)

        if collisions:
            for collision_obj in collisions:
                if collision_obj.rect.left <= self.player.rect.right <= collision_obj.rect.left + 20:
                    if self.player.direction == 'r':
                        Barrier.zero_speed()
                    else:
                        Barrier.reset_speed()

                elif collision_obj.rect.right >= self.player.rect.left >= collision_obj.rect.right - 20:
                    if self.player.direction == 'l':
                        Barrier.zero_speed()
                    else:
                        Barrier.reset_speed()

                elif collision_obj.rect.bottom + 10 >= self.player.rect.top >= collision_obj.rect.top - 10:
                    self.player.gravity = 10

                elif self.player.jumping and collision_obj.rect.bottom >= self.player.rect.top:
                    self.player.jumping = False
                    Barrier.standing = True

        else:
            Barrier.reset_speed()
            Barrier.standing = False
            self.player.jumping = True
