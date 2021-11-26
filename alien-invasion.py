import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_function as gf
from pygame.sprite import Group

def run_game():
    # Инициализирует pygame, settings и объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Создание корабля
    ship = Ship(ai_settings, screen)
    # Создание пришельца
    alien = Alien(ai_settings, screen)
    # Создание группы для хранения пуль
    bullets = Group()

    # Запуск основного цикла
    while True:
        # Отслеживание событий клавиатуры и мыши
        gf.check_events(ai_settings, screen,   ship, bullets)
        # Движение корабля
        ship.update()

        # Обновляет и отображает изображениена экране
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)

        #gf.update_screen(ai_settings, screen, ship, bullets)


run_game()