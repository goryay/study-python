import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ss_window):
        super().__init__()
        self.screen = ss_window.screen
        self.settings = ss_window.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midleft = ss_window.rocket.rect.midleft

        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
