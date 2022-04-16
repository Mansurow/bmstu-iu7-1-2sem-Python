import pygame as pg
from math import *


pg.init()

size = width, height = 1000, 600
win = pg.display.set_mode(size)
pg.display.set_caption("RK_2")

radius = 40
center_c = x_cc, y_cc = 40, 40
t = 1
n = int(input("N = "))
angle = int(input("ANGLE = "))

srf1 = pg.Surface((210, 110), pg.SRCALPHA)
srf1.fill((0,0,0))
center = x_c, y_c = 300 , 300 
rect1 = srf1.get_rect()
rect1.center = center
run = True
center_pram = x_p, y_p = 100  ,50 * t
i = 0
while run:
    win.fill((0, 0, 0))
    pg.draw.lines(srf1, "blue", True, ((0, 0), (200, 0 ), (200, 100), (0, 100)),2)
    pg.draw.arc(srf1, "blue", (10 , 10, 40, 40), 0, 2*pi, 2)
    pg.draw.line(srf1, "blue", (18, 16), (42, 42), 1)
    pg.draw.line(srf1, "blue", (42, 42), (42, 37) , 1)
    pg.draw.line(srf1, "blue", (42, 42), (37, 42) , 1)
    pg.draw.line(srf1, "blue", (18, 16), (23, 16) , 1)
    pg.draw.line(srf1, "blue", (18, 16), (18, 21) , 1)
    r_srf1 = pg.transform.rotate(srf1, angle)
    r_rect1 = r_srf1.get_rect()
    angle += 0.2
    i += angle / 300;
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    if i >= n * angle:
        win.blit(r_srf1, rect1)
        pg.display.flip()
    if i == n:
        run = False
pg.quit()
