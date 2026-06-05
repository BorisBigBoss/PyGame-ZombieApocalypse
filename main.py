"""
Основной модуль игры "Зомби апокалипсис"
Инициализация Pygame, создание игрового окна и главный цикл
"""

import pygame
import random

from pygame.math import Vector2

from entities.player import Player
from entities.zombie import Zombie
from entities.bullet import Bullet
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
player = Player(WIDTH // 2, HEIGHT // 2)
zombie = Zombie(random.randint(0, 789), random.randint(0, 789))

R = 11
bullets = []

# Главный игровой цикл
while running:
    # Контроль частоты кадров
    clock.tick(FPS)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = Vector2(pygame.mouse.get_pos())
            direction = (mouse_pos - Vector2(player.x, player.y)).normalize()
            bullets.append(Bullet(player.x, player.y, direction))

    # bullet.move()
    for bullet in bullets:
        bullet.move()

    # player.move()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0 + player.radius + 1:
        player.x -= player.speed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and player.x < WIDTH - player.radius - 1:
        player.x += player.speed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and player.y < HEIGHT - player.radius - 1:
        player.y += player.speed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player.y > 0 + player.radius + 1:
        player.y -= player.speed

    # zombie.move()

    # Очистка экрана
    screen.fill(Colors.BLACK.value)

    # Отрисовка сущностей
    player.draw(pygame, screen)
    zombie.draw(pygame, screen)
    for bullet in bullets:
        bullet.draw(pygame, screen)

    for frame in zombie.frames:
        screen.blit(frame, (zombie.x, zombie.y))
    # Обновление экрана
    pygame.display.flip()


# Завершение работы
pygame.quit()