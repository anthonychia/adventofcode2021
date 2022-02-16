from collections import Counter
import numpy as np

# input
lines = np.genfromtxt('input.txt', dtype=str)

# part 1
mat = np.array([list(map(int, line)) for line in lines])
counts = [Counter(bit) for bit in mat.T]
gamma = [str(int(count[1] > count[0])) for count in counts]
epsilon = [str(int(count[1] < count[0])) for count in counts]

print(int(''.join(gamma), 2) * int(''.join(epsilon), 2))