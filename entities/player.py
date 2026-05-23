"""
Модуль игрока
Содержит класс Player для управления персонажем игрока
"""

import pygame
from pygame.math import Vector2
from utils.colors import Colors


class Player:
    """Класс игрока"""
    
    def __init__(self, x, y):
        """Инициализация игрока
        
        Args:
            x (float): Начальная позиция по оси X
            y (float): Начальная позиция по оси Y
        """
        self.x = x
        self.y = y
        self.color = Colors.BLUE
        self.hp = 100
        self.velocity = Vector2(0, 0)
        self.radius = 10
    
    def draw(self, screen):
        """Отрисовка игрока на экране
        
        Args:
            screen: Поверхность Pygame для отрисовки
        """
        pygame.draw.circle(screen, self.color.value, (int(self.x), int(self.y)), self.radius)