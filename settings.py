class Settings():
    """Класс для хранения всех настроек игры Alien Invasion"""

    def __init__(self):
        """Инициализируем настройки игры"""
        # Параметры экрана
        self.screen_width = 800
        self.screen_height = 400
        self.bg_color = (200, 200, 200)

        # Настройки корабля
        self.ship_speed_factor = 2
