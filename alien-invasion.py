import sys
import pygame
from settings import Settings
from ship import Ship
import game_function as gf

def run_game():
    # Инициализирует pygame, settings и объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Создание корабля
    ship = Ship(ai_settings, screen)

    # Запуск основного цикла
    while True:
        # Отслеживание событий клавиатуры и мыши
        gf.check_events(ship)
        # Движение корабля
        ship.update()
        # Обновляет и отображает изображениена экране
        gf.update_screen(ai_settings, screen, ship)


run_game()