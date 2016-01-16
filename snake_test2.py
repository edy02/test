import pygame
import sys
from pygame.locals import *
from random import randint

pygame.init()

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
cellSize = 10
stepSize = 10

UP = 'up'
DOWN= 'down'
RIGHT = 'right'
LEFT = 'left'

def runGame():
    startx = 3
    starty = 3
    #list of coords for every cell
    coords = [[startx, starty]]
    
    global food
    food = []
    
    global direction
    #default direction
    direction = RIGHT
    
    global next_coord
    next_coord = []

    while True:
        set_direction()
       
        #print direction

        #source of coord is left-top corner -> down +y, right +x
        if direction == UP:
            #-1 to y of first list in list of coords (first cell of snake)
            next_coord=[coords[0][0],coords[0][1]-1]
            
        elif direction == DOWN:
            next_coord=[coords[0][0],coords[0][1]+1]
            
        elif direction == LEFT:
            next_coord=[coords[0][0]-1,coords[0][1]]
            
        elif direction == RIGHT:
            next_coord=[coords[0][0]+1,coords[0][1]]
            

        #if we are out of borders
        if (next_coord[0] < borderWidth/cellSize - 1) or (next_coord[1] < borderWidth/cellSize - 1) or (next_coord[0] > ((dispWidth-borderWidth)/cellSize)) or (next_coord[1] >((dispHeight-borderWidth)/cellSize)):
            deadText()

        check_collision(coords)  

        #if a food is eaten
        if len(food)!=0 and next_coord[0]== food[0] and next_coord[1]==food[1]:
            new_coord_food= [food[0],food[1]]
            coords.insert(0,new_coord_food)
            del food[:]
        else:
            #insert new coord
            coords.insert(0,next_coord)
            #delete the last (tail)
            coords.pop()
        
        makeFood(coords)
        #fill the background
        setDisplay.fill(bg)
        #redraw the cell(s)
        drawCell(coords)
        #make borders on map
        borders()
        drawFood()
        pygame.display.update()
        fpsTime.tick(fps)

        
        
        

def check_collision(coords):
    if next_coord in coords:
        deadText()
    
        

def makeFood(coords):
    global food
    if not food:
        rand_x =randint(borderWidth/cellSize,(dispWidth-borderWidth)/cellSize) 
        rand_y =randint(borderWidth/cellSize,(dispHeight-borderWidth)/cellSize)
        new_food=[rand_x, rand_y]
        if new_food not in coords:
            food =[rand_x,rand_y]
        else:
            makeFood(coords)
        
def drawFood():
    global food
    print food
    #*cellSize to have same rastr as snake cells, +(cellSize/2) - to get to centre of every cell
    x=food[0]*cellSize+(cellSize/2)
    y=food[1]*cellSize+(cellSize/2)
    
    #surface, color, (x,y), radius
    pygame.draw.circle(setDisplay, black, (x, y), cellSize/2)
    #pygame.display.update()

def drawCell(coords):
    for coord in coords:
        x = coord[0]*cellSize
        y=coord[1]*cellSize
        makeCell = pygame.Rect(x,y,cellSize, cellSize)
        pygame.draw.rect(setDisplay, black, makeCell)
         

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
    direction_changed='no'
    global direction
    for event in pygame.event.get():
        #print event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT and direction != RIGHT and direction_changed=='no':
                direction = LEFT
                direction_changed='yes'
            elif event.key == K_RIGHT and direction != LEFT and direction_changed=='no':
                direction = RIGHT
                direction_changed='yes'
            elif event.key == K_DOWN and direction != UP and direction_changed=='no':
                direction = DOWN
                direction_changed='yes'
            elif event.key == K_UP and direction != DOWN and direction_changed=='no':
                direction = UP
                direction_changed='yes'
    
    

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
