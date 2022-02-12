import pygame
import random

#=============================================================

screenScale = 8
width = int(100 * screenScale)
height = width
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BACKGROUND = (5,5,5)
LEFT_MOUSE = 1
RIGHT_MOUSE = 3
done = False
pygame.init()
pygame.mixer.init()
pygame.font.init()
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

#=============================================================

class Star:
    
    def __init__(self):
        
        self.x = random.randint(0,width)
        self.y = random.randint(0,height)
        self.r = random.randint(2,8)
        self.whiteLevel = (255//9) * self.r
        self.color = (self.whiteLevel, self.whiteLevel, self.whiteLevel)
        
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
        
#=============================================================
        
class StarField:
    
    def __init__(self):
        self.numStars = 100
        self.stars = [Star() for x in range(self.numStars)]
        self.stars.sort(key=lambda x: x.whiteLevel)
        
    def update(self):
        for x in self.stars:
            if x.y - x.r > height:
                x.y = 0-x.r
                x.x = random.randint(0,width)
            else:
                x.y += x.whiteLevel//56
                
    def draw(self):
        self.update()
        for x in self.stars:
            x.draw()
            
#=============================================================
            
starField = StarField()

while not done:
    
    pressed = pygame.key.get_pressed()
    x, y = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    starField.draw()
    pygame.display.flip()
    clock.tick(60)
    screen.fill(BACKGROUND)

#=============================================================
pygame.display.quit()
pygame.quit()