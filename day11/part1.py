import os
import sys
from collections import deque

#https://adventofcode.com/2021/day/11

data = []
lines =  open (os.path.join(sys.path[0],"input.txt"), "r")   
for line in lines:
    data.append([int(x) for x in line.strip()])


R = len(data)
C = len(data[0])
DR = [-1, -1, -1, 0, 0, 1, 1, 1]
DC = [-1, 0, 1, -1, 1, -1, 0, 1]

size = 0
Q=deque()
count = 0
while True:
    FLASH = []
    for r in range(R):
        for c in range(C):
            data[r][c] += 1

    while True:       
        for r in range(R):
            for c in range(C):
                if data[r][c] > 9 and (r,c) not in FLASH:  
                    FLASH.append((r,c))          
                    for d in range(8):
                        rr = r+DR[d]
                        cc = c+ DC[d]
                        if 0<=rr<R and 0<=cc<C:
                            Q.append((rr,cc))
        if not len(Q):
            break
            
        while Q:
            (r,c) = Q.popleft()
            data[r][c] += 1

    for (r,c) in FLASH:
        data[r][c] = 0

    count += 1
    if len(FLASH) == R*C:
        break
    
    size += len(FLASH)
    
    

    #print("Step"+str(i))
    #print(data)
print(size)
print(count)

                    