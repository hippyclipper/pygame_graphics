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
GRAY = (132, 121, 121)
BLACK = (25, 23, 22)
BACKGROUND = (5, 5, 5)
COLORLIST = [RED, GREEN, BLUE]
done = False

class Square:
    
    def __init__(self,i,j,w):
        self.x = i * w
        self.y = j * w
        self.i = i
        self.j = j
        self.w = w
        self.color = GRAY
        self.n = 0
        
    def draw(self):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.w,self.w))
        pygame.draw.circle(screen, RED, (self.x, self.y), 1)
        

class Board:
    
    def __init__(self):
        
        self.sizeSquare = 20
        self.squares = []
        for x in range(width//self.sizeSquare):
            self.squares.append([])
            for y in range(height//self.sizeSquare):
                self.squares[x].append(Square(x, y, self.sizeSquare))
                                
    def update(self):
        pass
    
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