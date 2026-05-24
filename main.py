"""
Основной модуль игры "Зомби апокалипсис"
Инициализация Pygame, создание игрового окна и главный цикл
"""

import pygame
import random
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
player = Player(WIDTH / 2, HEIGHT / 2)
zombie = Zombie(random.randint(0, 789), random.randint(0, 789))
bullet = Bullet(WIDTH / 2, HEIGHT / 2)

# Главный игровой цикл
while running:
    # Контроль частоты кадров
    clock.tick(FPS)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получение урона и конец игры
    distance = ((player.x - zombie.x) ** 2 + (player.y - zombie.y) ** 2) ** 0.5
    if distance <= player.radius + zombie.radius:
        player.hp -= zombie.attack
    if player.hp <= 0:
        running = False

    # Движение игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 11:
        player.x -= player.speed
    if keys[pygame.K_RIGHT] and player.x < WIDTH - 11:
        player.x += player.speed
    if keys[pygame.K_DOWN] and player.y < HEIGHT - 11:
        player.y += player.speed
    if keys[pygame.K_UP] and player.y > 11:
        player.y -= player.speed

    # Движение зомби
    if player.x < zombie.x and distance >= player.radius + zombie.radius:
        zombie.x -= zombie.speed
    if player.y < zombie.y and distance >= player.radius + zombie.radius:
        zombie.y -= zombie.speed
    if player.x > zombie.x and distance >= player.radius + zombie.radius:
        zombie.x += zombie.speed
    if player.y > zombie.y and distance >= player.radius + zombie.radius:
        zombie.y += zombie.speed

        # Движение пули
        if zombie.x < bullet.x and distance >= bullet.radius + zombie.radius:
            bullet.x -= bullet.speed
        if zombie.y < bullet.y and distance >= bullet.radius + zombie.radius:
            bullet.y -= bullet.speed
        if zombie.x > bullet.x and distance >= bullet.radius + zombie.radius:
            bullet.x += bullet.speed
        if zombie.y < bullet.y and distance >= bullet.radius + zombie.radius:
            bullet.y += bullet.speed


    # Очистка экрана
    screen.fill(Colors.BLACK.value)
    
    # Отрисовка сущностей
    player.draw(screen)
    zombie.draw(screen)
    bullet.draw(screen)

    # Обновление экрана
    pygame.display.flip()

# Завершение работы
pygame.quit()