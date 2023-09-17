import os
import sys


def readInput(inputfile):
    lines =  open (os.path.join(sys.path[0],inputfile), "r")  
    return [line.strip() for line in lines.readlines()]

class Digits:
    def __init__(self,data):
        self.signals = data
        self.unique_digits = {
            1: 2,
            4: 4,
            7: 3,
            8: 7
        }
   
    def count(self,digit):
        count = 0
        for row in self.signals:
            input, output  = row.split("|")
            inputs = input.strip().split(" ")
            outputs = output.strip().split(" ")
            for item in outputs:
                if len(item) == self.unique_digits[digit]:
                    count += 1
        return count



if __name__ == '__main__':
    #https://adventofcode.com/2021/day/8
    data = readInput('input.txt')
    digits = Digits(data)
    print("1: "+ str(digits.count(1)) + ", 4: " + str(digits.count(4)) + ", 7: " + str(digits.count(7)) + ", 8: " + str(digits.count(8)))
    print(digits.count(1)+digits.count(4)+digits.count(7)+digits.count(8))



