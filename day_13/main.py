import numpy as np


# input
f = open('input.txt')
lines = []
line = ''
while line != '\n':
    line = f.readline()
    lines.append(line)

instructions = f.readlines()
lines = np.array([list(map(int, line.replace('\n', '').split(','))) for line in lines if line != '\n'])
instructions = np.array([instruction.replace('\n', '').split()[-1] for instruction in instructions])

# print(lines)
# print(instructions)

y_max = np.max(lines[:, 1])
x_max = np.max(lines[:, 0])

grid = np.zeros((y_max+1, x_max+1), dtype=int)

for line in lines:
    grid[line[1], line[0]] += 1

for instruction in instructions:
    if instruction[0] == 'y':
        fold = int(instruction.split('=')[-1])
        # new_grid = np.zeros((grid.shape[0]-fold, grid.shape[1]))
        flipped_grid = np.zeros(grid.shape, dtype=int)
        flipped = (np.transpose(grid.nonzero()) - (fold, 0)) * (-1, 1) + (fold, 0)
        for i in flipped:
            flipped_grid[i[0], i[1]] += 1
        new_grid = (grid + flipped_grid)[:fold, :grid.shape[1]]
    elif instruction[0] == 'x':
        fold = int(instruction.split('=')[-1])
        # new_grid = np.zeros((grid.shape[0], grid.shape[1]-fold))
        flipped_grid = np.zeros(grid.shape, dtype=int)
        flipped = (np.transpose(grid.nonzero()) - (0, fold)) * (1, -1) + (0, fold)
        for i in flipped:
            flipped_grid[i[0], i[1]] += 1
        new_grid = (grid + flipped_grid)[:grid.shape[0], :fold]
    grid = new_grid

print(grid)
print(np.sum(grid > 0))