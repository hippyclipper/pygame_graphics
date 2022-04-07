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
COLORLIST = [RED, GREEN, BLUE]
done = False

class Square:
    
    def __init__(self,i,j,w):
        self.x = i * w
        self.y = j * w
        self.i = i
        self.j = j
        self.w = w
        self.color = RED

        
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
        pass
                
    def calcNextDoor(self):
        for x in range(len(self.sizeSquare[0])):
            for y in range(len(self.sizeSquare)):
                self.checkSquare(x,y)
        
                
    def draw(self):
        for x in self.squares:
            for y in x:
                y.draw()
        
board = Board()

testSquare = Square(0, 0, 20)
testSquare.color = BLUE

board.squares[30][20].color = GREEN
board.squares[31][20].color = GREEN
board.squares[33][22].color = GREEN
board.squares[36][27].color = GREEN
board.squares[36][28].color = GREEN
board.squares[21][20].color = GREEN
board.squares[31][21].color = GREEN

while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    board.draw()
    testSquare.draw()
    
    if testSquare.color == BLUE:
         testSquare.color = RED
    else:
        testSquare.color = BLUE
 
    pygame.display.flip()
    clock.tick(60)
    screen.fill(BACKGROUND)
    time.sleep(.5)
#=============================================================
pygame.display.quit()
pygame.quit()    