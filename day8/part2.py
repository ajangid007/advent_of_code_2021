import os
import sys
import itertools


def readInput(inputfile):
    lines = open (os.path.join(sys.path[0],inputfile), "r")
    return [line.strip() for line in lines.readlines()]

class Digits:
    def __init__(self,data):
        self.signals = data
        self.digitkeys = [ 
            "abcefg",
            "cf",
            "acdeg",
            "acdfg",
            "bcdf",
            "abdfg",
            "abdefg",
            "acf",
            "abcdefg",
            "abcdfg"
        ]
        self.MappedDigits = {
            "abcefg": 0,
            "cf":1,
            "acdeg":2,
            "acdfg":3,
            "bcdf":4,
            "abdfg":5,
            "abdefg":6,
            "acf":7,
            "abcdefg":8,
            "abcdfg":9
        }

    def countAll(self):
        sum = 0 
        for line in self.signals:
            inputs, outputs = line.strip().split("|")
            for sigma in list(itertools.permutations('abcdefg')):
                key = {}
                for c in "abcdefg":
                    key[c] = sigma["abcdefg".index(c)]

                mappedinputs = []

                for input in inputs.strip().split(" "):
                    digit = ""
                    for x in input:
                        digit += key[x] 
                    mappedinputs.append("".join(sorted(digit)))

                if all(elem in self.digitkeys for elem in mappedinputs):
                    outputNumber = 0
                    for output in outputs.strip().split(" "):
                        number = ""
                        for c in output:
                            number += key[c]
                        outputNumber = outputNumber*10 + self.MappedDigits["".join(sorted(number))]
                    sum += outputNumber
                    break
                else:
                    continue 
        print(sum)



if __name__ == '__main__':
    #https://adventofcode.com/2021/day/8
    data = readInput('input.txt')
    digits = Digits(data)
    digits.countAll()
