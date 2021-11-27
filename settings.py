class Settings():
    """Класс для хранения всех настроек игры Alien Invasion"""

    def __init__(self):
        """Инициализируем настройки игры"""
        # Параметры экрана
        self.screen_width = 900
        self.screen_height = 800
        self.bg_color = (200, 200, 200)

        # Настройки корабля
        self.ship_speed_factor = 1
        self.ship_limit = 3

        # Парметры пули
        self.bullet_speed_factor = 3
        self.bullets_allowed = 5

        # Настройки пришельцев
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо, а -1 влево
        self.fleet_direction = 1
