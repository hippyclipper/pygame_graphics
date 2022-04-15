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

noise = PerlinNoise(octaves=2, seed=2)



class Square:
    
    def __init__(self,i,j,w):
        self.x1 = i * w
        self.y1 = j * w
        self.scale = 20
        self.z = 0
        self.rads = noise([self.x1/width, self.y1/height, self.z]) * math.pi * 2
        self.x2 = self.x1 + (math.cos(self.rads) * self.scale)
        self.y2 = self.y1 + (math.sin(self.rads) * self.scale)
        self.i = i
        self.j = j
        self.w = w
        self.color = GRAY
        self.n = 0
        
    def update(self):
        self.z += .02
        self.rads = noise([self.x1/width, self.y1/height, self.z]) * math.pi * 2
        self.x2 = self.x1 + (math.cos(self.rads) * self.scale)
        self.y2 = self.y1 + (math.sin(self.rads) * self.scale)
        
    def draw(self):
        pygame.draw.rect(screen,self.color,(self.x1,self.y1,self.w,self.w))
        pygame.draw.circle(screen, RED, (self.x1, self.y1), 10)
        pygame.draw.line(screen, GREEN, (self.x1, self.y1), (self.x2, self.y2), 3)
        

class Board:
    
    def __init__(self):
        
        self.sizeSquare = 50
        self.squares = []
        for x in range(width//self.sizeSquare):
            self.squares.append([])
            for y in range(height//self.sizeSquare):
                self.squares[x].append(Square(x, y, self.sizeSquare))
                                
    def update(self):
        for x in self.squares:
            for y in x:
                y.update()
    
    def draw(self):
        for x in self.squares:
            for y in x:
                y.draw()
                
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