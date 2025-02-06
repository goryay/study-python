import sys
import pygame
from settings import Settings
from rocket import Rocket
from bullet import Bullet


class SideShooting:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Sideways shooting")
        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()

    def window_start(self):
        while True:
            self._check_events()
            self.rocket.update()
            self.bullets.update()
            self._update_bullets()
            self._update_screen()

            pygame.display.flip()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_w:
            self.rocket.moving_up = True
        elif event.key == pygame.K_s:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_w:
            self.rocket.moving_up = False
        elif event.key == pygame.K_s:
            self.rocket.moving_down = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.left > self.settings.screen_width:
                self.bullets.remove(bullet)
        print(len(self.bullets))

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.rocket.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    ss = SideShooting()
    ss.window_start()
