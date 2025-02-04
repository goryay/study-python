import pygame
import sys


class KeysPress:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Keys')

    def run_window(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print(f'Key pressed {pygame.key.name(event.key).title()}, its ASCII cod {event.key}')

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    kp = KeysPress()
    kp.run_window()
