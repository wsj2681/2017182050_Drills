from pico2d import *
import random


# init
KPU_WIDTH, KPU_HEIGHT = 1280, 1024
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

arrow = 100
frame = 0
idx = 0
running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
x1, y1 = KPU_WIDTH // 2, KPU_HEIGHT // 2

move_location = []

def curve_moving(points):
    global move_location
    global flag


    for i in range(0, 100, 2):
        t = i / 100
        mr = mathematics_type_b(t, points[9], points[0], points[1], points[2])
        move_location.append(mr)

    for i in range(0, 100, 2):
        t = i / 100
        mr = mathematics_type_b(t, points[0], points[1], points[2], points[3])
        move_location.append(mr)

    for i in range(0, 100, 2):
        t = i / 100
        mr = mathematics_type_b(t, points[1], points[2], points[3], points[4])
        move_location.append(mr)


    for i in range(0, 100, 2):
        t = i / 100
        mr = mathematics_type_b(t, points[2], points[3], points[4], points[5])
        move_location.append(mr)

    for i in range(0, 100, 2):
        t = i / 100
        mr = mathematics_type_b(t, points[3], points[4], points[5], points[6])
        move_location.append(mr)


    for i in range(0, 100, 2):
        t = i / 100
        mr = mathematics_type_b(t, points[4], points[5], points[6], points[7])
        move_location.append(mr)

    for i in range(0, 100, 2):
        t = i / 100
        mr = mathematics_type_b(t, points[5], points[6], points[7], points[8])
        move_location.append(mr)

    for i in range(0, 100, 2):
        t = i / 100
        mr = mathematics_type_b(t, points[6], points[7], points[8], points[9])
        move_location.append(mr)

    for i in range(0, 100, 2):
        t = i / 100
        mr = mathematics_type_b(t, points[7], points[8], points[9], points[0])
        move_location.append(mr)


    for i in range(0, 100, 2):
        t = i / 100
        mr = mathematics_type_b(t, points[8], points[9], points[0], points[1])
        move_location.append(mr)




def mathematics_type_a(t, a, b, c):
    mx = (2*t**2-3*t+1)*a[0]+(-4*t**2+4*t)*a[0]+(2*t**2-t)*a[0]
    my = (2*t**2-3*t+1)*a[1]+(-4*t**2+4*t)*a[1]+(2*t**2-t)*a[1]
    return mx, my

def mathematics_type_b(t, a, b, c, d):
    mx = ((-t ** 3 + 2 * t ** 2 - t) * a[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * b[0] + (-3 * t ** 3 + 4 * t ** 2 + t) *
             c[0] + (t ** 3 - t ** 2) * d[0]) / 2
    my = ((-t ** 3 + 2 * t ** 2 - t) * a[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * b[1] + (-3 * t ** 3 + 4 * t ** 2 + t) *
             c[1] + (t ** 3 - t ** 2) * d[1]) / 2
    return mx, my


# random location
points = [(random.randint(0.0, 1280.0), random.randint(0.0, 1024.0)) for i in range(10)]

# list fill
curve_moving(points)
print(len(move_location))
print(move_location)

while running:
    clear_canvas()

    if idx+1 == 499:
        idx = 0

    lx = move_location[idx][0]
    lx2 = move_location[idx+1][0]
    ly = move_location[idx][1]

    if lx > lx2:
        arrow = 0
    else:
        arrow = 100
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, arrow, 100, 100, lx, ly)
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.01)


    idx += 1

close_canvas()
