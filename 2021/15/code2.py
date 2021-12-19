import os, sys
from functools import cache
from collections import defaultdict
import heapq

# Advent of code Year 2021 Day 15 solution
# Author = Joao Antunes
# Date = December 2021


def print_board(board):
    for row in board:
        print(" ".join([str(n) for n in row]))

this_file_name = os.path.basename(sys.argv[0])
filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open((__file__.rstrip(this_file_name) + filename), 'r') as input_file:
    board = []
    for line in input_file:
        row = [int(c) for c in line.rstrip()]
        board.append(row)
    print_board(board)

    N = len(board)
    M = len(board[0])

    # copy board
    EXTEND = 4
    for i in range(N):
        board[i].extend([0] * M * EXTEND)
        for j in range(M):
            for k in range(1, EXTEND+1):
                board[i][j+k*M] = board[i][j+(k-1)*M] + 1
                if board[i][j+k*M] == 10:
                    board[i][j+k*M] = 1

    for _ in range(EXTEND):
        for i in range(N):
            i = len(board) - N
            board.append(board[i].copy())
            for j in range(len(board[i])):
                board[i+N][j] = board[i][j] + 1
                if board[i+N][j] == 10:
                    board[i+N][j] = 1
    print_board(board)

    N = len(board)
    M = len(board[0])
    MAX = float("+inf")

    heap = []
    heapq.heappush(heap, (0, (0,0)))
    distance = defaultdict(lambda: MAX)
    distance[(0,0)] = 0
    while heap:
        cost_to_node, (i,j) = heapq.heappop(heap)
        # expand all neighbors and add them to heap
        for ki, kj in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            x, y = i+ki, j+kj
            if not (0 <= x < N and 0 <= y < M): continue
            cost_to_neighbor = cost_to_node + board[x][y]
            if cost_to_neighbor < distance[(x, y)]:
                # We improved our distance, add to heap
                distance[(x, y)] = cost_to_neighbor
                if (x,y) == (N-1, M-1):
                    break
                heapq.heappush(heap, (cost_to_neighbor, (x, y)))
    print(distance[(N-1, M-1)])
