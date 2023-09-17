import os
import sys
import numpy


def readInput(inputfile):
    lines =  open (os.path.join(sys.path[0],inputfile), "r")    
    for line in lines:
        hor_positions = [int(x) for x in line.split(",")]
   
    return hor_positions

def findIndex(positions):
    fuel = [0] * len(positions)
    k = 0
    while k < len(positions):
        forward = backward = 0
        forward = sum([abs(positions[i] -positions[k]) for i in range(0,k)])
        backward = sum([abs(positions[j+1] - positions[k]) for j in range(k, len(positions)-1)])
        fuel[k] = forward + backward
        k += 1
    return min(fuel)

if __name__ == '__main__':
    #https://adventofcode.com/2021/day/7
    data = readInput("input.txt")
    index = findIndex(data)
    print(index)