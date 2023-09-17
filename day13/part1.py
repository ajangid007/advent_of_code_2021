import os
import sys
import collections

#https://adventofcode.com/2021/day/13

maxx = maxy = 0
fold = []
points = []
lines =  open (os.path.join(sys.path[0],"input.txt"), "r")   
for line in lines:
    if line == "\n":
        continue
    if not "fold along"  in line:
        [y,x]=[int(x) for x in line.strip().split(",")]
        maxx = x if maxx < x else maxx
        maxy = y if maxy < y else maxy
        points.append((y,x))
    else:
        fold.append(line.strip().split(" ")[-1])


map = [["." for y in range(maxy+1)] for x in range(maxx+1)]
for (y,x) in points:
    map[x][y] = "#"


for inst in fold:
    X=len(map)
    Y=len(map[0])
    if "y=" in inst:
        x=int(inst.split("=")[-1])
        newmap = [[0 for i in range(Y)]for j in range(x)]
        for i in range(x):
            for j in range(len(map[0])):
                newmap[i][j] = "#"  if map[len(map)-1-i][j] =='#' or map[i][j] == "#" else "."
    else:
        y=int(inst.split("=")[-1])
        newmap = [[0 for i in range(y)]for j in range(X)]
        for i in range(len(map)):
            for j in range(y):
                newmap[i][j] = "#" if map[i][j] =='#' or map[i][Y-1-j] == "#" else "."
    map=newmap 
    count=0
    for x in range(len(map)):
        for y in range(len(map[0])):
            if map[x][y]=="#":
                count+=1
    print(count)
for x in range(len(map)):
    string = ""
    for y in range(len(map[0])):
        string += map[x][y] 
    print(string)


