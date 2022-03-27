import pygame
import math

screenScale = 8
width = int(100 * screenScale)
height = width
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BACKGROUND = (5,5,5)
done = False
pygame.init()
pygame.mixer.init()
pygame.font.init()
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

class Circle:
    
    def __init__(self,x,y,r, rads):
        self.x = x
        self.y = y
        self.r = r
        self.rads = rads
        
    def draw(self):
        pygame.draw.circle(screen, BLUE, (self.x, self.y), self.r)
        
class Circles:
    
    def __init__(self):
        self.circles = []
        self.numCircles = 10
        self.bigRad = 100
        r = 20
        
        for i in range(self.numCircles):
            degree = i/self.numCircles * 360
            radians = math.radians(degree)
            centerX = width//2
            centerY = height//2
            x = centerX + (math.cos(radians) * self.bigRad)          
            y = centerY + (math.sin(radians) * self.bigRad)
            self.circles.append(Circle(x,y,r, radians))
            
    def update(self):
        for x in self.circles:
            x.rads += .01
            x.x = width//2 + math.cos(x.rads)*self.bigRad
            x.y = height//2 + math.sin(x.rads)*self.bigRad

    def draw(self):
        for x in self.circles:
            x.draw()
        
circles = Circles()  
while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    circles.draw()
    circles.update()
    pygame.display.flip()
    clock.tick(60)
    screen.fill(BACKGROUND)
    
#=============================================================
pygame.display.quit()
pygame.quit()