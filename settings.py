"""Класс для хранения всех настроек игры Alien Invasion."""


class Settings():
    def __init__(self):
        self.screen_width = 750
        self.screen_height = 655
        self.bg_color = (230, 230, 230)

        # Настройки корабля
        self.ship_speed = 1.5
        self.ship_limit = 2

        # Параметры снаряда
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 4

        # Настройки пришельцев
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1

        # Подсчет очков
        self.alien_points = 5


