import numpy as np
import math


def range_include_end(start, stop):
    return range(start, stop+1)


# input
f = open('input.txt')
lines = f.readlines()
vents = [[list(map(int, coords.split(','))) for coords in line.replace('\n', '').split(' -> ')] for line in lines]
vents = np.array(vents)

# part 1
grid = np.zeros((np.max(vents)+1, np.max(vents)+1))
for vent in vents:
    x1, x2, y1, y2 = vent[0, 0], vent[1, 0], vent[0, 1], vent[1, 1]
    if x1 == x2:
        for i in range_include_end(*sorted([y1, y2])):
            grid[x1, i] += 1
    elif y1 == y2:
        for i in range_include_end(*sorted([x1, x2])):
            grid[i, y1] += 1
    else:
        continue

print(np.sum(grid >= 2))

# part 2
grid = np.zeros((np.max(vents)+1, np.max(vents)+1))
for vent in vents:
    x1, x2, y1, y2 = vent[0, 0], vent[1, 0], vent[0, 1], vent[1, 1]
    if x1 == x2:
        for i in range_include_end(*sorted([y1, y2])):
            grid[x1, i] += 1
    elif y1 == y2:
        for i in range_include_end(*sorted([x1, x2])):
            grid[i, y1] += 1
    elif np.abs(x2-x1) == np.abs(y2-y1):
        xc, yc = x1, y1
        while xc != x2 + np.sign(x2 - x1)\
                and yc != y2 + np.sign(y2 - y1):
            grid[xc, yc] += 1
            xc = xc + np.sign(x2 - x1)
            yc = yc + np.sign(y2 - y1)
    else:
        continue

print(np.sum(grid >= 2))

