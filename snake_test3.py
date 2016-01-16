
import pygame
import sys
from pygame.locals import *
from random import randint


class Snake():

    def __init__(self):

        pygame.init()
            
        self.white =(255,255,255)
        self.black = (0,0,0)
        self.red=(200,0,0)
        self.myColor = (50,129,167)
        self.borderColor = (147,183,114)
        self.borderWidth = 20
        self.bg=self.myColor

        self.score=0

        self.fps = 30
        self.dispWidth = 800
        self.dispHeight = 600
        self.cellSize = 10
        self.stepSize = 10

        self.UP = 'up'
        self.DOWN= 'down'
        self.RIGHT = 'right'
        self.LEFT = 'left'

        self.direction = self.RIGHT
        self.next_coord = []
        #self.coords = []
        self.food=[]
        
        self.fpsTime = pygame.time.Clock()
        self.setDisplay = pygame.display.set_mode((self.dispWidth,self.dispHeight))
        pygame.display.set_caption('snake')

    def runGame(self):
        startx = 3
        starty = 3
        #startxy=[startx,starty]
        #list of coords for every cell
        coords = [[startx, starty]]
        
        #default direction
        self.direction = self.RIGHT

        self.score=0
        
        while True:
            self.set_direction()
           
            #source of coord is left-top corner -> down +y, right +x
            if self.direction == self.UP:
                #-1 to y of first list in list of coords (first cell of snake)
                self.next_coord=[coords[0][0],coords[0][1]-1]
                
            elif self.direction == self.DOWN:
                self.next_coord=[coords[0][0],coords[0][1]+1]
                
            elif self.direction == self.LEFT:
                self.next_coord=[coords[0][0]-1,coords[0][1]]
                
            elif self.direction == self.RIGHT:
                self.next_coord=[coords[0][0]+1,coords[0][1]]
                

            #if we are out of borders
            if (self.next_coord[0] < self.borderWidth/self.cellSize - 1) or (self.next_coord[1] < self.borderWidth/self.cellSize - 1) or (self.next_coord[0] > ((self.dispWidth-self.borderWidth)/self.cellSize)) or (self.next_coord[1] >((self.dispHeight-self.borderWidth)/self.cellSize)):
                self.deadText()

            self.check_collision(coords)  

            #if a food is eaten
            if len(self.food)!=0 and self.next_coord[0]== self.food[0] and self.next_coord[1]==self.food[1]:
                new_coord_food= [self.food[0],self.food[1]]
                coords.insert(0,new_coord_food)
                del self.food[:]
                self.score +=1
            else:
                #insert new coord
                coords.insert(0,self.next_coord)
                #delete the last (tail)
                coords.pop()
            
            self.makeFood(coords)
            #fill the background
            self.setDisplay.fill(self.bg)
            #redraw the cell(s)
            self.drawCell(coords)
            #make borders on map
            self.borders()
            self.drawFood()
            pygame.display.update()
            self.fpsTime.tick(self.fps)

    
    def check_collision(self,coords):
        if self.next_coord in coords:
            self.deadText()
    
    def makeFood(self,coords):
        
        if not self.food:
            rand_x =randint(self.borderWidth/self.cellSize,(self.dispWidth-self.borderWidth)/self.cellSize) 
            rand_y =randint(self.borderWidth/self.cellSize,(self.dispHeight-self.borderWidth)/self.cellSize)
            new_food=[rand_x, rand_y]
            if new_food not in coords:
                self.food =[rand_x,rand_y]
            else:
                self.makeFood(coords)
        
    def drawFood(self):
        
        #*cellSize to have same rastr as snake cells, +(cellSize/2) - to get to centre of every cell
        x=self.food[0]*self.cellSize+(self.cellSize/2)
        y=self.food[1]*self.cellSize+(self.cellSize/2)
        
        #surface, color, (x,y), radius
        pygame.draw.circle(self.setDisplay, self.black, (x, y), self.cellSize/2)
        #pygame.display.update()

    def drawCell(self,coords):
        for coord in coords:
            x=coord[0]*self.cellSize
            y=coord[1]*self.cellSize
            makeCell = pygame.Rect(x,y,self.cellSize, self.cellSize)
            pygame.draw.rect(self.setDisplay, self.black, makeCell)
         

    def deadText(self):
        x=300
        y=350
        length=200
        height=50

        #fonts
        font = pygame.font.SysFont("monospace", 120)
        font_small=pygame.font.SysFont("monospace",30)
        font_score = pygame.font.SysFont("monospace", 80)
        
        #rendering
        label=font.render("You Died!", 1,self.black)
        label_small=font_small.render("Press any key to continue", 1, self.red)
        score_text = "SCORE: "+str(self.score)
        label_score=font_score.render(score_text, 1,self.black)
        
        #show the text
        self.setDisplay.blit(label, (100,200))
        self.setDisplay.blit(label_small, (200,350))
        self.setDisplay.blit(label_score, (250,400))
        
        #pygame.draw.rect(setDisplay, black, (x,y,length,height))
        pygame.display.update()
        pygame.time.wait(1000)
        while True:
            for event in pygame.event.get():
                #print event
                if event.type == MOUSEBUTTONDOWN:
                    print "click"
                    self.mouseClickRepeat(pygame.mouse.get_pos(),x, y, length, height)
                if event.type == KEYDOWN:
                    self.runGame()
                    
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
    
    def mouseClickRepeat(self,mouse, x, y, length, height):
        if mouse[0] >x and mouse[0] < (x+length) and mouse[1]>y and mouse[1]< (y+height):
            self.runGame()
        
    def set_direction(self):
        direction_changed='no'
        
        for event in pygame.event.get():
            #print event
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT and self.direction != self.RIGHT and direction_changed=='no':
                    self.direction = self.LEFT
                    direction_changed='yes'
                elif event.key == K_RIGHT and self.direction != self.LEFT and direction_changed=='no':
                    self.direction = self.RIGHT
                    direction_changed='yes'
                elif event.key == K_DOWN and self.direction != self.UP and direction_changed=='no':
                    self.direction = self.DOWN
                    direction_changed='yes'
                elif event.key == K_UP and self.direction != self.DOWN and direction_changed=='no':
                    self.direction = self.UP
                    direction_changed='yes'
        
    def borders(self):
        pygame.draw.line(self.setDisplay, self.borderColor,(0,0),(0,600),self.borderWidth)
        pygame.draw.line(self.setDisplay, self.borderColor,(0,0),(800,0),self.borderWidth)
        pygame.draw.line(self.setDisplay, self.borderColor,(0,600),(800,600),self.borderWidth)
        pygame.draw.line(self.setDisplay, self.borderColor,(800,600),(800,0),self.borderWidth)
        
#MAIN
while True:
    #fpsTime
    #setDisplay
    #pygame.init()
    
    #fpsTime = pygame.time.Clock()
    #setDisplay = pygame.display.set_mode((dispWidth,dispHeight))
    #pygame.display.set_caption('snake')

    snake = Snake()
    snake.runGame()
