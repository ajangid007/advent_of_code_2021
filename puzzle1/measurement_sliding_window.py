import os
import sys
import queue

def readInput(inputfile):
    with open(os.path.join(sys.path[0], inputfile), "r") as myfile:
        return [int(x) for x in myfile.read().split()]
    
def measureSlidingWindow(input):
    sums = sum(x < y for x, y in zip(input, input[3:]))
    print(sums)

if __name__ == '__main__':
    input = readInput("input.txt")
    times =  measureSlidingWindow(input)
    print(times)