"""
Основной модуль игры "Зомби апокалипсис"
Инициализация Pygame, создание игрового окна и главный цикл
"""

import pygame
import random
from entities.player import Player
from entities.zombie import Zombie
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
zombie = Zombie(random.randint(0, 789), random.randint(0, 789))

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
    
    # Отрисовка сущностей
    player.draw(screen)
    zombie.draw(screen)

    # Обновление экрана
    pygame.display.flip()

# Завершение работы
pygame.quit()