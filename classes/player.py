import pygame
from utils import load_graphic
from classes.entity import Entity

graphics_base_path = "assets/player/"


class Player(Entity):
    def __init__(self):
        self.run_animation = [load_graphic(
            f"{graphics_base_path}run/run_{i}.png") for i in range(1, 6)]
        self.jump_frame = load_graphic(
            f"{graphics_base_path}jump/jump_1.png")
        self.idle_animation = [load_graphic(
            f"{graphics_base_path}idle/idle_{i}.png") for i in range(1, 3)]
        self.dash_frame = load_graphic(
            f"{graphics_base_path}dash/dash_1.png")

        super().__init__(self.idle_animation[0])
        self.image = self.idle_animation[0]
        self.rect = self.image.get_rect()
        self.dashing = 0
        self.last_dash = 0

    def animate_run(self, direction):
        self.frame += 0.2
        if self.frame >= len(self.run_animation):
            self.frame = 0
        if direction == "RIGHT":
            self.image = self.run_animation[int(self.frame)]
        elif direction == "LEFT":
            self.image = pygame.transform.flip(
                self.run_animation[int(self.frame)], True, False)

    def animate_jump(self, direction):
        if direction == "RIGHT":
            self.image = self.jump_frame
        elif direction == "LEFT":
            self.image = pygame.transform.flip(
                self.jump_frame, True, False)

    def animate_idle(self):
        self.frame += 0.04
        if self.frame >= len(self.idle_animation):
            self.frame = 0
        self.image = self.idle_animation[int(self.frame)]

    def animate_dash(self, direction):
        if direction == "RIGHT":
            self.image = self.dash_frame
        elif direction == "LEFT":
            self.image = pygame.transform.flip(
                self.dash_frame, True, False)

    def movement(self):
        keys = pygame.key.get_pressed()
        left = keys[pygame.K_a] or keys[pygame.K_LEFT]
        right = keys[pygame.K_d] or keys[pygame.K_RIGHT]
        up = keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE]
        dash = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]
        dash_cooldown = dash and (
            pygame.time.get_ticks() - self.last_dash) >= 5000

        if not int(self.dashing):
            if (left and right) or (not left and not right):
                self.animate_idle()
            elif left:
                if dash and dash_cooldown:
                    self.last_dash = pygame.time.get_ticks()
                    self.dashing = 7
                self.animate_run("LEFT")
                self.rect.x -= 5
            else:
                if dash and dash_cooldown:
                    self.last_dash = pygame.time.get_ticks()
                    self.dashing = 5
                self.animate_run("RIGHT")
                self.rect.x += 5

            if up and self.rect.bottom >= 300:
                self.gravity = -15

            if self.rect.bottom < 300:
                if left:
                    self.animate_jump("LEFT")
                else:
                    self.animate_jump("RIGHT")
        else:
            if dash:
                if (not left and not right) or (left and right):
                    self.dashing = 0
                elif left:
                    self.animate_dash("LEFT")
                    self.rect.x -= 20
                else:
                    self.animate_dash("RIGHT")
                    self.rect.x += 20
                self.dashing -= 0.2
            else:
                self.dashing = 0

    def apply_gravity(self):
        if not int(self.dashing):
            super().apply_gravity()
        else:
            self.gravity = 0

    def update(self):
        self.movement()
        self.apply_gravity()
