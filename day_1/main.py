import numpy as np


def shift_diff(a, n):
    return np.diff(a, n=n)


def rolling_sum(a, n):
    ret = np.cumsum(a)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:]


def find_n_positives(a):
    return sum(a > 0)


# Input
depths = np.genfromtxt("input.txt")

# Part 1
diff = shift_diff(depths, n=1)
print(find_n_positives(diff))

# Part 2
slides = rolling_sum(depths, n=3)
diff = shift_diff(slides, n=1)
print(find_n_positives(diff))