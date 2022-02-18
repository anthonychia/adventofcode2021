import numpy as np
from collections import Counter


class fish():
    def __init__(self, internal_timer=8):
        self.timer = internal_timer

    def decrease_timer(self):
        self.timer -= 1
        if self.timer < 0:
            self.timer = 6
            return self.create_new_fish()
        else:
            return None

    @staticmethod
    def create_new_fish():
        return fish()

    def __str__(self):
        return str(self.timer)

class pool():
    def __init__(self, fishes):
        self.fishes = fishes

    def increase_day(self):
        to_add = []
        for fish in self.fishes:
            new_fish = fish.decrease_timer()
            if new_fish:
                to_add.append(new_fish)
        self.fishes += to_add

    def __str__(self):
        return str(len(self.fishes))

# input
f = open('input.txt')
line = f.readline().split(',')
existing_fish_timers = list(map(int, line))
fishes = [fish(timer) for timer in existing_fish_timers]
current_pool = pool(fishes)

# part 1
for day in range(1, 80+1):
    # print(f'day {day}')
    current_pool.increase_day()
    # for i in current_pool.fishes:
    #     print(i)

print(current_pool)

# part 2
v = np.zeros(9)

for key, value in Counter(existing_fish_timers).items():
    v[key] = value

for day in range(1, 256+1):
    old_v = v.copy()
    for i in range(len(v)):
        if i != 8:
            v[i] = old_v[i+1]
        elif i == 8:
            v[i] = old_v[0]
            v[6] += old_v[0]
    print(v)

print(int(sum(v)))