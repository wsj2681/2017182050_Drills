import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
from grass import Grass
from ball import Ball, BigBall
from brick import Brick
name = "MainState"

boy = None
grass = None
ball = None
big_ball = None
brick = None
balls = []
big_balls = []


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False
    return True


def enter():
    global boy
    boy = Boy()
    game_world.add_object(boy, 1)

    global grass
    grass = Grass()
    game_world.add_object(grass, 0)

    global brick
    brick = Brick()
    game_world.add_object(brick, 1)

    global ball, big_ball, balls, big_balls
    for i in range(10):
        ball = Ball()
        balls.append(ball)
        big_ball = BigBall()
        big_balls.append(big_ball)
        game_world.add_object(ball, 1)
        game_world.add_object(big_ball, 1)



def exit():
    game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for ball in balls:
        if collide(grass, ball):
            ball.stop()
    for big_ball in big_balls:
        if collide(grass, big_ball):
            big_ball.stop()

    for ball in balls:
        if collide(brick, ball):
            ball.stop()
    for big_ball in big_balls:
        if collide(brick, big_ball):
            big_ball.stop()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
