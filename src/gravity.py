import pygame
import random
import math

LEFT_MOUSE = 1
RIGHT_MOUSE = 3
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

# F = G ( m1*m2/r**2 )
# F = m*a
# a = m / F
# v += a

class Body:
    
    def __init__(self,x,y,r):
        self.density = 1
        self.x = x
        self.y = y
        self.v = [0,0]
        self.r = r
        self.m = math.pi * r**2 * self.density
        self.color = (150, 150, 149)
        self.colorLine = (255, 255, 255)
    
    def update(self):
        self.x += self.v[0]
        self.y += self.v[1]
    
    def draw(self):
        pygame.draw.circle(screen, self.colorLine, (self.x, self.y), self.r+3)
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
        
        
def collide(mover, moved):
    G = .1
    massProduct = mover.m * moved.m
    distance = max(mover.r+moved.r, pygame.math.Vector2(mover.x, mover.y).distance_to((moved.x, moved.y)))
    F = G * (massProduct/distance**2)
    dx = mover.x - moved.x
    dy = mover.y - moved.y
    vx = (dx/distance)*(F/moved.m)
    vy = (dy/distance)*(F/moved.m)
    moved.v[0] += vx
    moved.v[1] += vy
        
#numBodies = 10
#bodies = [Body(random.randint(0, width), random.randint(0, height), random.randint(10,20)) for x in range(numBodies)]
#body1 = Body(width//2, height//2, 25)
#body2 = Body(width//2-100, height//2+303, 25)
bodies = []
x, y = 0, 0
while not done:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button ==  LEFT_MOUSE:           
            x, y = pygame.mouse.get_pos()
            bodies.append(Body(x, y, random.randint(10,20)))
            
            
    for x in bodies:
        for y in bodies:
            if x == y:
                continue
            else:
                collide(x, y)
                collide(y, x)
    for x in bodies:
        x.update()
    for x in bodies:
        x.draw()
            
    pygame.display.flip()
    clock.tick(60)
    screen.fill(BACKGROUND)
    
#=============================================================
pygame.display.quit()
pygame.quit()         