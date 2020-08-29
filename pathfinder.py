import pygame
import pfai

pygame.init()

display_width=800
display_height=600
gamedisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Path Finder")
font1=pygame.font.SysFont(None, 80)
font2=pygame.font.SysFont(None,30)


(winx,winy)=(3,0)
gridx=4
gridy=3
glength=100
FPS=10
grey=(180,180,180)
white=(255,255,255)
black=(0,0,0)
#============================================================================================================================
penalty=10
reward=20
lpenalty=1
starting=30
maxscore=45
#============================================================================================================================

win=pygame.image.load('win.jpg')
fire=pygame.image.load('fire.jpg')
agent=pygame.image.load('agent.png')
win=pygame.transform.scale(win,(glength,glength))
fire=pygame.transform.scale(fire,(glength,glength))
#============================================================================================================================
class grid():
    def __init__(self,gridx,gridy):
        self.grid=[[['0'] for i in range(gridy)] for j in range(gridx)]

    def fill(self,a,x,y):
        if a=='wall':
            pygame.draw.rect(gamedisplay,black,[grid.grid[x][y][1][0],grid.grid[x][y][1][1],glength,glength])
            grid.grid[x][y][0]='wall'
        elif a=='win':
            gamedisplay.blit(win,grid.grid[x][y][1])
            grid.grid[x][y][0]='win'
        elif a=='fire':
            gamedisplay.blit(fire,grid.grid[x][y][1])
            grid.grid[x][y][0]='fire'
        elif a=='agent':
            gamedisplay.blit(agent,grid.grid[x][y][1])
#============================================================================================================================
def printmap():
    gamedisplay.fill(grey)
    printgrid(gridx,gridy)
    grid.fill('wall',1,1)
    grid.fill('win',winx,winy)
    grid.fill('fire',3,2)

#============================================================================================================================
def printgrid1(a,b):
    (x,y)=(100,100)
    m=a
    for b in range(b):
        x=100
        a=m
        for a in range(a):
            pygame.draw.rect(gamedisplay,black,[x,y,glength,glength],1)
            grid.grid[a][b].append((x,y))
            x+=glength
        y+=glength


def printgrid(a,b):
    (x,y)=(100,100)
    m=a
    while b>0:
        b-=1
        x=100
        a=m
        while a>0:
            a-=1
            pygame.draw.rect(gamedisplay,black,[x,y,glength,glength],1)
            x+=glength
        y+=glength

#============================================================================================================================
def message(msg,color,font,y_disp=0,x_disp=0):
    textSurf=font.render(msg,True,color)
    textRect=textSurf.get_rect()
    textRect.center=display_width/2+x_disp,display_height/2+y_disp
    gamedisplay.blit(textSurf,textRect)



clock=pygame.time.Clock()


(gpx,gpy)=(100,100)
gameon=True
grid=grid(gridx,gridy)
printgrid1(gridx,gridy)
while gameon:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameon=False
    x=1
    while True:

        for j in range(pfai.population):
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
            posx=0
            posy=2
            genmax=max(pfai.fitnes)
            pfai.fitnes[j]=starting
            for i in pfai.pop[j]:
                if i==1:#LEFT
                    if posx!=0:
                        if grid.grid[posx-1][posy][0]!='wall':
                            posx-=1
                elif i==2:#RIGHT
                    if posx!=gridx-1:
                        if grid.grid[posx+1][posy][0]!='wall':
                            posx+=1
                elif i==3:#UP
                    if posy!=0:
                        if grid.grid[posx][posy-1][0]!='wall':
                            posy-=1
                elif i==4:#DOWN
                    if posy!=gridy-1:
                        if grid.grid[posx][posy+1][0]!='wall':
                            posy+=1

                printmap()
                grid.fill('agent',posx,posy)
                #pygame.display.update()
#========================fitness stuff==================================================
                pfai.fitnes[j]-=lpenalty
                if grid.grid[posx][posy][0]=='fire':
                    pfai.fitnes[j]-=penalty
                    break
                elif grid.grid[posx][posy][0]=='win':
                    pfai.fitnes[j]+=reward
                    break
#=================================================================================
                #print(pfai.fitnes)
                message(f'score:{pfai.fitnes[j]}',black,font1,250)
                message(f'Generation:{x}',black,font1,-230)
                message(f'max of this gen:{genmax}',black,font2,290)
                pygame.display.update()
                #clock.tick(30)
            #print(genmax)
#======================PFAI==========================================================
        matpool=pfai.matingpool(pfai.fitnes)
        newpop=pfai.crossover(matpool,pfai.pop)
        pfai.mutate(newpop)
        pfai.stepincrease(5)
        #print(pfai.pop)
        pfai.pop=newpop
        x+=1
        if max(pfai.fitnes)>=maxscore:
            #print(pfai.pop[pfai.fitnes.index(max(pfai.fitnes))])
            break
        #gamedisplay.blit(agent,(posx,posy))
    #clock.tick(FPS)
    message(f'Generation:{x}',black,font1,-230)
    message(f'max of this gen:{genmax}',black,font2,290)
    pygame.quit()
    quit()
