import pygame
import random
import math

#=============================================================================

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

#=============================================================================

class Walls:
    
    def __init__(self):
        self.walls = []
        
    def addWall(self, first, second):
        self.walls.append(Wall(first, second))
        
    def draw(self):
        for wall in self.walls:
            wall.draw()
            
#=============================================================================
            
class Wall:
    
    def __init__(self, first,second):
        self.x1 = first[0]
        self.y1 = first[1]
        self.x2 = second[0]
        self.y2 = second[1]
        self.lineWidth = 2
                
    def draw(self):
        pygame.draw.line(screen, GREEN, (self.x1, self.y1), (self.x2, self.y2),self.lineWidth)
        
#=============================================================================
        
class Ray:
    
    def __init__(self, x,y,rads):
        self.scale = 200
        self.x1 = x
        self.y1 = y
        self.x2 = x + (math.cos(rads)*self.scale)
        self.y2 = y + (math.sin(rads)*self.scale)
        self.lineWidth = 2
        self.rads = rads
                
    def intersectionPoint(self, wall):
        yd = self.y2-self.y1
        xd = self.x2-self.x1
        
    def update(self, x, y):
        self.x1 = x
        self.y1 = y
        self.x2 = x + (math.cos(self.rads)*self.scale)
        self.y2 = y + (math.sin(self.rads)*self.scale)
        
    def draw(self):
        pygame.draw.line(screen, RED, (self.x1, self.y1), (self.x2, self.y2),self.lineWidth)
        
#=============================================================================
        
class Player:
    
    def __init__(self):
        self.x = width // 2
        self.y = height // 2
        self.r = 10
        self.numRays = 20
        self.rays = []
        for ray in range(self.numRays):
            rads = math.radians((ray/self.numRays) * 360)
            self.rays.append(Ray(self.x, self.y, rads))
        
    def update(self,x,y):
        self.x = x
        self.y = y
        for ray in self.rays:
            ray.update(x,y)
    
    def draw(self):
        for ray in self.rays:
            ray.draw()
        pygame.draw.circle(screen, RED, (self.x, self.y), self.r)
        
#=============================================================================
        
player = Player()
walls = Walls()
walls.addWall((10,150),(200, 10))

#=============================================================================

while not done:
    
    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    walls.draw() 
    player.update(x,y)
    player.draw()
            
    pygame.display.flip()
    clock.tick(60)
    screen.fill(BACKGROUND)
    
#=============================================================================
    
pygame.display.quit()
pygame.quit()    