from pico2d import *
import random

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)


class Ball21:
    def __init__(self):
        self.x, self.y = random.randint(1, 799), 599
        self.fy = random.randint(1, 30)
        self.image = load_image('ball21x21.png')
    def update(self):
        if self.y > 50:
            self.y -= self.fy
        else:
            self.y = self.y

    def draw(self):
        self.image.draw(self.x, self.y)


class Ball41:
    def __init__(self):
        self.x, self.y = random.randint(1, 799), 599
        self.fy = y = random.randint(1, 30)
        self.image = load_image('ball41x41.png')
    def update(self):
        if self.y > 50:
            self.y -= self.fy
        else:
            self.y = self.y

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

# ball count max 20
idx21 = random.randint(1, 20)
idx41 = 20 - idx21
running = True

grass = Grass()
team = [Boy() for i in range(11)]
ball21 = [Ball21() for i in range(idx21)]
ball41 = [Ball41() for i in range(idx41)]

while running:
    handle_events()
    for boy in team:
        boy.update()

    for ball in ball21:
        ball.update()
    for ball in ball41:
        ball.update()

    clear_canvas()
    grass.draw()

    for boy in team:
        boy.draw()
    for ball in ball21:
        ball.draw()
    for ball in ball41:
        ball.draw()

    update_canvas()
    delay(0.05)

close_canvas()