import pygame as pg
import math

WINDOW_SIZE = WINDOW_W, WINDOW_H = 500, 400
FPS = 60

if __name__ == '__main__':

	pg.init()

	clock = pg.time.Clock()
	pg.display.set_caption("RK2")
	sc = pg.display.set_mode(WINDOW_SIZE)
	sc.fill("blue")

	srf1 = pg.Surface((100, 100), pg.SRCALPHA)
	srf2 = pg.Surface((100, 100))
	srf1.fill((0, 0, 0, 0))
	
	pg.draw.polygon(srf1, "red", [(0, 0), (50, 50), (0, 100)])
	pg.draw.polygon(srf1, "green", [(0, 0), (50, 50), (100, 0)])
	pg.draw.polygon(srf1, "white", [(100, 0), (50, 50), (100, 100)])
	pg.draw.polygon(srf1, "black", [(100, 100), (50, 50), (0, 100)])

	center = x_c, y_c = (200, 200)

	rect1 = srf1.get_rect()
	rect1.center = center
	
	angle = 0
	angle2 = 0
	radius = 100

	while True:
		sc.fill("blue")
		for event in pg.event.get():
			if event.type == pg.QUIT:
				exit(0)
		
		rotated_srf1 = pg.transform.rotate(srf1, angle)
		rotated_rect1 = rotated_srf1.get_rect()
		radians_angle2 = math.radians(angle2)
		rotated_rect1.center = (x_c + radius * math.cos(radians_angle2), y_c + radius * math.sin(radians_angle2))

		angle += 1
		angle2 += 3

		sc.blit(rotated_srf1, rotated_rect1)
		pg.display.flip()
		clock.tick(FPS)
