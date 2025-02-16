import pygame
from pygame.sprite  import Sprite

class Drop(Sprite):
    def __init__(self, wd):
        super().__init__()
        self.screen = wd.screen

        self.image = pygame.image.load('images/drop.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def update(self):
        self.y += 1
        self.rect.y = self.y