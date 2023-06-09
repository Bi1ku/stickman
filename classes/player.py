import pygame
from utils import load_asset
from classes.entity import Entity
from classes.lazer import Lazer

graphics_base_path = "assets/player/"


class Player(Entity):
    def __init__(self):
        self.run_animation = [load_asset(
            f"{graphics_base_path}run/run_{i}.png") for i in range(1, 6)]
        self.jump_frame = load_asset(
            f"{graphics_base_path}jump/jump_1.png")
        self.idle_animation = [load_asset(
            f"{graphics_base_path}idle/idle_{i}.png") for i in range(1, 3)]
        self.dash_frame = load_asset(
            f"{graphics_base_path}dash/dash_1.png")

        super().__init__(self.idle_animation[0], (0, 0))
        self.dashing = 0
        self.last_dash = 0
        self.lazers = pygame.sprite.Group()
        self.last_shot = 0

    def run(self):
        self.frame += 0.2
        if self.frame >= len(self.run_animation):
            self.frame = 0
        if self.direction == "r":
            self.image = self.run_animation[int(self.frame)]
            self.rect.x += 5
        else:
            self.image = pygame.transform.flip(
                self.run_animation[int(self.frame)], True, False)
            self.rect.x -= 5

    def jump(self):
        self.image = self.jump_frame if self.direction == "r" else pygame.transform.flip(
            self.jump_frame, True, False)

    def idle(self):
        self.frame = 0 if self.frame >= len(
            self.idle_animation) - 1 else self.frame + 0.04
        self.image = self.idle_animation[int(self.frame)]

    def dash(self):
        if self.direction == "r":
            self.image = self.dash_frame
            self.rect.x += 20
        else:
            self.image = pygame.transform.flip(
                self.dash_frame, True, False)
            self.rect.x -= 20

    def inputs(self):
        keys = pygame.key.get_pressed()
        left = keys[pygame.K_a] or keys[pygame.K_LEFT]
        right = keys[pygame.K_d] or keys[pygame.K_RIGHT]
        up = keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE]
        dash = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]
        shoot = keys[pygame.K_e]

        time = pygame.time.get_ticks()
        dash_cooldown = time - self.last_dash >= 5000

        if not int(self.dashing):
            if (left and right) or (not left and not right):
                self.idle()
            elif right:
                self.direction = "r"
                self.run()
                if dash and dash_cooldown:
                    self.last_dash = time
                    self.dashing = 5
            else:
                self.direction = "l"
                self.run()
                if dash and dash_cooldown:
                    self.last_dash = time
                    self.dashing = 7

            if up and self.rect.bottom >= 600:
                self.gravity = -15
            if self.rect.bottom < 600:
                self.jump()

            if shoot and time - self.last_shot >= 250:
                self.lazers.add(
                    Lazer((self.rect.topright[0], self.rect.topright[1] + 25), self.direction))
                self.last_shot = time
        else:
            if dash:
                self.dashing = 0 if (not left and not right) or (
                    left and right) else self.dashing - 0.2
                self.dash()
            else:
                self.dashing = 0

    def apply_gravity(self):
        if not int(self.dashing):
            super().apply_gravity()
        else:
            self.gravity = 0

    def update(self):
        self.lazers.draw(pygame.display.get_surface())
        self.lazers.update()
        self.inputs()
        self.apply_gravity()
