import game_framework
from pico2d import *
import main_state

name = "PauseState"
image = None
flag = None


def enter():
    global image, flag
    image = load_image('pause.png')
    flag = 1


def exit():
    global image
    del(image)


def update():
    update_canvas()


def draw():
    global image, flag

    if flag is 1:
        image.draw(400, 300, 300, 300)
        update()
        delay(0.5)
        flag = 0
    elif flag is 0:
        main_state.draw()
        enter()
        delay(0.5)
        flag = 1

    delay(0.01)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()