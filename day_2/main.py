import numpy as np


def action(action_string, n, current_pos):
    if action_string == 'forward':
        current_pos[0] = current_pos[0] + n
    elif action_string == 'up':
        current_pos[1] = current_pos[1] - n
    elif action_string == 'down':
        current_pos[1] = current_pos[1] + n
    else:
        raise Exception('invalid action string')

    return current_pos


def action2(action_string, n, current_pos):
    if action_string == 'forward':
        current_pos[0] = current_pos[0] + n
        current_pos[1] = current_pos[1] + (current_pos[2] * n)
    elif action_string == 'up':
        current_pos[2] = current_pos[2] - n
    elif action_string == 'down':
        current_pos[2] = current_pos[2] + n
    else:
        raise Exception('invalid action string')

    return current_pos


def follow_instructions(func, f, current_pos):
    for instruction in f:
        action_string, n = instruction.split()
        current_pos = func(action_string, int(n), current_pos)
    return current_pos


# input
f = open('input.txt')

# part 1
current_pos = [0, 0]
current_pos = follow_instructions(action, f, current_pos)
print(np.prod(current_pos))

# part 2
f = open('input.txt')

current_pos = [0, 0, 0]
current_pos = follow_instructions(action2, f, current_pos)
print(np.prod(current_pos[:2]))
