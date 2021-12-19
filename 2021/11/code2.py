import os, sys
# Advent of code Year 2021 Day 11 solution
# Author = Joao Antunes
# Date = December 2021

this_file_name = os.path.basename(sys.argv[0])
filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open((__file__.rstrip(this_file_name) + filename), 'r') as input_file:
    board = [[int(c) for c in line.rstrip()] for line in input_file]

N = len(board)
M = len(board[0])

def print_board():
    for row in board:
        print("".join([ str(n) for n in row]))

flashes = 0
def propagate(i, j, first):
    global flashes
    flashed_lst = []
    if not (0 <= i < N and 0 <= j < M):
        return flashed_lst
    if not first and board[i][j] == 0:
        return flashed_lst

    board[i][j] += 1
    if board[i][j] == 10:
        flashes += 1
        board[i][j] = 0
        for k in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)):
            flashed_lst.append((i+k[0], j+k[1]))
    return flashed_lst

print_board()
steps = 0
while flashes != N * M:
    flashes = 0
    print()
    to_increment_lst = []
    for i in range(N):
        for j in range(M):
            flashed_lst = propagate(i, j, first=True)
            to_increment_lst.extend(flashed_lst)
    while to_increment_lst:
        i, j = to_increment_lst.pop()
        flashed_lst = propagate(i, j, first=False)
        to_increment_lst.extend(flashed_lst)
    steps += 1
    # print_board()

print(steps)