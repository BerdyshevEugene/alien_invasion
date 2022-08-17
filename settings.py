import pygame

class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1400
        self.screen_height = 700
        self.bg_color = (7, 11, 39)  # фон нерабочий
        bg = pygame.image.load('images/space.bmp')
        self.bg = pygame.transform.scale(bg, (1400, 700))
        self.ship_speed_factor = 5
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 2
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1
        # Параметры пули
        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 96, 174, 200
        self.bullets_allowed = 3
