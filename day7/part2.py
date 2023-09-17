import os
import sys
import numpy
from math import ceil


def readInput(inputfile):
    lines =  open (os.path.join(sys.path[0],inputfile), "r")    
    for line in lines:
        hor_positions = [int(x) for x in line.split(",")]
   
    return hor_positions

def findMinCost(positions):
    fuel = [0] * len(positions)
    full_range = range(min(positions), max(positions))
    fuel = min([sum([cost(abs(item - k)) for item in positions]) for k in full_range])
    return fuel

def cost(number):
    return int(number*(number+1)/2)

if __name__ == '__main__':
    #https://adventofcode.com/2021/day/7
    data = readInput("input.txt")
    cost = findMinCost(data)
    print(cost)