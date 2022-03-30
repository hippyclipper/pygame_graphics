import pygame
import random

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
done = False

class Firework:
    
    def __init__(self):
        self.x = random.randint(0,width)
        self.y = height
        self.v = random.randint(10,22)*-1
        self.g = .3
        self.r = 10
        self.color = BLUE
        self.exploded = False
        self.explodeV = 5
        
    def update(self):

        if self.v > self.explodeV:
            self.exploded = True
            self.color = RED
            
        self.v += self.g
        self.y += self.v
        
    def isDone(self):
        
        if self.y < 0-self.r or (self.v > 0 and self.y > height):
            return True
        
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
        

fireworks = [Firework() for x in range(3)]

while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
 
    for firework in fireworks:
        firework.update()
        firework.draw()
    for firework in fireworks:
        if firework.isDone():
            fireworks.remove(firework)
            fireworks.append(Firework())
 
 
 
            
    pygame.display.flip()
    clock.tick(60)
    screen.fill(BACKGROUND)
    
#=============================================================
pygame.display.quit()
pygame.quit()         
            
            