import sys
import time
import pygame
from settings import Settings
from rocket import Rocket
from bullet import Bullet
from alien import Alien


class SideShooting:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Sideways shooting")
        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.aliens_destroyed = 0
        self.collisions_with_ship = 0
        self.last_collision_time = 0

    def window_start(self):
        while True:
            self._check_events()
            self.rocket.update()
            self.bullets.update()
            self._update_bullets()
            self._update_aliens()
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

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.width, alien.rect.height

        number_aliens_x = 5
        start_x = self.settings.screen_width - (number_aliens_x * alien_width * 2)

        available_y_space = self.settings.screen_height - (2 * alien_height)
        number_rows = available_y_space // (alien_height * 2)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                new_alien = Alien(self)
                new_alien.x = start_x + 2 * alien_width * alien_number
                new_alien.rect.x = new_alien.x
                new_alien.y = alien_height + 2 * alien_height * row_number
                new_alien.rect.y = new_alien.y
                self.aliens.add(new_alien)

    def _update_aliens(self):
        for alien in self.aliens.sprites():
            # Если хотя бы один пришелец дошел до левого края – пауза 5 сек и перезапуск флота
            if alien.rect.left <= 0:
                print("Пришельцы достигли левого края! Пауза 5 сек...")
                pygame.time.delay(5000)  # Пауза на 5 секунд
                self._reset_fleet()
                return

            # Проверяем столкновение с кораблём
            if pygame.sprite.spritecollideany(self.rocket, self.aliens):
                current_time = time.time()
                if current_time - self.last_collision_time > 1:  # Разрешаем считать столкновение раз в 1 секунду
                    print("🚨 Столкновение с кораблём!")
                    self.collisions_with_ship += 1
                    self.last_collision_time = current_time  # Обновляем время столкновения
                    self._reset_fleet()
                    return

        self.aliens.update()

    def _reset_fleet(self):
        self.aliens.empty()  # Удаляем всех пришельцев
        self._create_fleet()  # Создаём новый флот
        self.settings.alien_speed = 1  # Сбрасываем скорость

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.left > self.settings.screen_width:
                self.bullets.remove(bullet)

        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            self.aliens_destroyed += sum(len(v) for v in collisions.values())

        if not self.aliens:
            self._create_fleet()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.rocket.blitme()
        self.aliens.draw(self.screen)

        print(
            f"👾 Уничтожено пришельцев: {self.aliens_destroyed} | 🚀 Столкновений с кораблём: {self.collisions_with_ship}")

        pygame.display.flip()


if __name__ == '__main__':
    ss = SideShooting()
    ss.window_start()
