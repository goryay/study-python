import pygame


class Rocket:
    def __init__(self, bs_window):
        self.screen = bs_window.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('images/rocket.png')
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)
