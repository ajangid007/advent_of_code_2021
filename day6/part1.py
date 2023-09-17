import os
import sys
import numpy

def readInput(inputfile):
    originalFishCounter = []
    lines =  open (os.path.join(sys.path[0],inputfile), "r")    
    for line in lines:
        originalFishCounter.extend([int(x) for x in line.split(",")])
    return originalFishCounter

def lanternFishCount(fishes, days):
    for day in range(days):
        newFish = 0
        for i in range(len(fishes)):
            if fishes[i] > 0:
                fishes[i] -= 1
            else:
                fishes[i] = 6
                newFish += 1
        if newFish > 0:
            for i in range(newFish):
                fishes.append(8)
    return len(fishes)
    

if __name__ == '__main__':
    #https://adventofcode.com/2021/day/6
    input = readInput("input.txt")
    days = 80
    count = lanternFishCount(input, days)
    print(count)