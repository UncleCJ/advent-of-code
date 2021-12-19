# Advent of code Year 2021 Day 4 solution
# Author = Joao Antunes
# Date = December 2021
ans = None

marked = []
with open((__file__.rstrip("code1.py")+"test.txt"), 'r') as input_file:
    line = input_file.readline().split(",")
    numbers = [int(number) for number in line]
    boards = []

    while input_file.readline():
        board = []
        board_mark = {'rows': [0]*5, 'cols': [0]*5}
        for i in range(5):
            line = input_file.readline().split()
            row = [int(number) for number in line]
            board.append(row)
        print(board)
        boards.append(board)
        marked.append(board_mark)


del board
del line
################################################################################
def mark(index, i, j, n):
    if n != boards[index][i][j]:
        return False
    print(f"marking {n} on board {index+1}")
    boards[index][i][j] = None
    marked[index]['rows'][i] += 1
    marked[index]['cols'][j] += 1
    return marked[index]['rows'][i] == 5 or marked[index]['cols'][j] == 5

def sums(board):
    flat_list = [item for sublist in board for item in sublist if item is not None]
    return sum(flat_list)

def board_wins(index, n):
    for i in range(5):
        for j in range(5):
            if mark(index, i, j, n):
                return True
    return False

for n in numbers:
    for i in range(len(boards)):
        if board_wins(i, n):
            ans = n * sums(boards[i])
            print(f"Solution: {ans}")
            exit()
