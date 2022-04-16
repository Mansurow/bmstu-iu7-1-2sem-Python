import pygame as pg
import random as rd

pg.init()
window = pg.display.set_mode((1200, 750))
pg.display.set_caption("Car Animation Loop")


width_cars = 366
height_cars = 94
width_bg = 1200
height_bg = 750

car_1 = pg.image.load('car_1.png')
car_2 = pg.image.load('car_2.png')
wheel = pg.image.load('wheel.png')
car_2 = pg.transform.scale(car_2, (width_cars, height_cars))
bg_1 = pg.image.load('bg-1.jpg')
bg_1 = pg.transform.scale(bg_1, (width_bg, height_bg))
bg_2 = pg.transform.scale(bg_1, (width_bg, height_bg))

x_bg_1 = 0
x_bg_2 = 1200
speed_bg = 12
# x y car_1 и ее колес
x_car_1 = 450
y_car_1 = 510
x_wheel_car_1_1 = 492
y_wheel_car_1_1 = 560
x_wheel_car_1_2 = 720
y_wheel_car_1_2 = 560
speed_car_1 = 20

# x y car_2 и ее колес
x_car_2 = 1200
y_car_2 = 600
x_wheel_car_2_1 = 1250
y_wheel_car_2_1 = 655
x_wheel_car_2_2 = 1480
y_wheel_car_2_2 = 648
speed_car_2 = 25

angle_1 = 0
angle_2 = 0
time = 0
time_delay_car =rd.randint(50, 100)
print(time_delay_car)
p_cars = True

def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pg.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


def draw_car(car, wheel_1, wheel_2, x_car, y_car, x_wheel_1, y_wheel_1, x_wheel_2, y_wheel_2, angle):
    window.blit(car,(x_car ,y_car))
    window.blit(wheel_1, (x_wheel_1, y_wheel_1))
    window.blit(wheel_2, (x_wheel_2, y_wheel_2))
    window.blit(rot_center(wheel_1, angle), (x_wheel_1, y_wheel_1))
    window.blit(rot_center(wheel_2, angle), (x_wheel_2, y_wheel_2))
def draw():
    global angle_1, angle_2, time, time_delay_car, x_car_2, x_wheel_car_2_1, x_wheel_car_2_2, p_cars

    # главная машина
    draw_car(car_1, wheel, wheel, x_car_1, y_car_1, x_wheel_car_1_1, y_wheel_car_1_1, x_wheel_car_1_2, y_wheel_car_1_2, angle_1)
    angle_1 -= speed_car_1

    # встречные машины

    if time == time_delay_car:
        if p_cars == True:
            draw_car(car_2, wheel, pg.transform.scale(wheel, (66, 66)), x_car_2, y_car_2, x_wheel_car_2_1, y_wheel_car_2_1, x_wheel_car_2_2, y_wheel_car_2_2, angle_2)
            p_cars = False
        if p_cars == False:
            draw_car(car_2, wheel, pg.transform.scale(wheel, (66, 66)), x_car_2, y_car_2, x_wheel_car_2_1, y_wheel_car_2_1, x_wheel_car_2_2, y_wheel_car_2_2, angle_2)
            x_car_2 -= speed_car_2
            x_wheel_car_2_1 -= speed_car_2
            x_wheel_car_2_2 -= speed_car_2
            angle_2 += speed_car_2 + 10
            if x_car_2 < -400:
                time_delay_car = rd.randint(100, 1000)
                time = 0
                x_car_2 = 1200
                x_wheel_car_2_1 = 1250
                x_wheel_car_2_2 = 1480
            
    else:
        time += 1
    

run = True
while run:
    pg.time.delay(10)
    window.fill((0,0,0))
    window.blit(bg_1, (x_bg_1, 0))
    window.blit(bg_1, (x_bg_2, 0))
    if (x_bg_1 < -1199):
        x_bg_1 = width_bg
    if (x_bg_2 < -1199):
        x_bg_2 = width_bg
    
    x_bg_1 -= speed_bg
    x_bg_2 -= speed_bg
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    draw()
    pg.display.update()
pg.quit()
