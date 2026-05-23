"""
Модуль зомби
Содержит класс Zombie для управления персонажем зомби
"""

import pygame
from pygame.math import Vector2
from utils.colors import Colors


class Zombie:
    """Класс зомби"""

    def __init__(self, x, y):
        """Инициализация зомби

                Args:
                    x (float): Позиция по оси X
                    y (float): Позиция по оси Y
                """
        self.x = x
        self.y = y
        self.color = Colors.GREEN
        self.hp = 10
        self.velocity = Vector2(0, 0)
        self.speed = 1
        self.attack = 1
        self.radius = 10

    def draw(self, screen):
        """Отрисовка зомби на экране

        Args:
            screen: Поверхность Pygame для отрисовки
        """
        pygame.draw.circle(screen, self.color.value, (int(self.x), int(self.y)), self.radius)