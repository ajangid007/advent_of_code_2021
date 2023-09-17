import copy
import sys
import os

def readInput(inputfile):
    with open(os.path.join(sys.path[0], inputfile), "r") as myfile:
        return [str(x) for x in myfile.read().split()]
    
def calculateOxygen(data):
    total = len(data)
    data1 = []
    data0 = []
    place = count = 0
    while place < len(data[0]) and len(data) > 1:
        while count < len(data):
            if data[count][place] =='1':
                data1.append(data[count])
            else:
                data0.append(data[count])
            count += 1
        place += 1
        count = 0
        if len(data1) > len(data0):
            data = copy.deepcopy(data1)
        else:
            data = copy.deepcopy(data0)
        data1.clear()
        data0.clear()
    return int(data[0], 2)

def calculateCo2(data):
    total = len(data)
    data1 = []
    data0 = []
    place = count = 0
    while place < len(data[0]) and len(data) > 1:
        while count < len(data):
            if data[count][place] == '1':
                data1.append(data[count])
            else:
                data0.append(data[count])
            count += 1
        place += 1
        count = 0
        if len(data1) < len(data0):
            data = copy.deepcopy(data1)
        else:
            data = copy.deepcopy(data0)
        data1.clear()
        data0.clear()
    return int(data[0], 2)


    

if __name__ == '__main__':
    input = readInput("input.txt")
    oxygen =  calculateOxygen(input)
    co2 =  calculateCo2(input)
    print(oxygen, co2)
    print(co2 * oxygen)