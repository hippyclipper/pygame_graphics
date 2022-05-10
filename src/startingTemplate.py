import pygame
import random
import math

screenScale = 8
width = int(100 * screenScale)
height = width
pygame.init()
pygame.mixer.init()
pygame.font.init()
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BACKGROUND = (5, 5, 5)
COLORLIST = [RED, GREEN, BLUE]
done = False

while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = True           
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:           
            pass     
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            pass
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            pass      
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            pass
        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            pass
            
    pygame.draw.circle(screen, RED, (width//2, height//2), 100)      
            
    pygame.display.flip()
    clock.tick(60)
    screen.fill(BACKGROUND)
    
#=============================================================
pygame.display.quit()
pygame.quit()    