import pygame as pg

# Работа с окном
pg.init()                                                                        
win = pg.display.set_mode((1200,750))
pg.display.set_caption("Street Driver 5")   

# Загрузка спрайтов
car = pg.image.load('car_1.png')
wheel = pg.image.load('car_2.png')
bg = pg.image.load('bg.jpg')

snoop = [pg.image.load('01.png'), pg.image.load('02.png'),
         pg.image.load('03.png'), pg.image.load('04.png'),
         pg.image.load('05.png'), pg.image.load('06.png'),
         pg.image.load('07.png'), pg.image.load('08.png'),
         pg.image.load('09.png'), pg.image.load('10.png')]

# Параметры
clock = pg.time.Clock()
animCount = 0
x_car = -364
y_car = 627
x_wheel1 = -321
y_wheel = 678
x_wheel2 = -91
x_dog = 1000
y_dog = 540
speed = 6
angle = 0

# Флажки - действия
isDrive = True

# Данная функция поворачивает изображение отн-но центра
def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pg.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

# Функция отвечающая за картинку на окне
def drawWindow():
    global isDrive, x_car, y_car, x_wheel1, x_wheel2, y_wheel, angle, wheel, animCount
    win.blit(bg, (0,0))

    # Snoop Dogg - animation
    if animCount + 1 <= 61:
        win.blit(snoop[animCount // 7], (x_dog,y_dog))
        animCount += 1
    elif animCount + 1 <= 126:
        win.blit(list(reversed(snoop))[(animCount-60) // 7], (x_dog,y_dog))
        animCount += 1
    else:
        animCount = 0
    

    # Car - animation
    if isDrive:
        if x_car < 1200:
            win.blit(car, (x_car, y_car))
            win.blit(rot_center(wheel, angle), (x_wheel1, y_wheel))
            win.blit(rot_center(wheel, angle), (x_wheel2, y_wheel))
            x_wheel1 += speed
            x_wheel2 += speed
            x_car += speed
            angle -= 7
        else:
            isDrive = False
    else:
        x_car = -364
        x_wheel1 = -321
        x_wheel2 = -91
        win.blit(car, (x_car, y_car))
        win.blit(wheel, (x_wheel1, y_wheel))
        win.blit(wheel, (x_wheel2, y_wheel))
        
    pg.display.update()

# Основной цикл
run = True
while run:
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        if event.type == pg.KEYDOWN:
            isDrive = True

    drawWindow()

pg.quit()
