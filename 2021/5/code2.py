# Advent of code Year 2021 Day 5 solution
# Author = Joao Antunes
# Date = December 2021

ans = None
lines = []
X = 0
Y = 0
with open((__file__.rstrip("code2.py")+"input.txt"), 'r') as input_file:
    for textline in input_file:
        line = []
        for point in textline.split(" -> "):
            x, y = point.split(",")
            line.append((int(x), int(y)))
        X = max(X, line[0][0], line[1][0])
        Y = max(Y, line[0][1], line[1][1])
        lines.append(line)
print(lines)
print(f"X: {X}; Y: {Y}")

board = [[0] * (Y+1) for _ in range(X+1)]
overlap = set()
for (p0, p1) in lines:
    x0, y0 = p0
    x1, y1 = p1
    if x0 == x1 or y0 == y1:
        xrange = range(x0, x1 + 1) if x0 <= x1 else range(x0, x1 - 1, -1)
        yrange = range(y0, y1 + 1) if y0 <= y1 else range(y0, y1 - 1, -1)
        for i in xrange:
            for j in yrange:
                board[i][j] += 1
                if board[i][j] >= 2:
                    overlap.add((i, j))
    elif abs(x0 - x1) == abs(y0 - y1):
        print(f"{p0} -> {p1}")
        xrange = range(x0, x1 + 1) if x0 <= x1 else range(x0, x1 - 1, -1)
        y_increment = 1 if y0 <= y1 else -1
        j = y0
        for i in xrange:
            board[i][j] += 1
            if board[i][j] >= 2:
                overlap.add((i, j))
            j += y_increment

for bline in board:
    for val in bline:
        print(f"{val} ", end="")
    print()

# print(board)
print(len(overlap))
