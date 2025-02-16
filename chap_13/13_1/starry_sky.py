import pygame
import sys
from settings import Settings
from stars import Star


class StarrySky:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Starry Sky")

        self.stars = pygame.sprite.Group()

        self.game_active = True

        self._create_stars_sky()

    def window_start(self):
        while True:
            self._check_events()  # Обработка событий

            self._update_screen()
            self.clock.tick(60)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def _create_stars_sky(self):
        star = Star(self)
        star_width, star_height = star.rect.size

        current_x, current_y = star_width, star_height
        while current_y < (self.settings.screen_height - 3 * star_height):
            while current_x < (self.settings.screen_width - 2 * star_width):
                self._create_stars(current_x, current_y)
                current_x += 2 * star_width

            current_x = star_width
            current_y += 2 * star_height

    def _create_stars(self, x_pos, y_pos):
        new_star = Star(self)
        new_star.x = x_pos
        new_star.rect.x = x_pos
        new_star.rect.y = y_pos
        self.stars.add(new_star)


if __name__ == '__main__':
    starry = StarrySky()
    starry.window_start()
