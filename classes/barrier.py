from classes.entity import Entity
import pygame

from classes.moveable import Moveable


class Barrier():
    standing = False

    def __init__(self, player, barrier):
        self.player = player
        self.barrier = barrier

    def check_collisions(self):
        print(Barrier.standing)
        collisions = pygame.sprite.spritecollide(
            self.player, self.barrier, False)

        if collisions:
            collision_obj = collisions[0]

            if not Barrier.standing:
                if collision_obj.rect.left <= self.player.rect.right <= collision_obj.rect.left + 3:
                    if self.player.direction == 'r':
                        Moveable.speed = 0
                    else:
                        Moveable.speed = 5

                elif collision_obj.rect.right >= self.player.rect.left >= collision_obj.rect.right - 3:
                    if self.player.direction == 'l':
                        Moveable.speed = 0
                    else:
                        Moveable.speed = 5

                elif self.player.jumping:
                    self.player.jumping = False
                    Barrier.standing = True

        else:
            Moveable.speed = 5
            Barrier.standing = False
            self.player.jumping = True
