import pygame as pg
from math import sin, cos, pi, radians

pg.init()
width = 1000
height = 600
win = pg.display.set_mode((width, height))
pg.display.set_caption("PYGAME")
run = True
'''
r = pg.Rect(50, 100, 100, 200)
pg.draw.rect(win, "blue", r, 0)
pg.draw.line(win, "red", (10,10), (20,20), 1)
pg.draw.lines(win, "white", True, ((100,100),(20,20),(40,50),(50,40)), 1)
pg.draw.circle(win, "red", (500, 500), 50, 0)
pg.draw.ellipse(win, "red", r, 0)
pg.draw.polygon(win, "orange", ((500, 500), (600, 500), (800, 800)), 0)
pg.draw.arc(win, "white", (50, 50, 100, 100), 3.14, 3.14/2, 100)
'''

x = 0
y = 200 + sin(0)* 100
w, h = 100, 100
z = 0
sd = 0.01
sd_y = 0.005
sx = 0.5
sc = 0
while run:
    win.fill((50, 10, 15))
    pg.draw.arc(win, "white", (x, y, w, h), 0 + sc, (pi/2) + sc, 100)
    pg.draw.arc(win, "blue", (x, y, w, h), (pi/2) + sc, pi + sc, 100)
    pg.draw.arc(win, "red", (x, y, w, h), (pi) + sc, (pi*3/2) + sc, 100)
    pg.draw.arc(win, "orange", (x, y, w, h), (pi*3/2) + sc, 2*pi + sc, 100)
    sc += sd
    x += sx
    z += sd_y
    y = 200 + sin(z) * 100
    if (x > width):
        x = -15
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    pg.display.flip()
    pg.display.update()


srf1 = pg.Surface((120, 120), pg.SRCALPHA)
srf1.fill((0, 0, 0, 0))

x = 10
y = 10
w, h = 100, 100
center = x_c, y_c = 300 , 300

rect1 = srf1.get_rect()
rect1.center = center
angle = 0
angle2 = 0
radius = 100
    
run = True
while run:
    win.fill((50, 10, 15))
    
    pg.draw.arc(srf1, "white", (x, y, w, h), 0, (pi/2), 100)
    pg.draw.arc(srf1, "blue", (x, y, w, h), (pi/2), pi, 100)
    pg.draw.arc(srf1, "red", (x, y, w, h), (pi), (pi*3/2), 100)
    pg.draw.arc(srf1, "orange", (x, y, w, h), (pi*3/2), 2*pi, 100)

    rotated_srf1 = pg.transform.rotate(srf1, angle)
    rotated_rect1 = rotated_srf1.get_rect()
    radians_angle2 = radians(angle2)
    rotated_rect1.center = (x_c + radius * cos(radians_angle2), y_c + radius * sin(radians_angle2))

    angle += 0.5
    angle2 += 0.3

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    win.blit(rotated_srf1, rotated_rect1)
    pg.display.flip()


coor = 100
x = 0
y = 0
srf1 = pg.Surface((coor, coor), pg.SRCALPHA)
srf1.fill((0,0,0))
t = coor/2
center = x_c, y_c = t , 200  + cos(0) * 100 
rect1 = srf1.get_rect()
rect1.center = center
speed = 0.3
sd = 0.005
z = 0
angle = 0
run = True
while run:
    win.fill((50, 10, 15))
    
    pg.draw.polygon(srf1, "white", ((x, y), (x + t, y + t), (x, y + 2*t)))
    pg.draw.polygon(srf1, "blue", ((x, y), (x + t, y + t), (x + 2*t, y)))
    pg.draw.polygon(srf1, "red", ((x + 2*t, y), (x + t, y + t), (x + 2*t, y + 2*t)))
    pg.draw.polygon(srf1, "orange", ((x + 2*t, y + 2*t), (x + t, y + t), (x, y + 2*t)))

    r_srf1 = pg.transform.rotate(srf1, angle)
    
    x_c += speed
    z += sd
    y_c = 200 + cos(z) * 100
    center = x_c, y_c
    r_rect1 = r_srf1.get_rect()
    r_rect1.center = center
    angle += 0.2
    if x_c > width:
        x_c = t
        z = 0
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    win.blit(r_srf1, r_rect1)
    pg.display.flip()



coor = 100
x = 0
y = 0
srf1 = pg.Surface((coor, coor), pg.SRCALPHA)
srf1.fill((0,0,0))
t = coor/2
center = x_c, y_c = 200, 200
rect1 = srf1.get_rect()
rect1.center = center
angle = 0
angle2 = 0
r = 100
run = True
while run:
    win.fill((50, 10, 15))
    
    pg.draw.polygon(srf1, "white", ((x, y), (x + t, y + t), (x, y + 2*t)))
    pg.draw.polygon(srf1, "blue", ((x, y), (x + t, y + t), (x + 2*t, y)))
    pg.draw.polygon(srf1, "red", ((x + 2*t, y), (x + t, y + t), (x + 2*t, y + 2*t)))
    pg.draw.polygon(srf1, "orange", ((x + 2*t, y + 2*t), (x + t, y + t), (x, y + 2*t)))

    r_srf1 = pg.transform.rotate(srf1, angle)
    r_rect1 = r_srf1.get_rect()
    r_ang = radians(angle2)
    r_rect1.center = (x_c + r * cos(r_ang), y_c + r * sin(r_ang))
    angle += 0.4
    angle2 += 0.15

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    win.blit(r_srf1, r_rect1)
    
    pg.display.flip()
pg.quit()
