import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.settings.screen_width - self.rect.width
        self.rect.y = self.rect.height
        # self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.rect.x -= self.settings.alien_speed