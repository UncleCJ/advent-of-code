import os, sys
# Advent of code Year 2021 Day 15 solution
# Author = Joao Antunes
# Date = December 2021


def print_board(board):
    for row in board:
        print("\t".join([str(n) for n in row]))

this_file_name = os.path.basename(sys.argv[0])
filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open((__file__.rstrip(this_file_name) + filename), 'r') as input_file:
    board = []
    for line in input_file:
        row = [int(c) for c in line.rstrip()]
        board.append(row)
    print_board(board)
    MAX = float("+inf")

    N = len(board)
    M = len(board[0])
    risk = [[MAX] * (M + 1) for _ in range(N + 1)]
    risk[N][M] = 0
    risk[N-1][M] = 0
    risk[N][M-1] = 0

    # THIS IS ACTUALLY WRONG.
    # I was assuming we can only go down or right (and never back up or left).
    # See Part 2 for the correct solution
    for i in reversed(range(N)):
        for j in reversed(range(M)):
            risk[i][j] = min(risk[i+1][j], risk[i][j+1]) + board[i][j]

    print_board(risk)
    print(risk[0][0] - board[0][0])
