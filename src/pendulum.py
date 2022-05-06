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

class Pendulum:
    
    def __init__(self, x, y, d):
        self.r = 5
        self.x1 = x
        self.y1 = y
        self.x2 = x
        self.y2 = y+d
        self.d = d
        self.rads = math.pi/4
        self.seed = 0
        self.scalar = math.sin(self.seed)
        self.rotation = math.pi/2

        
    def update(self):
        self.seed += .05
        self.scalar = math.sin(self.seed)
        self.x2 = self.x1 + (math.cos(self.rotation + (self.rads * self.scalar)) * self.d)          
        self.y2 = self.y1 + (math.sin(self.rotation + (self.rads * self.scalar)) * self.d)
    
    def draw(self):
        pygame.draw.circle(screen, RED, (self.x1,self.y1), self.r)
        pygame.draw.line(screen, RED, (self.x1, self.y1), (self.x2, self.y2), 1)  
        pygame.draw.circle(screen, BLUE, (self.x2,self.y2), self.r)

        
        

pendulum = Pendulum(width//2, 20, 500)



while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
                   

    pendulum.update()
    pendulum.draw()  
            
    pygame.display.flip()
    clock.tick(60)
    screen.fill(BACKGROUND)
    
#=============================================================
pygame.display.quit()
pygame.quit()    