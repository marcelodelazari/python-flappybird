class Bird(object):

    def __init__(self, pos):
        self.size = 20
        self.pos = pos
        self.speed = 0
        self.accel = 0.55
        self.max_speed = 9

    def move(self):
        if self.speed + self.accel <= self.max_speed:
            self.speed += self.accel
        else:
            self.speed = self.max_speed

        self.pos[1] += self.speed

        # bird doesn't fly infinitely
        if self.pos[1] < -100:
            self.pos[1] = -100

    def jump(self):
        self.speed = -10

    def get_pos(self):
        x = self.pos[0]
        y = self.pos[1]
        return [int(x), int(y)]