import pygame
from pygame.math import Vector2
from utils.colors import Colors

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = Colors.BLUE
        self.hp = 100
        self.velocity = Vector2(0, 0)
        self.radius = 10

    def draw(self, screen):
        pygame.draw.circle(screen, self.color.value, (int(self.x), int(self.y)), self.radius)