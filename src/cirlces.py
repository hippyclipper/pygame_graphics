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
    
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r
        
    def draw(self):
        pygame.draw.circle(screen, BLUE, (self.x, self.y), self.r)
        
class Circles:
    
    def __init__(self):
        self.circles = []
        self.numCircles = 3
        r = 20
        
        for i in range(self.numCircles):
            degree = i/self.numCircles * 360
            radians = math.radians(degree)
            centerX = width//2
            centerY = height//2
            x = centerX + (math.cos(radians) * 100)          
            y = centerY + (math.sin(radians) * 100)
            self.circles.append(Circle(x,y,r))

    def draw(self):
        for x in self.circles:
            x.draw()
        
circles = Circles()  
while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    circles.draw()
    pygame.display.flip()
    clock.tick(60)
    screen.fill(BACKGROUND)
    
#=============================================================
pygame.display.quit()
pygame.quit()