"""Класс для хранения всех настроек игры Alien Invasion."""


class Settings():
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 500
        self.bg_color = (230, 230, 230)

        # Настройки корабля
        self.ship_speed = 1.5
