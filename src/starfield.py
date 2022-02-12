import pygame
#=============================================================
screenScale = 8
width = int(100 * screenScale)
height = width
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
LEFT_MOUSE = 1
RIGHT_MOUSE = 3
done = False
pygame.init()
pygame.mixer.init()
pygame.font.init()
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
#=============================================================
while not done:
    
    pressed = pygame.key.get_pressed()
    x, y = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    pygame.display.flip()
    clock.tick(60)
    screen.fill((0, 0, 0))

#=============================================================
pygame.display.quit()
pygame.quit()