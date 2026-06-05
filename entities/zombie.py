import pygame
from pygame.math import Vector2
from utils.colors import Colors


sheet = pygame.image.load(r"C:\Users\Пользователь\PycharmProjects\PyGame-ZombieApocalypse\pictures\ZombieToast.png")

FRAME_WIDTH = 64
FRAME_HEIGHT = 64

frames = []

frames_dic = {
    'idle': [],
    'run': []

}

for i in range(0, 1600, FRAME_WIDTH):
    frame = sheet.subsurface((i, 0, FRAME_WIDTH, FRAME_HEIGHT))
    frames.append(frame)



class Zombie:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (0, 220, 80)
        self.hp = 10
        self.velocity = Vector2(0, 0)
        self.speed=1
        self.attack=1
        self.radius = 10
        self.frames = frames

    def draw(self, pygame, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)