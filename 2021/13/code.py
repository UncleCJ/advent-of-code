import os, sys
# Advent of code Year 2021 Day 13 solution
# Author = Joao Antunes
# Date = December 2021

this_file_name = os.path.basename(sys.argv[0])
filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
map_axis_to_index = {"x": 0, "y": 1}
with open((__file__.rstrip(this_file_name) + filename), 'r') as input_file:
    dots = []
    fold_along = []
    collect_dots = True
    for line in input_file:
        if line == "\n":
            collect_dots = False
            continue

        if collect_dots:
            x, y = line.rstrip().split(",")
            dots.append([int(x), int(y)])
        else:
            fold_along_line = line.rstrip().split(" ")[2]
            axis, val = fold_along_line.split("=")
            fold_along.append((axis, int(val)))

part_one = True
for axis, val in fold_along:
    N, M = 0, 0
    for coord in dots:
        ci = map_axis_to_index[axis]
        if coord[ci] > val:
            coord[ci] = val - (coord[ci] - val)
        # print(coord[ci])
        N, M = max(N, coord[1]+1), max(M, coord[0]+1)
    if part_one:
        part_one = False
        unique_dots = set([(x, y) for x, y in dots])
        print(f"PART ONE: {len(unique_dots)}")

board = [M*[" "] for _ in range(N)]
for x, y in dots:
    board[y][x] = "█"


def print_board():
    for row in board:
        print("".join([str(n) for n in row]))

print("PART TWO")
print_board()
