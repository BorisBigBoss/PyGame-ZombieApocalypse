"""
Модуль пули
Содержит класс Bullet для управления снарядами
"""


class Bullet:
    """Класс пули (заготовка)"""
    
    def __init__(self, x, y):
        """Инициализация пули
        
        Args:
            x (float): Начальная позиция по оси X
            y (float): Начальная позиция по оси Y
        """
        self.x = x
        self.y = y
    
    def draw(self, screen):
        """Отрисовка пули на экране
        
        Args:
            screen: Поверхность Pygame для отрисовки
        """
        pass