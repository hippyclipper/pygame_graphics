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
BACKGROUND = (5, 5, 5)
done = False

class Spark:
    
    def __init__(self):
        v = random.randint(1,10)
        self.xv = random.uniform(-v,v)
        self.yv = math.sqrt(v**2 - self.xv**2) * [1,-1][random.randint(0,1)]
        self.y = 0
        self.x = 0
        self.g = .1
        self.decell = random.uniform(.90,.95)
        self.r = 10 * random.uniform(.5,.1)
        self.color = RED
        self.timer = self.r
        self.timerDelta = .1
        self.isDone = False
        
    def update(self):
        
        self.x += self.xv
        self.y += self.yv
        self.yv += self.g
        self.xv *= self.decell
        self.yv *= self.decell
        self.timer -= self.timerDelta
        if self.timer < 0:
            self.isDone = True
        
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
        

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
        self.sparks = [Spark() for x in range(100)]
        
        
    def update(self):

        if self.v > self.explodeV and not self.exploded:
            self.exploded = True
            self.color = RED
            for spark in self.sparks:
                spark.x = self.x
                spark.y = self.y
        if not self.exploded:  
            self.v += self.g
            self.y += self.v
        else:
            for spark in self.sparks:
                spark.update()
            for spark in self.sparks:
                if spark.isDone:
                    self.sparks.remove(spark)
        
    def isDone(self):
        
        if self.y < 0-self.r or (self.v > 0 and self.y > height):
            return True
        return len(self.sparks) == 0
        
    def draw(self):
        if not self.exploded:
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
        else:
            for spark in self.sparks:
                spark.draw()

fireworks = [Firework() for x in range(6)]

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
            
            