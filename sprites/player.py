import pygame
from utils.graphics import load_graphic

graphics_base_path = "graphics/player/"


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.run_animation = [load_graphic(
            f"{graphics_base_path}run/run_{i}.png") for i in range(1, 6)]
        self.jump_frame = load_graphic(
            f"{graphics_base_path}jump/jump_1.png")
        self.idle_animation = [load_graphic(
            f"{graphics_base_path}idle/idle_{i}.png") for i in range(1, 3)]
        self.dash_frame = load_graphic(
            f"{graphics_base_path}dash/dash_1.png")
        self.image = self.idle_animation[0]
        self.rect = self.image.get_rect()
        self.frame = 0
        self.gravity = 0
        self.dashing = 0
        self.last_dash = 0

    def movement(self):
        def animate_run(direction):
            print(self.frame)
            self.frame += 0.2
            if self.frame >= len(self.run_animation):
                self.frame = 0
            if direction == "RIGHT":
                self.image = self.run_animation[int(self.frame)]
            elif direction == "LEFT":
                self.image = pygame.transform.flip(
                    self.run_animation[int(self.frame)], True, False)

        def animate_jump(direction):
            if direction == "RIGHT":
                self.image = self.jump_frame
            elif direction == "LEFT":
                self.image = pygame.transform.flip(
                    self.jump_frame, True, False)

        def animate_idle():
            self.frame += 0.04
            if self.frame >= len(self.idle_animation):
                self.frame = 0
            self.image = self.idle_animation[int(self.frame)]

        def animate_dash(direction):
            if direction == "RIGHT":
                self.image = self.dash_frame
            elif direction == "LEFT":
                self.image = pygame.transform.flip(
                    self.dash_frame, True, False)

        keys = pygame.key.get_pressed()
        if not int(self.dashing):
            if keys[pygame.K_a]:
                if keys[pygame.K_RIGHTBRACKET] and pygame.time.get_ticks() - self.last_dash >= 1000:
                    self.last_dash = pygame.time.get_ticks()
                    self.dashing = 5
                animate_run("LEFT")
                self.rect.x -= 5
            elif keys[pygame.K_d]:
                if keys[pygame.K_RIGHTBRACKET] and pygame.time.get_ticks() - self.last_dash >= 1000:
                    self.last_dash = pygame.time.get_ticks()
                    self.dashing = 5
                animate_run("RIGHT")
                self.rect.x += 5
            else:
                animate_idle()

            if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
                self.gravity = -15

            if self.rect.bottom < 300:
                if keys[pygame.K_a]:
                    animate_jump("LEFT")
                else:
                    animate_jump("RIGHT")
        else:
            if keys[pygame.K_a] and keys[pygame.K_RIGHTBRACKET]:
                animate_dash("LEFT")
                self.rect.x -= 10
            elif keys[pygame.K_d] and keys[pygame.K_RIGHTBRACKET]:
                animate_dash("RIGHT")
                self.rect.x += 10
            else:
                self.dashing = 0
            self.dashing -= 0.2

    def apply_gravity(self):
        if not int(self.dashing):
            self.gravity += 1
            self.rect.y += self.gravity
            if self.rect.bottom >= 300:
                self.rect.bottom = 300
        else:
            self.gravity = 0

    def update(self):
        self.movement()
        self.apply_gravity()
