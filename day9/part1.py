import os
import sys
import itertools
from collections import deque


def readInput(inputfile):
    dataarray = []
    lines = open (os.path.join(sys.path[0],inputfile), "r")
    for line in lines:
        dataarray.append([int(x) for x in line.strip()])
    return dataarray

class Digits:
    def __init__(self,data):
        self.array = data
        self.ROWS = len(data)
        self.COLUMNS = len(data[0])


    def findAdjacentDigits(self):
        adjacentDigits = []
        basin = []

        for row in range(0, self.ROWS):
            for column in range(0, self.COLUMNS):
                lowest = self.evaluateCost(row, column)
                if lowest:
                    adjacentDigits.append(self.array[row][column])
                    basin.append(self.evaluateBasin(row,column))
        return adjacentDigits, basin

    def evaluateCost(self,x,y):
        #topLeft  = self.array[ x - 1 ][ y - 1 ] if x>0 and y>0 else None
        top     = self.array[ x - 1 ][ y ] if x>0 else None 
        #topRight = self.array[ x - 1 ][ y + 1 ] if x>0 and y<self.COLUMNS-1 else None 

        midLeft = self.array[ x  ][ y - 1 ] if y>0 else None
        midRight = self.array[ x  ][ y + 1 ] if y<self.COLUMNS-1 else None 

        #botLeft  = self.array[ x + 1 ][ y - 1 ] if x<self.ROWS-1 and y>0 else None
        bot = self.array[ x + 1 ][ y  ] if x<self.ROWS-1 else None
        #botRight = self.array[ x + 1 ][ y + 1 ] if x<self.ROWS-1 and y<self.COLUMNS-1 else None

        elements = []
        #elements.append(topLeft) if topLeft != None else None
        elements.append(top) if top != None else None
        #elements.append(topRight) if topRight != None else None
        elements.append(midLeft) if midLeft != None else None
        elements.append(midRight) if midRight != None else None
        #elements.append(botLeft) if botLeft != None else None
        elements.append(bot) if bot != None else None
        #elements.append(botRight) if botRight != None else None

        return True if self.array[x][y] < min(elements) else False

    def evaluateBasin(self,x,y):
        alreadyVisited = []
        sum = 0
        alreadyVisited.append((x,y))

        sum += (self.recursiveBasin(x-1,y,self.array[x][y],sum,alreadyVisited) if x>0 else 0) + \
                    (self.recursiveBasin(x,y-1,self.array[x][y],sum,alreadyVisited) if y>0 else 0) + \
                    (self.recursiveBasin(x+1,y,self.array[x][y],sum,alreadyVisited) if x+1<len(self.array) else 0) + \
                    (self.recursiveBasin(x,y+1,self.array[x][y],sum,alreadyVisited) if y+1<len(self.array[0]) else 0)
        sum += len(alreadyVisited) 
        return sum

    def recursiveBasin(self,x,y,value,sum,alreadyVisited):
        sum = 0
        if (x,y) in alreadyVisited:
            return 0
        if self.array[x][y] == 9:
            #alreadyVisited.append((x,y))
            return 0
        if self.array[x][y] > value + 1 :
            return 0
        if self.array[x][y] == value + 1 :
            alreadyVisited.append((x,y))    
            sum += (self.recursiveBasin(x-1,y,self.array[x][y],sum,alreadyVisited) if x>0 else 0) + \
                    (self.recursiveBasin(x,y-1,self.array[x][y],sum,alreadyVisited) if y>0 else 0) + \
                    (self.recursiveBasin(x+1,y,self.array[x][y],sum,alreadyVisited) if x+1<len(self.array) else 0) + \
                    (self.recursiveBasin(x,y+1,self.array[x][y],sum,alreadyVisited) if y+1<len(self.array[0]) else 0)
        return sum +1

    def updatedBasin(self):
        R = len(self.array)
        C = len(self.array)
        DR = [-1,0,1,0]
        DC = [0,1,0,-1]
        ans = 0

        S=[]
        SEEN = set()
        for r in range(R):
            for c in range(C):
                if not (r,c) in SEEN and self.array[r][c] !=9:
                    size = 0
                    Q=deque()
                    Q.append((r,c))
                    while Q:
                        (r,c) = Q.popleft()
                        if (r,c) in SEEN:
                            continue
                        SEEN.add((r,c))
                        size +=1
                        for d in range(4):
                            rr = r+DR[d]
                            cc = c+ DC[d]
                            if 0<=rr<R and 0<=cc<C and self.array[rr][cc] != 9:
                                Q.append((rr,cc))
                    S.append(size)
        return sorted(S)


if __name__ == '__main__':
    #https://adventofcode.com/2021/day/9
    data = readInput('input.txt')
    #adjacentLowest, basin = Digits(data).findAdjacentDigits()
    #print(adjacentLowest)
    #print(sum(adjacentLowest) + 1*(len(adjacentLowest)))
    #print(basin)
    #basin = sorted(basin)
    #print(basin[-1]*basin[-2]*basin[-3])
    basin = Digits(data).updatedBasin()
    print (basin)
    print(basin[-1]*basin[-2]*basin[-3])