import numpy as np
import math


# input
f = open("sample.txt")
lines = f.readlines()
grid = np.array([list(map(int, line.replace('\n', ''))) for line in lines])
max_x = len(grid[1])
max_y = len(grid)

nodes = np.transpose(grid.nonzero())
grid = {(node[0], node[1]): grid[node[0], node[1]] for node in nodes}
distances = {(node[0], node[1]): {} for node in nodes}
for node in nodes:
    for i in [(0, 1), (-1, 0), (1, 0), (-1, 0)]:
        neighbour = (node[0]+i[0], node[1]+i[1])
        if neighbour in grid.keys(): distances[(node[0], node[1])][neighbour] = grid[neighbour]

# part 1
unvisited = {(node[0], node[1]): None for node in nodes} #using None as +inf
visited = {}
current = (0, 0)
currentDistance = 0
unvisited[current] = currentDistance

while True:
    for neighbour, distance in distances[current].items():
        if neighbour not in unvisited: continue
        newDistance = currentDistance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance
    visited[current] = currentDistance
    del unvisited[current]
    if not unvisited: break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]

print(visited[(max_y-1, max_x-1)])


# part 2
grid = np.array([list(map(int, line.replace('\n', ''))) for line in lines])
org_max_x = len(grid[1])
org_max_y = len(grid)
grid = np.tile(grid, (5, 5))
max_x = len(grid[1])
max_y = len(grid)
for i in range(max_y):
    for j in range(max_x):
        grid[i, j] += math.floor(i / org_max_y)
        grid[i, j] += math.floor(j / org_max_x)
nodes = np.transpose(grid.nonzero())
grid = {(node[0], node[1]): grid[node[0], node[1]] for node in nodes}
distances = {(node[0], node[1]): {} for node in nodes}
for node in nodes:
    for i in [(0, 1), (-1, 0), (1, 0), (-1, 0)]:
        neighbour = (node[0]+i[0], node[1]+i[1])
        if neighbour in grid.keys(): distances[(node[0], node[1])][neighbour] = grid[neighbour]

unvisited = {(node[0], node[1]): None for node in nodes} #using None as +inf
visited = {}
current = (0, 0)
currentDistance = 0
unvisited[current] = currentDistance

while True:
    for neighbour, distance in distances[current].items():
        if neighbour not in unvisited: continue
        newDistance = currentDistance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance
    visited[current] = currentDistance
    del unvisited[current]
    if not unvisited: break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]

print(visited[(max_y-1, max_x-1)])