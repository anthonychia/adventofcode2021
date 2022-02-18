import numpy as np
# from scipy import stats

# input
f = open('input.txt')
line = f.readline().split(',')
crabs = list(map(int, line))

# part 1
best_guess = int(np.median(crabs))
total_fuel = 0

for crab in crabs:
    total_fuel += np.abs(crab - best_guess)

print(total_fuel)

# part 2
best_guess = int(np.mean(crabs))
total_fuel = 0

for crab in crabs:
    n = np.abs(crab - best_guess)
    total_fuel += (n**2 + n)/2

print(int(total_fuel))