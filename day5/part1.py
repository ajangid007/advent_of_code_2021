import os
import sys
import numpy

maxX = 0
maxY = 0

def readInput(inputfile):
    global maxX, maxY
    coordinatePairs = []
    lines = open (os.path.join(sys.path[0],inputfile), "r")
    for line in lines:
        coordinatetuple = []
        for pairs in line.strip().split("->"):
            coordinatetuple.append(tuple([int(x) for x in pairs.strip().split(",")]))
        coordinatePairs.append(coordinatetuple)
    for item in coordinatePairs:
        for mytuple in item:
            if mytuple[0] > maxX:
                maxX = mytuple[0]
            if mytuple[1] > maxY:
                maxY = mytuple[1] 

    return coordinatePairs

def findOverlappingPoint(input):
    global maxX, maxY
    board = numpy.zeros((maxX+1,maxY+1))
    for (start, end) in input:
        xcoordinate = ycoordinate = []
        if start[0] == end[0]:
            xcoordinate.append(start[0])
            ycoordinate = list(range(start[1],end[1]+1,1)) if end[1]>start[1] else list(range(end[1],start[1]+1,1))
        elif start[1] == end[1]:
            ycoordinate.append(start[1])
            xcoordinate = list(range(start[0],end[0]+1,1)) if end[0]>start[0] else list(range(end[0],start[0]+1,1))
        elif abs(start[0] - end[0]) == abs(start[1] - end[1]):
            xcoordinate = list(range(start[0],end[0]+1,1)) if end[0]>start[0] else list(range(start[0],end[0]-1,-1))
            ycoordinate = list(range(start[1],end[1]+1,1)) if end[1]>start[1] else list(range(start[1],end[1]-1,-1))
        if len(xcoordinate) and len(ycoordinate):
            board = updateBoard(xcoordinate, ycoordinate, board)
    return board

def updateBoard(x,y,board):
    if len(x) == 1 or len(y) == 1:
        for i in y:
            for j in x:
                board[i][j] += 1
    if len(x) != 1 and len(y) != 1:
        for i in range(len(x)):
            board[y[i]][x[i]] += 1
    return board

def Min2OverlappingPoints(board):
    count = 0
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] >=2:
                count += 1
    return count


if __name__ == '__main__':
    #https://adventofcode.com/2021/day/5
    input = readInput("input.txt")
    board = findOverlappingPoint(input)
    print(Min2OverlappingPoints(board))
