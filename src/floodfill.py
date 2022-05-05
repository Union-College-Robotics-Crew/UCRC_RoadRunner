import config
from src.robot import Robot
from src.encoder import Encoder
import rotaryio

class FloodFill():

    def __init__(self):
        encL = rotaryio.IncrementalEncoder(config.l_encA, config.l_encB)
        encR = rotaryio.IncrementalEncoder(config.r_encA, config.r_encB)
        self.robot = Robot(encL, encR)

        self.orient=0
        self.cell = 0

        self.cells = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

        self.flood=[[14,13,12,11,10,9,8,7,7,8,9,10,11,12,13,14],
                [13,12,11,10,9,8,7,6,6,7,8,9,10,11,12,13],
                [12,11,10,9,8,7,6,5,5,6,7,8,9,10,11,12],
                [11,10,9,8,7,6,5,4,4,5,6,7,8,9,10,11],
                [10,9,8,7,6,5,4,3,3,4,5,6,7,8,9,10],
                [9,8,7,6,5,4,3,2,2,3,4,5,6,7,8,9],
                [8,7,6,5,4,3,2,1,1,2,3,4,5,6,7,8],
                [7,6,5,4,3,2,1,0,0,1,2,3,4,5,6,7],
                [7,6,5,4,3,2,1,0,0,1,2,3,4,5,6,7],
                [8,7,6,5,4,3,2,1,1,2,3,4,5,6,7,8],
                [9,8,7,6,5,4,3,2,2,3,4,5,6,7,8,9],
                [10,9,8,7,6,5,4,3,3,4,5,6,7,8,9,10],
                [11,10,9,8,7,6,5,4,4,5,6,7,8,9,10,11],
                [12,11,10,9,8,7,6,5,5,6,7,8,9,10,11,12],
                [13,12,11,10,9,8,7,6,6,7,8,9,10,11,12,13],
                [14,13,12,11,10,9,8,7,7,8,9,10,11,12,13,14]]

        self.flood2= [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

        self.queue=[]

    def orientation(self,orient,turning):
        if (turning== 'L'):
            orient-=1
            if (orient==-1):
                orient=3
        elif(turning== 'R'):
            orient+=1
            if (orient==4):
                orient=0
        elif(turning== 'B'):
            if (orient==0):
                orient=2
            elif (orient==1):
                orient=3
            elif (orient==2):
                orient=0
            elif (orient==3):
                orient=1

        return(orient)

    def updateCoordinates(self,x,y,orient):
        if (orient==0):
            y+=1
        if (orient==1):
            x+=1
        if (orient==2):
            y-=1
        if (orient==3):
            x-=1

        return(x,y)

    def updateWalls(self,x,y,orient,L,R,F):
        if(L and R and F):
            if (orient==0): 
                self.cells[y][x]= 13
            elif (orient==1): 
                self.cells[y][x]= 12
            elif (orient==2): 
                self.cells[y][x]= 11
            elif (orient==3): 
                self.cells[y][x]= 14

        elif (L and R and not F):
            if (orient==0 or orient== 2): 
                self.cells[y][x]= 9
            elif (orient==1 or orient==3): 
                self.cells[y][x]= 10

        elif (L and F and not R):
            if (orient==0): 
                self.cells[y][x]= 8
            elif (orient==1): 
                self.cells[y][x]= 7
            elif (orient==2): 
                self.cells[y][x]= 6
            elif (orient==3): 
                self.cells[y][x]= 5

        elif (R and F and not L):
            if (orient==0): 
                self.cells[y][x]= 7
            elif (orient==1): 
                self.cells[y][x]= 6
            elif (orient==2): 
                self.cells[y][x]= 5
            elif (orient==3): 
                self.cells[y][x]= 8

        elif(F):
            if (orient==0): 
                self.cells[y][x]= 2
            elif (orient==1): 
                self.cells[y][x]= 3
            elif (orient==2): 
                self.cells[y][x]= 4
            elif (orient==3): 
                self.cells[y][x]= 1

        elif(L):
            if (orient==0): 
                self.cells[y][x]= 1
            elif (orient==1): 
                self.cells[y][x]= 2
            elif (orient==2): 
                self.cells[y][x]= 3
            elif (orient==3): 
                self.cells[y][x]= 4

        elif(R):
            if (orient==0): 
                self.cells[y][x]= 3
            elif (orient==1): 
                self.cells[y][x]= 4
            elif (orient==2): 
                self.cells[y][x]= 1
            elif (orient==3): 
                self.cells[y][x]= 2

        else:
            self.cells[y][x]= 15

    def isAccessible(self,x,y,x1,y1):
        '''
        returns True if mouse can move to x1,y1 from x,y (two adjescent cells)
        '''

        if (x==x1):
            if(y>y1):
                if(self.cells[y][x]==4 or self.cells[y][x]==5 or self.cells[y][x]==6 or self.cells[y][x]==10 or self.cells[y][x]==11 or self.cells[y][x]==12 or self.cells[y][x]==14 or self.cells[y1][x1]==2 or self.cells[y1][x1]==7 or self.cells[y1][x1]==8 or self.cells[y1][x1]==10 or self.cells[y1][x1]==12 or self.cells[y1][x1]==13 or self.cells[y1][x1]==14 ):
                    return (False)
                else:
                    return(True)
            else:
                if(self.cells[y][x]==2 or self.cells[y][x]==7 or self.cells[y][x]==8 or self.cells[y][x]==10 or self.cells[y][x]==12 or self.cells[y][x]==13 or self.cells[y][x]==14 or self.cells[y1][x1]==4 or self.cells[y1][x1]==5 or self.cells[y1][x1]==6 or self.cells[y1][x1]==10 or self.cells[y1][x1]==11 or self.cells[y1][x1]==12 or self.cells[y1][x1]==14 ):
                    return (False)
                else:
                    return(True)
                

        elif (y==y1):
            if(x>x1):
                if(self.cells[y][x]==1 or self.cells[y][x]==5 or self.cells[y][x]==8 or self.cells[y][x]==9 or self.cells[y][x]==11 or self.cells[y][x]==13 or self.cells[y][x]==14 or self.cells[y1][x1]==3 or self.cells[y1][x1]==6 or self.cells[y1][x1]==7 or self.cells[y1][x1]==9 or self.cells[y1][x1]==11 or self.cells[y1][x1]==12 or self.cells[y1][x1]==13 ):
                    return (False)
                else:
                    return (True)
            else:
                if(self.cells[y][x]==3 or self.cells[y][x]==6 or self.cells[y][x]==7 or self.cells[y][x]==9 or self.cells[y][x]==11 or self.cells[y][x]==12 or self.cells[y][x]==13 or self.cells[y1][x1]==1 or self.cells[y1][x1]==5 or self.cells[y1][x1]==8 or self.cells[y1][x1]==9 or self.cells[y1][x1]==11 or self.cells[y1][x1]==13 or self.cells[y1][x1]==14 ):
                    return (False)
                else:
                    return (True)

    def getSurrounds(self,x,y):
        ''' 
        returns x1,y1,x2,y2,x3,y3,x4,y4 the four surrounding square
        '''
        x3= x-1
        y3=y
        x0=x
        y0=y+1
        x1=x+1
        y1=y
        x2=x
        y2=y-1
        if(x1>=16):
            x1=-1
        if(y0>=16):
            y0=-1
        return (x0,y0,x1,y1,x2,y2,x3,y3)  #order of cells- north,east,south,west

    def changeDestination(self,maze,destinationx, destinationy):
        for j in range(16):
            for i in range(16):
                self.flood[i][j]=255

        queue=[]
        maze[destinationy][destinationx]=0

        queue.append(destinationy)
        queue.append(destinationx)

        
        while (len(queue)!=0):
            yrun=queue.pop(0)
            xrun=queue.pop(0)

            x0,y0,x1,y1,x2,y2,x3,y3= self.getSurrounds(xrun,yrun)
            if(x0>=0 and y0>=0 ):
                if (maze[y0][x0]==255):
                    maze[y0][x0]=maze[yrun][xrun]+1
                    queue.append(y0)
                    queue.append(x0)
            if(x1>=0 and y1>=0 ):
                if (maze[y1][x1]==255):
                    maze[y1][x1]=maze[yrun][xrun]+1
                    queue.append(y1)
                    queue.append(x1)
            if(x2>=0 and y2>=0 ):
                if (maze[y2][x2]==255):
                    maze[y2][x2]=maze[yrun][xrun]+1
                    queue.append(y2)
                    queue.append(x2)
            if(x3>=0 and y3>=0 ):
                if (maze[y3][x3]==255):
                    maze[y3][x3]=maze[yrun][xrun]+1
                    queue.append(y3)
                    queue.append(x3)

    def floodFill2(self,maze):
        for i in range(16):
            for j in range(16):
                maze[i][j]=0

        queue=[]
        self.flood2[7][7]=1
        self.flood2[8][7]=1
        self.flood2[7][8]=1
        self.flood2[8][8]=1

        queue.append(7)
        queue.append(7)
        queue.append(8)
        queue.append(7)
        queue.append(7)
        queue.append(8)
        queue.append(8)
        queue.append(8)

        
        while (len(queue)!=0):
            yrun=queue.pop(0)
            xrun=queue.pop(0)

            x0,y0,x1,y1,x2,y2,x3,y3= self.getSurrounds(xrun,yrun)
            if(x0>=0 and y0>=0 and self.cells[y0][x0]!=0):
                if (maze[y0][x0]==0):
                    if (self.isAccessible(xrun,yrun,x0,y0)):
                        maze[y0][x0]=maze[yrun][xrun]+1
                        queue.append(y0)
                        queue.append(x0)
            if(x1>=0 and y1>=0 and self.cells[y1][x1]!=0):
                if (maze[y1][x1]==0):
                    if (self.isAccessible(xrun,yrun,x1,y1)):
                        maze[y1][x1]=maze[yrun][xrun]+1
                        queue.append(y1)
                        queue.append(x1)
            if(x2>=0 and y2>=0 and self.cells[y2][x2]!=0):
                if (maze[y2][x2]==0):
                    if (self.isAccessible(xrun,yrun,x2,y2)):
                        maze[y2][x2]=maze[yrun][xrun]+1
                        queue.append(y2)
                        queue.append(x2)
            if(x3>=0 and y3>=0 and self.cells[y3][x3]!=0):
                if (maze[y3][x3]==0):
                    if (self.isAccessible(xrun,yrun,x3,y3)):
                        maze[y3][x3]=maze[yrun][xrun]+1
                        queue.append(y3)
                        queue.append(x3)

    def floodFill3(self,maze,queue):

        while (len(queue)!=0):
            yrun=queue.pop(0)
            xrun=queue.pop(0)

            x0,y0,x1,y1,x2,y2,x3,y3= self.getSurrounds(xrun,yrun)
            if(x0>=0 and y0>=0 ):
                if (maze[y0][x0]==255):
                    if (self.isAccessible(xrun,yrun,x0,y0)):
                        maze[y0][x0]=maze[yrun][xrun]+1
                        queue.append(y0)
                        queue.append(x0)
            if(x1>=0 and y1>=0):
                if (maze[y1][x1]==255):
                    if (self.isAccessible(xrun,yrun,x1,y1)):
                        maze[y1][x1]=maze[yrun][xrun]+1
                        queue.append(y1)
                        queue.append(x1)
            if(x2>=0 and y2>=0 ):
                if (maze[y2][x2]==255):
                    if (self.isAccessible(xrun,yrun,x2,y2)):
                        maze[y2][x2]=maze[yrun][xrun]+1
                        queue.append(y2)
                        queue.append(x2)
            if(x3>=0 and y3>=0 ):
                if (maze[y3][x3]==255):
                    if (self.isAccessible(xrun,yrun,x3,y3)):
                        maze[y3][x3]=maze[yrun][xrun]+1
                        queue.append(y3)
                        queue.append(x3)

    def toMove(self,maze,x,y,xprev,yprev,orient):
        '''
        returns the direction to turn into L,F,R or B
        '''
        x0,y0,x1,y1,x2,y2,x3,y3 = self.getSurrounds(x,y)
        val= maze[y][x]
        prev=0
        minVals=[1000,1000,1000,1000]

        if (self.isAccessible(x,y,x0,y0)):
            if (x0==xprev and y0==yprev):
                prev=0
            minVals[0]= maze[y0][x0]

        if (self.isAccessible(x,y,x1,y1)):
            if (x1==xprev and y1==yprev):
                prev=1
            minVals[1]= maze[y1][x1]

        if (self.isAccessible(x,y,x2,y2)):
            if (x2==xprev and y2==yprev):
                prev=2
            minVals[2]= maze[y2][x2]

        if (self.isAccessible(x,y,x3,y3)):
            if (x3==xprev and y3==yprev):
                prev=3
            minVals[3]= maze[y3][x3]

        minVal=minVals[0]
        minCell=0
        noMovements=0
        for i in minVals:
            if (i!=1000):
                noMovements+=1

        for i in range(4):
            if (minVals[i]<minVal):
                if (noMovements==1):
                    minVal= minVals[i]
                    minCell= i
                else:
                    if(i==prev):
                        pass
                    else:
                        minVal= minVals[i]
                        minCell= i

        if (minCell==orient):
            return ('F')
        elif((minCell==orient-1) or (minCell== orient+3)):
            return('L')
        elif ((minCell==orient+1) or (minCell== orient-3)):
            return('R')
        else:
            return('B')

    def toMove2(self,maze,x,y,xprev,yprev,orient):
        '''
        returns the direction to turn into L,F,R or B
        '''
        x0,y0,x1,y1,x2,y2,x3,y3 = self.getSurrounds(x,y)
        val= maze[y][x]
        minCell=0
        if (self.isAccessible(x,y,x0,y0)):
            if (maze[y0][x0]==val-1):
                minCell=0

        if (self.isAccessible(x,y,x1,y1)):
            if (maze[y1][x1]==val-1):
                minCell=1

        if (self.isAccessible(x,y,x2,y2)):
            if (maze[y2][x2]==val-1):
                minCell=2

        if (self.isAccessible(x,y,x3,y3)):
            if (maze[y3][x3]==val-1):
                minCell=3


        if (minCell==orient):
            return ('F')
        elif((minCell==orient-1) or (minCell== orient+3)):
            return('L')
        elif ((minCell==orient+1) or (minCell== orient-3)):
            return('R')
        else:
            return('B')

    def center(self,x,y,orient):
        L= self.robot.wallLeft()
        R= self.robot.wallRight()
        F= self.robot.wallFront()

        if (L):
            self.updateWalls(x,y,orient,L,R,F)
            
            self.robot.forward()
            xprev=x
            yprev=y
            x,y = self.updateCoordinates(x,y,orient)

            L= self.robot.wallLeft()
            R= self.robot.wallRight()
            F= self.robot.wallFront()
            self.updateWalls(x,y,orient,L,R,F)

            self.robot.turnRight()
            orient = self.orientation(orient,'R')

            self.robot.forward()
            xprev=x
            yprev=y
            x,y = self.updateCoordinates(x,y,orient)
            
            L= self.robot.wallLeft()
            R= self.robot.wallRight()
            F= self.robot.wallFront()
            self.updateWalls(x,y,orient,L,R,F)

            self.robot.turnRight()
            orient = self.orientation(orient,'R')

            self.robot.forward()
            xprev=x
            yprev=y
            x,y = self.updateCoordinates(x,y,orient)

            L= self.robot.wallLeft()
            R= self.robot.wallRight()
            F= self.robot.wallFront()
            self.updateWalls(x,y,orient,L,R,F)

            self.robot.turnRight()
            orient = self.orientation(orient,'R')

            self.robot.forward()
            xprev=x
            yprev=y
            x,y = self.updateCoordinates(x,y,orient)

            L= self.robot.wallLeft()
            R= self.robot.wallRight()
            F= self.robot.wallFront()
            self.updateWalls(x,y,orient,L,R,F)
            
            return (x,y,xprev,yprev,orient)

        else:
            self.updateWalls(x,y,orient,L,R,F)

            self.robot.forward()
            xprev=x
            yprev=y
            x,y = self.updateCoordinates(x,y,orient)

            L= self.robot.wallLeft()
            R= self.robot.wallRight()
            F= self.robot.wallFront()
            self.updateWalls(x,y,orient,L,R,F)

            self.robot.turnLeft()
            orient = self.orientation(orient,'L')

            self.robot.forward()
            xprev=x
            yprev=y
            x,y = self.updateCoordinates(x,y,orient)
            
            L= self.robot.wallLeft()
            R= self.robot.wallRight()
            F= self.robot.wallFront()
            self.updateWalls(x,y,orient,L,R,F)

            self.robot.turnLeft()
            orient = self.orientation(orient,'L')

            self.robot.forward()
            xprev=x
            yprev=y
            x,y = self.updateCoordinates(x,y,orient)

            L= self.robot.wallLeft()
            R= self.robot.wallRight()
            F= self.robot.wallFront()
            self.updateWalls(x,y,orient,L,R,F)

            self.robot.turnLeft()
            orient = self.orientation(orient,'L')

            self.robot.forward()
            xprev=x
            yprev=y
            x,y = self.updateCoordinates(x,y,orient)

            L= self.robot.wallLeft()
            R= self.robot.wallRight()
            F= self.robot.wallFront()
            self.updateWalls(x,y,orient,L,R,F)

            return (x,y,xprev,yprev,orient)

    def appendZero(self):

        for i in range(16):
            for j in range(16):
                self.flood[i][j]=255

        self.flood[7][7]=0
        self.flood[8][7]=0
        self.flood[7][8]=0
        self.flood[8][8]=0

        self.queue.append(7)
        self.queue.append(7)
        self.queue.append(8)
        self.queue.append(7)
        self.queue.append(7)
        self.queue.append(8)
        self.queue.append(8)
        self.queue.append(8)


    def appendDestination(self,x,y):

        for i in range(16):
            for j in range(16):
                self.flood[i][j]=255

        self.flood[y][x]=0

        self.queue.append(y)
        self.queue.append(x)

    def main(self):
        x=0
        y=0
        xprev=0
        yprev=0
        orient=0
        state=0
        short= False

        while True:
            L= self.robot.wallLeft()
            R= self.robot.wallRight()
            F= self.robot.wallFront()
            self.updateWalls(x,y,orient,L,R,F)

            if (self.flood[y][x]!=0):
                
                if (state==0):
                    self.appendZero()
                elif(state==1):
                    self.appendDestination(15,0)
                    short=False
                elif(state==2):
                    self.appendDestination(0,0)
                    short=False
                elif(state==3):
                    self.appendZero()
                    self.floodFill2(self.flood2)
                    short=True
                elif(state==4):
                    self.appendDestination(0,15)
                    short=False
                elif(state==5):
                    self.appendDestination(0,0)
                    short=False
                elif(state==6):
                    self.appendZero()
                    self.floodFill2(self.flood2)
                    short=True

                self.floodFill3(self.flood,self.queue)

            else:
                if state==5:
                    self.appendZero()
                    self.floodFill3(self.flood,self.queue)
                    state+=1
                elif state==4:
                    self.changeDestination(self.flood,0,0)
                    state+=1
                elif state==3:
                    self.changeDestination(self.flood,0,15)
                    state+=1
                elif state==2:
                    self.appendZero()
                    self.floodFill3(self.flood,self.queue)
                    state+=1
                elif state==1:
                    self.changeDestination(self.flood,0,0)
                    state+=1
                elif state==0:
                    x,y,xprev,yprev,orient= self.center(x,y,orient)
                    self.changeDestination(self.flood,15,0)
                    state+=1

                self.floodFill2(self.flood2)

                
            if short:
                direction= self.toMove2(self.flood2,x,y,xprev,yprev,orient)
            else:
                direction= self.toMove(self.flood,x,y,xprev,yprev,orient)
            
            if (direction=='L'):
                self.robot.turnLeft()
                orient = self.orientation(orient,'L')

            elif (direction=='R'):
                self.robot.turnRight()
                orient = self.orientation(orient,'R')

            elif (direction=='B'):
                self.robot.turnLeft()
                orient = self.orientation(orient,'L')
                self.robot.turnLeft()
                orient = self.orientation(orient,'L')


            self.robot.forward()
            xprev=x
            yprev=y
            x,y = self.updateCoordinates(x,y,orient)