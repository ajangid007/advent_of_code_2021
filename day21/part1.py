import os
import sys
import numpy
from math import ceil

class Player:
    def __init__(self, initialposition):
        self.position = initialposition
        self.sum = 0
    
    def update(self, move):
        self.position += move
        self.position = (self.position -1 ) % 10 + 1
        self.sum = self.sum + self.position

class Die():

    def __init__(self, p1, p2) -> None:
        self.player1 = Player(p1)
        self.player2 = Player(p2)
        self.rolledcount = 0
        self.lastrolledvalue = 0

    def findWiningPlayer(self):
        while not (self.player1.sum >= 1000 or self.player2.sum >= 1000):
            self.player1.update(self.rollDice())
            if self.player1.sum >=1000:
                return self.player2.sum * self.rolledcount
            self.player2.update(self.rollDice())
            if self.player2.sum >= 1000:
                return self.player1.sum * self.rolledcount

    def rollDice(self):
        self.rolledcount += 3
        rolledValue = 0
        for i in range(1,4):  
            self.lastrolledvalue += 1     
            rolledValue +=  (self.lastrolledvalue -1) % 100 + 1
        return rolledValue

        
def readInput(inputfile):
    with open(os.path.join(sys.path[0], inputfile), "r") as myfile:
        data = [int((x.split(":"))[1]) for x in myfile]
        return tuple(data)
    
if __name__== '__main__':
    (p1, p2) = readInput('input.txt')
    die = Die(p1, p2)
    value = die.findWiningPlayer()
    print(value)

