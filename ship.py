import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Инициализирует корабль и задает его начальную позицию"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузка изображения корбля и получение прямоугольника
        self.image = pygame.image.load("image/ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Сохранение вещественной координаты корабля
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)
        # Флаги пермещения
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bot = False

    def update(self):
        """Обновляет позицию корабля с учетом флага"""
        # Обновляет атрибут center, не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center_x -= self.ai_settings.ship_speed_factor
        if self.moving_top and self.rect.top > 0:
            self.center_y -= self.ai_settings.ship_speed_factor
        if self.moving_bot and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.ai_settings.ship_speed_factor

        # Обновление атрибута rect на основании self.center
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
