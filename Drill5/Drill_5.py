from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def Follow_cursor():
    global Following
    global x, y
    global cx,cy
    global arrow
    global click
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Following = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.type == SDLK_ESCAPE:
            Following = False

        elif event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x - 20, KPU_HEIGHT - 1 - event.y + 20
            click = True
            if x < cx:
                arrow = 0
            elif x > cx:
                arrow = 1
        elif event.type == SDL_MOUSEBUTTONUP:
            click = False

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
cursor = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')

Following = True
frame = 0
hide_cursor()
Click_Event = False
arrow = 100
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
cx, cy = KPU_WIDTH // 2, KPU_HEIGHT // 2
click = False


while Following:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    cursor.draw(x, y)
    if click:
        if x == cx and y == cy:
            x = 0
            y = 0
        cx += (x - cx) / 100
        cy += (y - cy) / 100

    character.clip_draw(frame * 100, arrow * 100, 100, 100, cx, cy)

    update_canvas()
    frame = (frame + 1) % 8
    Follow_cursor()

close_canvas()
