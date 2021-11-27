class GameStats():
    """Отслеживание статистики для игры Al_Inv"""

    def __init__(self, ai_settings):
        """Инициализирует статистику"""
        self.ai_strings = ai_settings
        self.reset_stats()
        # Игра запускается в активном состоянии
        self.game_active = True

    def reset_stats(self):
        """Инициализирует статистику"""
        self.ships_left = self.ai_strings.ship_limit