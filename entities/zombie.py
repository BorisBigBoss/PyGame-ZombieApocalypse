"""
Модуль зомби
Содержит класс Zombie для управления врагами
"""


class Zombie:
    """Класс зомби (заготовка)"""
    
    def __init__(self, x, y):
        """Инициализация зомби
        
        Args:
            x (float): Начальная позиция по оси X
            y (float): Начальная позиция по оси Y
        """
        self.x = x
        self.y = y
    
    def draw(self, screen):
        """Отрисовка зомби на экране
        
        Args:
            screen: Поверхность Pygame для отрисовки
        """
        pass