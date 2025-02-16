import pygame
from random import randint
from pygame.sprite import Sprite


class Star(Sprite):
    def __init__(self, starry):
        super().__init__()
        self.screen = starry.screen
        self.settings = starry.settings

        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.visible = True

        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.right > screen_rect.right) or (self.rect.left <= 0)

    def update_visible(self):
        if randint(-10, 10) == 0:
            self.visible = False