import pygame
import random
import math
import time

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
COLORLIST = [RED, BLUE]
done = False

class Square:
    
    def __init__(self,i,j,w):
        self.x = i * w
        self.y = j * w
        self.i = i
        self.j = j
        self.w = w
        self.color = RED
        self.n = 0

        
    def draw(self):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.w,self.w))
        

class Board:
    
    def __init__(self):
        
        self.sizeSquare = 20
        self.squares = []
        for x in range(width//self.sizeSquare):
            self.squares.append([])
            for y in range(height//self.sizeSquare):
                self.squares[x].append(Square(x, y, self.sizeSquare))
                
    
    def checkSquare(self,x,y):
        dirs = [[-1,-1,],[-1,0,],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        i = 0
        j = 0
        self.squares[x][y].n = 0
        for side in dirs:
            i = x + side[0]
            j = y + side[1]
            if (i < 0 or i >= width//self.sizeSquare) or (j < 0 or j >= height//self.sizeSquare):
                continue
            if self.squares[i][j].color == BLUE:
                self.squares[x][y].n += 1
                                
    def calcNextDoor(self):
        for x in range(len(self.squares[0])):
            for y in range(len(self.squares)):
                self.checkSquare(x,y)
                
    def updateColor(self):
        for row in self.squares:
            for square in row:
                if square.color == BLUE and (square.n == 3 or square.n == 2):
                    square.color = BLUE
                elif square.color == RED and square.n == 3:
                    square.color = BLUE
                else:
                    square.color = RED
                
    def update(self):
        self.calcNextDoor()
        self.updateColor()
                
    def draw(self):
        for x in self.squares:
            for y in x:
                y.draw()
        
board = Board()

offset = 20
board.squares[0+offset][0+offset].color = BLUE
board.squares[1+offset][0+offset].color = BLUE
board.squares[2+offset][0+offset].color = BLUE
board.squares[2+offset][1+offset].color = BLUE
board.squares[1+offset][2+offset].color = BLUE
# board.squares[21][20].color = BLUE
# board.squares[31][21].color = BLUE


while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    board.update()
    board.draw()

 
    pygame.display.flip()
    clock.tick(60)
    screen.fill(BACKGROUND)
    time.sleep(.5)
#=============================================================
pygame.display.quit()
pygame.quit()    