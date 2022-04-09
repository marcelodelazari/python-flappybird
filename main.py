import pygame

from Bird import Bird
from Drawer import Drawer
from Controller import Controller

pygame.init()

# Screen config
WIDTH = 480
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyBird")

# Classes instances
bird = Bird([200, 320])
controller = Controller(screen, bird)
drawer = Drawer(screen, WIDTH, HEIGHT, bird, controller)

# Game loop
running = True
clock = pygame.time.Clock()
frametime = 60

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()

    controller.update()
    drawer.draw()
    pygame.display.update()

    clock.tick(frametime)