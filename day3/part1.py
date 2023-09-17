import sys
import os

def readInput(inputfile):
    with open(os.path.join(sys.path[0], inputfile), "r") as myfile:
        return [str(x) for x in myfile.read().split()]

def powerConsumption(data):
    total = len(data)
    digits = [0,0,0,0,0,0,0,0,0,0,0,0]
    for reading in data:
        count = 0
        for char in str(reading):
            if char == '1':
                digits[count] += 1
            count += 1
    gammarate = epsilonrate = '0b'
    for digit in digits:
        if digit > total/2:
            gammarate += '1'
            epsilonrate += '0'
        else:
            gammarate += '0'
            epsilonrate += '1'
    return(int(gammarate, 2), int(epsilonrate, 2))


if __name__ == '__main__':
    #https://adventofcode.com/2021/day/3
    input = readInput("input.txt")
    (gamma, epsilon) =  powerConsumption(input)
    print(gamma, epsilon)
    print(gamma * epsilon)