import pygame
from entities.player import Player
from utils.colors import Colors

pygame.init()

WIDTH = 800
HEIGHT = 800
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Зомби апокалипсис")

clock = pygame.time.Clock()
running = True

player = Player(WIDTH / 2, HEIGHT / 2)

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(Colors.BLACK.value)
    player.draw(screen)

    pygame.display.flip()

pygame.quit()