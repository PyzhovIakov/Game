import sys
import pygame
from ship import Ship
from settings import Settings
"""Класс для управления ресурсами и поведением игры."""


class AlienInvasion:
    """Инициализирует игру и создает игровые ресурсы."""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    """Запуск основного цикла игры."""

    def run_game(self):
        while True:
            # Отслеживание событий клавиатуры и мыши.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # При каждом проходе цикла перерисовывается экран.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            # Отображение последнего прорисованного экрана.
            pygame.display.flip()


# Создание экземпляра и запуск игры.
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
