import pygame
import sys
from pygame.locals import *

pygame.init()

#neco pro git
#dalsi git
#a dalsi
white =(255,255,255)
black = (0,0,0)
red=(200,0,0)
myColor = (50,129,167)
borderColor = (147,183,114)
borderWidth = 20
bg=myColor

fps = 30
dispWidth = 800
dispHeight = 600
cellSize = 5

UP = 'up'
DOWN= 'down'
RIGHT = 'right'
LEFT = 'left'
direction = RIGHT

def runGame():
    startx = 3
    starty = 3
    coords = [{'x': startx, 'y': starty}]
    global direction
    direction = RIGHT

    while True:
        set_direction()
        #print direction
        
        if direction == UP:
            newCell = {'x':coords[0]['x'], 'y':coords[0]['y']-1}

        if direction == DOWN:
            newCell = {'x':coords[0]['x'], 'y':coords[0]['y']+1}
            
        if direction == LEFT:
            newCell = {'x':coords[0]['x']-1, 'y':coords[0]['y']}

        if direction == RIGHT:
            newCell = {'x':coords[0]['x']+1, 'y':coords[0]['y']}

        del coords[-1]

        borders()

        coords.insert(0, newCell)
        #fill the background
        setDisplay.fill(bg)
        #redraw the cell
        drawCell(coords)
        #borders
        borders()        
        pygame.display.update()
        fpsTime.tick(fps)

        #if we are out of borders
        if (newCell['x'] < borderWidth/cellSize - 1) or (newCell['y'] < borderWidth/cellSize - 1) or (newCell['x'] > ((dispWidth-borderWidth)/cellSize)) or (newCell['y'] >((dispHeight-borderWidth)/cellSize)):
            
            print newCell['x']
            print newCell['y']
            print "you died"
            deadText()
            

def deadText():
    x=300
    y=350
    length=200
    height=50
    
    font = pygame.font.SysFont("monospace", 120)
    font_small=pygame.font.SysFont("monospace",30)
    
    label=font.render("You Died!", 1,black)
    label_small=font_small.render("Press enter to continue", 1, red)
    
    setDisplay.blit(label, (100,200))
    setDisplay.blit(label_small, (200,350))

    #pygame.draw.rect(setDisplay, black, (x,y,length,height))
    pygame.display.update()
    pygame.time.wait(1000)
    while True:
        for event in pygame.event.get():
            #print event
            if event.type == MOUSEBUTTONDOWN:
                print "click"
                mouseClickRepeat(pygame.mouse.get_pos(),x, y, length, height)
            if event.type == KEYDOWN:
                runGame()
                
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

#def enterForRepeat()
        
def mouseClickRepeat(mouse, x, y, length, height):
    if mouse[0] >x and mouse[0] < (x+length) and mouse[1]>y and mouse[1]< (y+height):
        runGame()
    

def set_direction():
    global direction
    for event in pygame.event.get():
        #print event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT and direction != RIGHT:
                direction = LEFT
            if event.key == K_RIGHT and direction != LEFT:
                direction = RIGHT
            if event.key == K_DOWN and direction != UP:
                direction = DOWN
            if event.key == K_UP and direction != DOWN:
                direction = UP
    
    

def drawCell(coords):
    for coord in coords:
        x = coord['x']*cellSize
        y=coord['y']*cellSize
        makeCell = pygame.Rect(x,y,cellSize, cellSize)
        pygame.draw.rect(setDisplay, black, makeCell)

def borders():
    pygame.draw.line(setDisplay, borderColor,(0,0),(0,600),borderWidth)
    pygame.draw.line(setDisplay, borderColor,(0,0),(800,0),borderWidth)
    pygame.draw.line(setDisplay, borderColor,(0,600),(800,600),borderWidth)
    pygame.draw.line(setDisplay, borderColor,(800,600),(800,0),borderWidth)
        
    #pygame.display.update()

while True:
    #fpsTime
    #setDisplay

    fpsTime = pygame.time.Clock()
    setDisplay = pygame.display.set_mode((dispWidth,dispHeight))
    pygame.display.set_caption('snake')
    
    runGame()
