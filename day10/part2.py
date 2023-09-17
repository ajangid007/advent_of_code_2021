import os
import sys
from collections import deque

#https://adventofcode.com/2021/day/10

data = []
lines =  open (os.path.join(sys.path[0],"input.txt"), "r")   
for line in lines:
    data.append(line.strip())

completionPoints = {
    '{':3,
    '[':2,
    '(':1,
    '<':4
}

closingMap = {
    '}':'{',
    ']':'[',
    ')':'(',
    '>':'<'
}
score = []
for line in data:
    sum = 0
    Q = deque()
    foundIncomplete = True
    for c in line:
        if c in [')', ']','}','>']:
            if len(Q)>0:
                lastChar = Q.pop()
                if lastChar == closingMap[c]:
                    continue
                else:
                    foundIncomplete = False
                    break
            else:
                foundIncomplete = False
                break
        else:
            Q.append(c)
    if foundIncomplete:
        while Q:
            sum = sum*5 + completionPoints[Q.pop()]
        score.append(sum)
score = sorted(score)
print(score)
print(score[int(len(score)/2)])