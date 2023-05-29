import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.run_animation = [pygame.transform.rotozoom(pygame.image.load("graphics/player/run/run_1.png").convert_alpha(), 0, 0.25), pygame.transform.rotozoom(pygame.image.load("graphics/player/run/run_2.png").convert_alpha(), 0, 0.25), pygame.transform.rotozoom(pygame.image.load(
            "graphics/player/run/run_3.png").convert_alpha(), 0, 0.25), pygame.transform.rotozoom(pygame.image.load("graphics/player/run/run_4.png").convert_alpha(), 0, 0.25), pygame.transform.rotozoom(pygame.image.load("graphics/player/run/run_5.png").convert_alpha(), 0, 0.25)]
        self.jump_animation = pygame.transform.rotozoom(pygame.image.load("graphics/player/jump/jump_1.png").convert_alpha(
        ), 0, 0.25)
        self.idle_animation = [pygame.transform.rotozoom(pygame.image.load("graphics/player/idle/idle_1.png").convert_alpha(), 0, 0.25), pygame.transform.rotozoom(
            pygame.image.load("graphics/player/idle/idle_2.png").convert_alpha(), 0, 0.25)]
        self.image = self.run_animation[0]
        self.rect = self.image.get_rect()
        self.run_frame = 0
        self.idle_frame = 0
        self.gravity = 0

    def movement(self):
        def animate_run(direction):
            self.run_frame += 0.2
            if self.run_frame >= len(self.run_animation):
                self.run_frame = 0
            if direction == "RIGHT":
                self.image = self.run_animation[int(self.run_frame)]
            elif direction == "LEFT":
                self.image = pygame.transform.flip(
                    self.run_animation[int(self.run_frame)], True, False)

        def animate_jump(direction):
            if direction == "RIGHT":
                self.image = self.jump_animation
            elif direction == "LEFT":
                self.image = pygame.transform.flip(
                    self.jump_animation, True, False)

        def animate_idle():
            self.idle_frame += 0.04
            if self.idle_frame >= len(self.idle_animation):
                self.idle_frame = 0
            self.image = self.idle_animation[int(self.idle_frame)]

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            animate_run("LEFT")
            self.rect.x -= 5
        elif keys[pygame.K_d]:
            animate_run("RIGHT")
            self.rect.x += 5

        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -15

        if self.rect.bottom < 300:
            if keys[pygame.K_a]:
                animate_jump("LEFT")
            else:
                animate_jump("RIGHT")
        elif not keys[pygame.K_a] and not keys[pygame.K_d]:
            animate_idle()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def update(self):
        self.movement()
        self.apply_gravity()
