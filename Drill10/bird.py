import game_framework
from pico2d import *
import time


class Bird:

    def __init__(self):
        self.x, self.y = 1600 // 2, 300
        self.image_go_right = load_image('bird_animation.png')
        self.image_go_left = load_image('bird_animation2.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        # velocity = 5km/h
        self.velocity = 5
        self.frameX = 0
        self.frameY = 0
        self.frameTime = 0
        self.current_time = time.time()

    def update(self):
        if self.dir == 1:
            self.x += game_framework.frame_time * 300;
            if self.x > 1500:
                self.dir = -1
        elif self.dir == -1:
            self.x -= game_framework.frame_time * 300;
            if self.x < 100:
                self.dir = 1

        self.frameTime += game_framework.frame_time
        if self.frameTime > 0.1:
            self.frameTime = 0
            self.frameX += 1;

        if self.frameX == 5:
            self.frameX = 0
            self.frameY += 1
        if self.frameY == 2:
            self.frameY = 0

        pass

    def draw(self):
        if self.dir == 1:
            self.image_go_right.clip_draw(self.frameX * 183, self.frameY * 160, 180, 168, self.x, self.y, 100, 100)
        if self.dir == -1:
            self.image_go_left.clip_draw(self.frameX * 183, self.frameY * 160, 180, 168, self.x, self.y, 100, 100)
        pass
