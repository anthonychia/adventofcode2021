from itertools import product
from typing import List
import sys

import numpy as np

class Octopos():
    adjacent = []

    def __init__(self, initial_energy, position: tuple):
        self.energy = initial_energy
        self.position = position

    def increase_energy(self):
        self.energy += 1
        self.adjacent = []
        if self.energy > 9:
            self.flash()
            self.energy = 0
            return self.adjacent, True
        return None, False

    def flash(self):
        for i in np.array(list(product((-1, 0, 1), repeat=2))):
            if not list(i) == [0, 0]: # ignore self
                self.adjacent.append(self.position + i)


# input
f = open('input.txt')
lines = [line.replace('\n', '') for line in f.readlines()]
grid = np.array([list(map(int, line)) for line in lines])
max_x = len(grid)
max_y = len(grid[0])
octoposes: List[Octopos] = np.zeros((len(grid), len(grid[0])), dtype=Octopos)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        octoposes[i, j] = Octopos(grid[i, j], (i, j))

total_flashes = 0
flashes = 0
step = 1
while flashes < max_x*max_y:
    flashes = 0
    print(step)
    flashed_bool = np.zeros((max_x, max_y), dtype=bool)
    adjacent = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            adj, flashed = octoposes[i, j].increase_energy()
            flashed_bool[i, j] = flashed
            flashes += int(flashed)
            if adj: adjacent += [list(l) for l in adj]

    while len(adjacent) > 0:
        for k in adjacent:
            if 0 <= k[0] < len(grid) and 0 <= k[1] < len(grid[0]) and not flashed_bool[k[0], k[1]]:
                adj, flashed = octoposes[k[0], k[1]].increase_energy()
                flashes += int(flashed)
                flashed_bool[k[0], k[1]] = flashed
                if adj: adjacent += [list(l) for l in adj]
            adjacent.remove(k)
            for i, j in np.transpose(flashed_bool.nonzero()):
                if [i, j] in adjacent:
                    # print(i, j)
                    adjacent.remove([i, j])

    grid = np.vectorize(lambda x: x.energy)(octoposes)
    total_flashes += flashes
    step += 1
    print(grid, flush=True)

print(total_flashes)

