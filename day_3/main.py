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


# part 2
def find_rating(mat, mode):
    filtered_bool = np.ones(len(mat), dtype=bool)
    for bit in mat.T:
        filtered_bit = bit[filtered_bool]
        counts = Counter(filtered_bit)
        # update filtered_bool
        if mode == 'o2':
            filtered_bool = filtered_bool & (bit == int(counts[1] >= counts[0]))
        elif mode == 'co2':
            filtered_bool = filtered_bool & (bit == int(counts[1] < counts[0]))
        else:
            raise Exception('invalid mode')
        # break condition
        if sum(filtered_bool) <= 1:
            return mat[filtered_bool]


o2_rating = find_rating(mat, 'o2')[0]
co2_rating = find_rating(mat, 'co2')[0]

string_rating = [''.join([str(j) for j in i]) for i in [o2_rating, co2_rating]]
decimal_rating = np.array([int(i, 2) for i in string_rating])
print(np.prod(decimal_rating))