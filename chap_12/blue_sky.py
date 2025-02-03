import sys
import pygame
from settings import Settings
from rocket import Rocket


class BlueSky:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("BLUE SKY")
        # self.bg_color = (0, 0, 255)
        self.rocket = Rocket(self)

    def window_start(self):
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()

            pygame.display.flip()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.rocket.moving_right = True
                elif event.key == pygame.K_a:
                    self.rocket.moving_left = True
                elif event.key == pygame.K_w:
                    self.rocket.moving_up = True
                elif event.key == pygame.K_s:
                    self.rocket.moving_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.rocket.moving_right = False
                elif event.key == pygame.K_a:
                    self.rocket.moving_left = False
                elif event.key == pygame.K_w:
                    self.rocket.moving_up = False
                elif event.key == pygame.K_s:
                    self.rocket.moving_down = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()


if __name__ == '__main__':
    bs = BlueSky()
    bs.window_start()
