import numpy as np
from scipy import signal


# input
f = open('input.txt')
lines = f.readlines()
grid = np.array([[int(i) for i in line.replace('\n', '')] for line in lines])

# part 1
kernels = [
    np.array([[0, 0, 0], [0, 1, 0], [0, -1, 0]]),
    np.array([[0, -1, 0], [0, 1, 0], [0, 0, 0]]),
    np.array([[0, 0, 0], [0, 1, -1], [0, 0, 0]]),
    np.array([[0, 0, 0], [-1, 1, 0], [0, 0, 0]])
    ]
gs = []
for kernel in kernels:
    g = signal.convolve2d(grid, kernel, mode='same', boundary='fill', fillvalue=99)

    gs.append(g<0)

low_point_bool = sum(gs) >= 4
print(np.sum(grid[low_point_bool] + 1))

# part 2
class Solution:
    def find_all_areas(self, grid, lowest_points):
        self.r_len = len(grid)
        self.c_len = len(grid[0])
        areas = []
        for r in lowest_points[:, 0]:
            for c in lowest_points[:, 1]:
                if grid[r][c] == 1:
                    self.total = 0
                    self.find_area(grid, r, c)
                    areas.append(self.total)
        return areas
    def find_area(self, matrix, r, c):
        self.total += 1
        matrix[r][c] = 0
        if r - 1 >= 0 and matrix[r - 1][c] == 1:
            self.find_area(matrix, r - 1, c)
        if c - 1 >= 0 and matrix[r][c - 1] == 1:
            self.find_area(matrix, r, c - 1)
        if r + 1 < self.r_len and matrix[r + 1][c] == 1:
            self.find_area(matrix, r + 1, c)
        if c + 1 < self.c_len and matrix[r][c + 1] == 1:
            self.find_area(matrix, r, c + 1)

ob = Solution()
areas = ob.find_all_areas(grid != 9, np.transpose(low_point_bool.nonzero()))
print(np.prod(sorted(areas, key=lambda x: x, reverse=True)[:3]))