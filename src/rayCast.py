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
        self.contacts = []
        self.contact = None

                
    def intersectionPoint(self, wall):
        yd = self.y2-self.y1
        xd = self.x2-self.x1
        
    def update(self, x, y):
        self.x1 = x
        self.y1 = y
        self.x2 = x + (math.cos(self.rads)*self.scale)
        self.y2 = y + (math.sin(self.rads)*self.scale)
        
        if len(self.contacts) == 0:
            self.contact = None
            return
        
        dist = pygame.math.Vector2(self.contacts[0][0], self.contacts[0][1]).distance_to((self.x1, self.y1))
        final = [self.contacts[0][0], self.contacts[0][1]]
        
        if len(self.contacts) > 1: 
            for Pv in self.contacts[1:]:                
                if pygame.math.Vector2(Pv[0], Pv[1]).distance_to((self.x1, self.y1)) < dist:
                    dist = pygame.math.Vector2(Pv[0], Pv[1]).distance_to((self.x1, self.y1))
                    final = Pv
        self.contact = final

        #self.contacts = [dist[min(dist, key=dist.get)]]
        

        
    def draw(self):
        if not self.contact == None:
            pygame.draw.circle(screen, GREEN, (self.contact[0], self.contact[1]), 10)
        pygame.draw.line(screen, RED, (self.x1, self.y1), (self.x2, self.y2),self.lineWidth)
        self.contacts = []
        self.contact = None
        
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

def contact(wall, ray):
    x1 = wall.x1
    y1 = wall.y1
    
    x2 = wall.x2
    y2 = wall.y2
    
    x3 = ray.x1
    y3 = ray.y1
    
    x4 = ray.x2
    y4 = ray.y2
    
    D = ((x1 - x2) * (y3-y4)) - ((y1 - y2) * (x3 - x4))
    
    if D == 0:
        return
    
    t = (((x1-x3) * (y3-y4)) - ((y1-y3) * (x3-x4))) / D
    u = (((x1-x3) * (y1-y2)) - ((y1-y3) * (x1-x2))) / D
    
    if not (0 <= t <= 1 and 0 <= u <= 1):
        return
    
    Px = x1 + (t * (x2-x1))
    Py = y1 + (t * (y2-y1))
    ray.contacts.append([Px,Py])
    #pygame.draw.circle(screen, BLUE, (Px, Py), 11)
        
#=============================================================================
        
player = Player()
walls = Walls()
offset =  height//2
offset1 =  offset + 20
walls.addWall((10+offset,150+offset),(200+offset, 10+offset))
walls.addWall((10+offset1,150+offset1),(200+offset1, 10+offset1))

#=============================================================================

while not done:
    
    x, y = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    for wall in walls.walls:
        for ray in player.rays:
            contact(wall, ray)
            
    walls.draw() 
    player.update(x,y)
    player.draw()
            
    pygame.display.flip()
    clock.tick(60)
    screen.fill(BACKGROUND)
    
#=============================================================================
    
pygame.display.quit()
pygame.quit()    