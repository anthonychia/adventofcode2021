import numpy as np


# input
f = open('sample.txt')

line = f.readline()
sequence = list(map(int, line.split(',')))
lines = f.readlines()
step_size = 6
boards = []

for i in range(1, len(lines), step_size):
    board = [list(map(int, line.replace('\n', '').split())) for line in lines[i:i + step_size] if line != '\n']
    boards.append(board)
boards = np.array(boards)

# part 1
bool_mat = np.zeros((len(boards), 5, 5), dtype=bool)

win_flag = False
for s in sequence:
    # update bool matrix
    bool_mat = bool_mat | (boards == s)
    # check win
    for i in range(len(bool_mat)):
        if any([all(row) for row in bool_mat[i]]) or any([all(row) for row in bool_mat[i].T]):
            win_flag = True
            winning_board = boards[i]
    if win_flag: break

score = sum(winning_board[~bool_mat[i]]) * s
print(score)

# part 2
bool_mat = np.zeros((len(boards), 5, 5), dtype=bool)
filtered_boards = boards.copy()
filtered_bool_mat = bool_mat.copy()

for s in sequence:
    # update bool matrix
    filtered_bool_mat = filtered_bool_mat | (filtered_boards == s)
    # drop win boards
    for i in range(len(filtered_bool_mat)):
        if any([all(row) for row in filtered_bool_mat[i]]) or any([all(row) for row in filtered_bool_mat[i].T]):
            last_winning_board = filtered_boards[i]
            last_winning_bool = filtered_bool_mat[i]
            filtered_bool_mat = np.delete(filtered_bool_mat, i, 0)
            filtered_boards = np.delete(filtered_boards, i, 0)
            break
    if len(filtered_bool_mat) <= 1 or s == sequence[-1]: break

score = sum(last_winning_board[~last_winning_bool]) * s
print(score)

