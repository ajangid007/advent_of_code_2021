import os
import sys
from collections import deque

##https://adventofcode.com/2021/day/10
data = []
lines =  open (os.path.join(sys.path[0],"input.txt"), "r")   
for line in lines:
    data.append(line.strip())

corruptcount = {
    '}':0,
    ']':0,
    ')':0,
    '>':0
}

closingMap = {
    '}':'{',
    ']':'[',
    ')':'(',
    '>':'<'
}
for line in data:
    Q = deque()
    for c in line:
        if c in [')', ']','}','>']:
            if len(Q)>0:
                lastChar = Q.pop()
                if lastChar == closingMap[c]:
                    continue
                else:
                    corruptcount[c] +=1
                    break
            else:
                break
        else:
            Q.append(c)
print(corruptcount)
print(corruptcount[')']*3+corruptcount[']']*57+corruptcount['}']*1197+corruptcount['>']*25137)