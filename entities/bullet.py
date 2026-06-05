"""
Модуль пули
Содержит класс Bullet для управления снарядами
"""

import pygame
from pygame.math import Vector2
from utils.colors import Colors


class Bullet:
    """Класс пули"""

    def __init__(self, x, y):
        """Инициализация пули

        Args:
            x (float): Позиция по оси X
            y (float): Позиция по оси Y
            direction (Vector2): Направление движения
        """
        self.position = Vector2(x, y)
        self.color = Colors.GOLD.value
        self.speed = 1
        self.radius = 5
        self.attack = 20

    def draw(self, screen):
        """Отрисовка пули на экране

        Args:
            screen: Поверхность Pygame для отрисовки
        """
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)