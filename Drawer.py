import pygame
import time

class Drawer(object):

    def __init__(self, screen, width, height, bird, controller):
        self.screen = screen
        self.width = width
        self.height = height
        self.bird = bird
        self.controller = controller

        self.bg = pygame.image.load("sprites/bg.png")
        self.midflap = pygame.image.load("sprites/midflap.png")
        self.bird_image = self.midflap
        self.upflap = pygame.image.load("sprites/upflap.png")
        self.downflap = pygame.image.load("sprites/downflap.png")

        self.base = pygame.image.load("sprites/base.png")
        self.last_time = time.time()

        self.zero = pygame.image.load("sprites/0.png")
        self.one = pygame.image.load("sprites/1.png")
        self.two = pygame.image.load("sprites/2.png")
        self.three = pygame.image.load("sprites/3.png")
        self.four = pygame.image.load("sprites/4.png")
        self.five = pygame.image.load("sprites/5.png")
        self.six = pygame.image.load("sprites/6.png")
        self.seven = pygame.image.load("sprites/7.png")
        self.eight = pygame.image.load("sprites/8.png")
        self.nine = pygame.image.load("sprites/9.png")
        self.numbers = [self.zero, self.one, self.two, self.three, self.four, self.five, self.six, self.seven,
                        self.eight, self.nine]

    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.base, (0, 550))
        self.draw_bird()
        self.draw_pipes()
        self.draw_score()


    def draw_bird(self):
        if time.time() - self.last_time > 0.08:
            self.last_time = time.time()

            if self.bird_image == self.midflap:
                self.bird_image = self.upflap
            elif self.bird_image == self.upflap:
                self.bird_image = self.downflap
            else:
                self.bird_image = self.midflap

        x, y = self.bird.get_pos()
        new_x, new_y = x - self.bird.size, y - self.bird.size
        self.screen.blit(self.bird_image, (new_x, new_y))

    def draw_pipes(self):
        gap_size = self.controller.pipe_gap
        pipe_size = self.controller.pipe_size

        for pipe in self.controller.pipes:
            green = (10, 200, 10)

            pygame.draw.rect(self.screen, (0, 0, 0),
                             (int(pipe[0]) - 3, 0, pipe_size + 6,
                              int(pipe[1] - gap_size / 2) + 3))

            pygame.draw.rect(self.screen, green,
                             (int(pipe[0]), 0, pipe_size,
                              int(pipe[1] - gap_size / 2)))

            pygame.draw.rect(self.screen, (0, 0, 0),
                             (pipe[0] - 3, int(pipe[1] + gap_size / 2) - 3, pipe_size + 6,
                              600))

            pygame.draw.rect(self.screen, green,
                             (pipe[0], int(pipe[1] + gap_size / 2), pipe_size,
                              600))


    def draw_score(self):
        drawing = []
        xs = [220,240,261]
        score = self.controller.score
        y = 120

        for e in str(score):
            drawing.append(int(e))

        for i in range(len(drawing)):
            e = drawing[i]
            x = xs[i]
            if i == 0 and e == 1:
                x += 7
            self.screen.blit(self.numbers[e], (x, y))