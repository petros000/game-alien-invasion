class Settings():
    """Класс для хранения всех настроек игры Alien Invasion"""

    def __init__(self):
        """Инициализируем настройки игры"""
        # Параметры экрана
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (200, 200, 200)

        # Настройки корабля
        self.ship_speed_factor = 0.5

        # Парметры пули
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (200, 60, 60)
        self.bullets_allowed = 3
