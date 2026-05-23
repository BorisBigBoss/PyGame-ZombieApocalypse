"""
Основной модуль игры "Зомби апокалипсис"
Инициализация Pygame, создание игрового окна и главный цикл
"""

import pygame
from entities.player import Player
from utils.colors import Colors

# Инициализация Pygame
pygame.init()

# Константы экрана
WIDTH = 800
HEIGHT = 800
FPS = 60

# Создание игрового окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Зомби апокалипсис")

# Игровые объекты
clock = pygame.time.Clock()
running = True
player = Player(WIDTH / 2, HEIGHT / 2)

# Главный игровой цикл
while running:
    # Контроль частоты кадров
    clock.tick(FPS)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очистка экрана
    screen.fill(Colors.BLACK.value)
    
    # Отрисовка игрока
    player.draw(screen)

    # Обновление экрана
    pygame.display.flip()

# Завершение работы
pygame.quit()