
import sys
import os
import collections

#https://adventofcode.com/2021/day/12

"""
data = []
nodes = []
lines =  open (os.path.join(sys.path[0],"inputtest.txt"), "r")   
for line in lines:
    edge1,edge2 = line.strip().split("-")
    data.append((edge1,edge2))
    if edge1 not in nodes:
        nodes.append(edge1)
    if edge2 not in nodes:
        nodes.append(edge2)

allValidPaths = []

Graph = nx.MultiGraph()
Graph.add_nodes_from(nodes)
Graph.add_edges_from(data)

for path in nx.algorithms.all_simple_paths(Graph, source='start', target='end'):
    print(path)
    repeat = ([item for item, count in collections.Counter(path).items() if count > 1])
    valid = True
    for item in path:
        if str(repeat).islower():
            valid = False
            break
    if valid:
        allValidPaths.append(path)

path = []
node='start'

def recursivePath(Graph, start, end='end'):
    if start == end:
        return end
    else:
        path

while True:
    
for nodes in Graph.neighbors('start'):
    print(nodes)
"""

E=collections.defaultdict(list)
lines =  open (os.path.join(sys.path[0],"input.txt"), "r")   
for line in lines:
    a,b = line.strip().split("-")
    E[a].append(b)
    E[b].append(a)

start = ('start', set(["start"]), None)
ans = 0
Q=collections.deque([start])
while Q:
    pos,small, twice = Q.popleft()
    #print(pos, small)
    if pos =='end':
        ans +=1
        continue
    for y in E[pos]:
        if y not in small:
            new_small = set(small)
            if y.lower() == y:
                new_small.add(y)
            Q.append((y,new_small, twice))
        elif y in small and twice is None and y not in ['start', 'end']:
           Q.append((y,small,y))
print(ans)

