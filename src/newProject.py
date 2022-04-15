import pygame
import random
import math
from perlin_noise import PerlinNoise


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
GRAY = (132, 121, 121)
BLACK = (25, 23, 22)
BACKGROUND = (5, 5, 5)
COLORLIST = [RED, GREEN, BLUE]
done = False
randseed = random.randint(0,10000)
noise = PerlinNoise(octaves=9, seed=randseed)
print(randseed)

class Particle:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xv = 0
        self.yv = 0
        self.ax = 0
        self.ay = 0
        self.m = .01
        self.r = 2
        self.color = (240,240,240)
        self.deleteMe = False
    
        
    def update(self):
        self.xv = self.ax 
        self.yv = self.ay
        
        self.x += self.xv 
        self.y += self.yv 
        
        if self.y >= height:
            self.y = 0
            self.deleteMe = True
        elif self.y < 0:
            self.y = height
            self.deleteMe = True
            
        if self.x >= width:
            self.x = 0
            self.deleteMe = True
        elif self.x < 0:
            self.x = width
            self.deleteMe = True
            
            
        
    
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
        

class Square:
    
    def __init__(self,i,j,w):
        self.x1 = i * w
        self.y1 = j * w
        self.scale = 10
        self.force = .1
        self.z = 0
        self.rads = .5 #noise([self.x1/width, self.y1/height, self.z]) * math.pi * 2
        self.x2 = self.x1 + (math.cos(self.rads) * self.scale)
        self.y2 = self.y1 + (math.sin(self.rads) * self.scale)
        self.i = i
        self.j = j
        self.w = w
        self.color = GRAY
        self.n = 0
        self.drawVector = False
        
    def update(self):
           
        
        self.z += .01
        self.rads = -2 + noise([self.x1/width, self.y1/height, self.z]) * math.pi * 2
        self.x2 = self.x1 + (math.cos(self.rads+ (.5*math.pi)) * self.scale)
        self.y2 = self.y1 + (math.sin(self.rads) * self.scale)
        
    def draw(self):
        pygame.draw.rect(screen,self.color,(self.x1,self.y1,self.w,self.w))
        if self.drawVector:
            pygame.draw.circle(screen, RED, (self.x1, self.y1), 2)
            pygame.draw.line(screen, GREEN, (self.x1, self.y1), (self.x2, self.y2), 1)
        

class Board:
    
    def __init__(self):
        
        self.sizeSquare = 25
        self.squares = []
        self.particles = []
        self.numParticles = 5000
        
        for x in range(width//self.sizeSquare):
            self.squares.append([])
            for y in range(height//self.sizeSquare):
                self.squares[x].append(Square(x, y, self.sizeSquare))
                
                
    def updateParticels(self):

        for particle in self.particles:
            x = min(int(width//self.sizeSquare)-1, int(particle.x//self.sizeSquare))
            y = min(int(height//self.sizeSquare)-1,int(particle.y//self.sizeSquare))

            rad = self.squares[x][y].rads
            scale = self.squares[x][y].force
            particle.ax = (math.cos(rad) * scale) / particle.m
            particle.ay = (math.sin(rad) * scale) / particle.m            
            particle.update()
            if particle.deleteMe:
                self.particles.remove(particle)
            
            
                
                
                                
    def update(self):
        if len(self.particles) < 10000:
            for x in range(10):
                self.particles.append(Particle(width//2 + random.randint(-10,10), height - 30 + random.randint(-10,10)))
        self.updateParticels()
        
        for x in self.squares:
            for y in x:
                y.update()

    
    def draw(self):
        
        for x in self.squares:
            for y in x:
                y.draw()
                
        for x in self.particles:
            x.draw()
                
board = Board()

while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    board.update()
    board.draw()    
            
    pygame.display.flip()
    clock.tick(60)
    screen.fill(BACKGROUND)
    
#=============================================================
pygame.display.quit()
pygame.quit()    