import sys

# Advent of code Year 2021 Day 9 solution
# Author = Joao Antunes
# Date = December 2021

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
board = [[None]]
cols = 0
with open((__file__.rstrip("code.py") + filename), 'r') as input_file:
    for line in input_file:
        row = list(map(lambda x: int(x), line.rstrip()))
        row = [9] + row + [9]
        cols = max(cols, len(row))
        board.append(row)

# add extra rows and cols with value 9, to make it easier to find lows on the edges
board[0] = [9] * cols
board.append([9] * cols)
rows = len(board)

sums = 0
for i in range(1, rows-1):
    for j in range(1, cols-1):
        if board[i][j-1] > board[i][j] < board[i][j+1] and board[i-1][j] > board[i][j] < board[i+1][j]:
            risk = board[i][j] + 1
            # print(risk)
            sums += risk


print(sums)
