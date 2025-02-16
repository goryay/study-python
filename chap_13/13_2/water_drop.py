import sys
import pygame
from drop import Drop
from settings import Settings


class WaterDrop:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Water Drop")

        self.drops = pygame.sprite.Group()
        self._create_drops()

    def run_game(self):
        while True:
            self._event_check()
            self._update_drops()
            self._check_water_drop_bottom()
            self._update_screen()
            self.clock.tick(60)

    def _event_check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_drops(self):
        drop = Drop(self)
        drop_width, drop_height = drop.rect.size

        current_x, current_y = drop_width, drop_height
        while current_y < (self.settings.screen_height - 3 * drop_height):
            while current_x < (self.settings.screen_width - 2 * drop_width):
                new_drop = Drop(self)
                new_drop.x = current_x
                new_drop.rect.x = current_x
                new_drop.rect.y = current_y
                self.drops.add(new_drop)
                current_x += 2 * drop_width

            current_x = drop_width
            current_y += 2 * drop_height

    def _update_drops(self):
        self.drops.update()

    def _check_water_drop_bottom(self):
        for drop in self.drops.copy():
            if drop.rect.bottom >= self.settings.screen_height:
                drop.kill()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.drops.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    wd = WaterDrop()
    wd.run_game()
