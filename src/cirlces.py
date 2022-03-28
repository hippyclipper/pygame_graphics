import pygame
import math

screenScale = 8
width = int(100 * screenScale)
height = width
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BACKGROUND = (68, 17, 81)
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
        self.color = (141, 134, 201)
        
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
        
class Circles:
    
    def __init__(self, bigRad, num, sRad, scale, color=(141, 134, 201)):
        
        self.circles = []
        self.numCircles = num
        self.bigRad = bigRad
        self.smallRad = sRad
        self.middleX = width//2
        self.middleY = height//2
        self.counter = 0
        self.radScale = scale
        self.color = color
        for i in range(self.numCircles):
            radians = math.radians(i/self.numCircles * 360)
            x = self.middleX + (math.cos(radians) * self.bigRad)          
            y = self.middleY + (math.sin(radians) * self.bigRad)
            self.circles.append(Circle(x,y,self.smallRad, radians))
            self.circles[-1].color = self.color

    def update(self):
        for x in self.circles:
            x.rads += .01
            x.x = self.middleX + math.cos(x.rads)*self.bigRad
            x.y = self.middleY + math.sin(x.rads)*self.bigRad
        self.bigRad += math.sin(self.counter)*5 * self.radScale
        self.counter += .1

    def draw(self):
        for x in self.circles:
            x.draw()
        
circles = Circles(150, 7, 20, 1)
smallHalos = [Circles(30, 7, 10, .5, (89, 195, 195)) for x in range(circles.numCircles)]
while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    #circles.draw()
    circles.update()
    for i,x in enumerate(smallHalos):
        x.middleX = circles.circles[i].x
        x.middleY = circles.circles[i].y
        x.update()
        x.draw()
    circles.draw()
    pygame.display.flip()
    clock.tick(60)
    screen.fill(BACKGROUND)
    
#=============================================================
pygame.display.quit()
pygame.quit()