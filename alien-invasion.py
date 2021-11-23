import sys
import pygame

def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Alien Invasion")
    # Назначение цвета фона
    bg_color = (230, 230, 230)

    # Запуск основного цикла
    while True:
        # При каждом проходе цикла перерисовывается экран
        screen.fill(bg_color)

        # Отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Отображение последнего прорисованного экрана
        pygame.display.flip()


run_game()