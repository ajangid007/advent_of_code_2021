import os
import sys

def readInput(inputfile):
    with open(os.path.join(sys.path[0], inputfile), "r") as myfile:
        return [int(x) for x in myfile.read().split()]
    
def measureSubsequentLargeValue(input):
    count =0
    max=0
    for value in input:
        if max != 0 and value > max:
            count +=1
        max = value
    return count
if __name__ == '__main__':
    input = readInput("input.txt")
    times =  measureSubsequentLargeValue(input)
    print(times)