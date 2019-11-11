from pico2d import *


class Brick:
    def __init__(self):
        self.image = load_image('brick180x40.png')
        self.x, self.y = 0, 300

    def update(self):
        self.x += 1

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20
