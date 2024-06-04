from classes.entity import Entity
import pygame

from classes.moveable import Moveable


class Barrier():
    standing = False

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
            collision_obj = collisions[0]
            if int(self.player.dashing):
                print(collision_obj.rect.left, self.player.rect.right)

            if not Barrier.standing:
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

                elif self.player.jumping:
                    self.player.jumping = False
                    Barrier.standing = True

        else:
            Barrier.reset_speed()
            Barrier.standing = False
            self.player.jumping = True
