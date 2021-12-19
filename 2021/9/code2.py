import sys
import heapq

# Advent of code Year 2021 Day 9 solution
# Author = Joao Antunes
# Date = December 2021

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
board = [[None]]
cols = 0
with open((__file__.rstrip("code2.py") + filename), 'r') as input_file:
    for line in input_file:
        row = list(map(lambda x: int(x), line.rstrip()))
        row = [9] + row + [9]
        cols = max(cols, len(row))
        board.append(row)

# add extra rows and cols with value 9, to make it easier to find lows on the edges
board[0] = [9] * cols
board.append([9] * cols)
rows = len(board)

lows = []
for i in range(1, rows-1):
    for j in range(1, cols-1):
        if board[i][j-1] > board[i][j] < board[i][j+1] and board[i-1][j] > board[i][j] < board[i+1][j]:
            lows.append((i, j))


def markBasin(i, j):
    if not (0 <= i < rows and 0 <= j < cols) or board[i][j] == 9:
        return 0
    board[i][j] = 9
    return 1 + markBasin(i-1, j) + markBasin(i+1, j) + markBasin(i, j-1) + markBasin(i, j+1)


sizes = []
heapq.heapify(sizes)
for i, j in lows:
    size = markBasin(i, j)
    heapq.heappush(sizes, -size)

ans = 1
for _ in range(3):
    ans *= -heapq.heappop(sizes)

print(ans)
