import pygame
from math import sin, cos


pygame.init()
FPS = 30
RADIUS = 150
VELO1 = -2
VELO2 = 0.1

clock = pygame.time.Clock()

display = pygame.display.set_mode((960, 960))
surf = pygame.Surface((200, 200), pygame.SRCALPHA)
rect = surf.get_rect()
rect.center = (400, 400)

pygame.draw.polygon(surf, (200, 200, 200), ((0, 0), (100, 100), (0, 200)))
pygame.draw.polygon(surf, (100, 100, 200), ((0, 0), (100, 100), (200, 0)))
pygame.draw.polygon(surf, (200, 200, 100), ((0, 200), (100, 100), (200, 200)))
pygame.draw.polygon(surf, (200, 100, 200), ((200, 0), (100, 100), (200, 200)))
    
run = True
i = 0
while run:
    i += 1
    clock.tick(FPS)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False

    display.fill((0, 0, 0))    
        
    surf2 = pygame.transform.rotate(surf, VELO1*i/3.14)
    rect2 = surf2.get_rect()
    rect2.center = rect.center
    rect2 = rect2.move(RADIUS*sin(VELO2*i/3.14), RADIUS*cos(VELO2*i/3.14))    
       
    display.blit(surf2, rect2)
    pygame.display.flip()    
    
            
pygame.quit()

