from classes.entity import Entity
import pygame


class Barrier():
    def __init__(self, player, barrier):
        self.player = player
        self.barrier = barrier

    def check_collisions(self):
        collisions = pygame.sprite.spritecollide(
            self.player, self.barrier, False)

        if collisions:
            collision_obj = collisions[0]

            if collision_obj.rect.bottom >= self.player.rect.bottom and self.player.jumping and self.player.gravity > 0:
                self.player.jumping = False
                self.player.gravity = 0
            elif collision_obj.rect.left <= self.player.rect.right <= collision_obj.rect.left + 3:
                if self.player.direction == 'l':
                    collision_obj.speed = 0
                else:
                    self.player.speed = 0
            elif collision_obj.rect.right >= self.player.rect.left >= collision_obj.rect.right - 3:
                if self.player.direction == 'r':
                    collision_obj.speed = 0
                else:
                    self.player.speed = 0
        else:
            self.player.speed = 5
            self.player.jumping = True
