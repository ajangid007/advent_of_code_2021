import os
import sys
import numpy

fishesdict = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}

def readInput(inputfile):
    global fishesdict
    lines = open (os.path.join(sys.path[0],inputfile), "r")
    for line in lines:
        fishes = [int(x) for x in line.split(",")]
    for fish in fishes:
        fishesdict[fish] += 1

def lanternFishCount(days):
    global fishesdict
    for day in range(days):
        zeros = fishesdict[0]
        fishesdict[0] = 0
        for index in range(1, len(fishesdict)):
            fishesdict[index-1] +=fishesdict[index]
            fishesdict[index] = 0
        fishesdict[6] += zeros
        fishesdict[8] += zeros

    fishcount = 0
    for fish in fishesdict:
        fishcount += fishesdict[fish]

    return fishcount


if __name__ == '__main__':
    #https://adventofcode.com/2021/day/6
    readInput("input.txt")
    days = 256
    count = lanternFishCount(days)
    print(count)