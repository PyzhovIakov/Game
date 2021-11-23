import sys
import pygame

"""Класс для управления ресурсами и поведением игры."""


class AlienInvasion:
    """Инициализирует игру и создает игровые ресурсы."""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    """Запуск основного цикла игры."""

    def run_game(self):
        while True:
            # Отслеживание событий клавиатуры и мыши.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Отображение последнего прорисованного экрана.
            pygame.display.flip()


# Создание экземпляра и запуск игры.
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
