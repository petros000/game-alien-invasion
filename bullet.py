import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Класс для управления пулями, выпущенными кораблем"""

    def __init__(self, ai_settings, screen, ship):
        """Создает объект пули в текущей позиции"""
        super(Bullet, self).__init__()
        self.screen = screen

        # Загрузка изображения пули и получение прямоугольника
        self.image = pygame.image.load("image/bullet.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # назначение правильной позиции
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Позиция пули хранится в вещественном формате
        self.y = float(self.rect.y)

        #self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Перемещает пуля вверх по экрану"""

        # Обновление позиции пули в вещественном формате
        self.y -= self.speed_factor
        # Обновление позиции прямоугольгика
        self.rect.y = self.y

    def draw_bullet(self):
        """Вывод пули на экран"""
        self.screen.blit(self.image, self.rect)