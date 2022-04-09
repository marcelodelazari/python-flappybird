import random

class Controller(object):

    def __init__(self, screen, bird):
        self.screen = screen
        self.bird = bird
        self.pipe_size = 80
        self.pipe_gap = 170
        self.pipes = []
        self.create_pipes()
        self.current_pipe = False
        self.score = 0

    def update(self):
        self.bird.move()
        self.move_pipes()
        self.check_collision()

        if self.check_death():
            self.restart()


    def check_fall(self):
        if self.bird.get_pos()[1] >= 600:
          return True

        return False

    def check_death(self):
        return self.check_fall() or self.check_collision()


    def restart(self):
        self.bird.pos = [200, 320]
        self.pipes.clear()
        self.create_pipes()
        self.current_pipe = False
        self.score = 0

    def create_pipes(self):
        for i in range(4):
            y = random.randrange(140, 460)
            self.pipes.append([600+i*280, y])

    def create_pipe(self):
        y = random.randrange(140, 460)
        x = self.pipes[-1][0] + 280
        self.pipes.append([x, y])

    def move_pipes(self):
        for pipe in self.pipes:
            pipe[0] -= 3

        if self.pipes[0][0] <= -self.pipe_size:
            self.pipes.pop(0)
            self.create_pipe()


    def check_collision(self):
        bird_x, bird_y = self.bird.get_pos()
        bird_size = self.bird.size

        old_pipe = self.current_pipe
        if self.pipes[0][0] + self.pipe_size >= bird_x:
            self.current_pipe = self.pipes[0]
        else:
            self.current_pipe = self.pipes[1]

        if old_pipe and old_pipe != self.current_pipe:
            self.score += 1

        pipe = self.current_pipe
        pipe_x = pipe[0]
        pipe_y = pipe[1]

        if bird_x + bird_size >= pipe_x:
            if bird_y - bird_size <= pipe_y - self.pipe_gap / 2 or bird_y + bird_size >= pipe_y + self.pipe_gap / 2:
                return True

        return False







