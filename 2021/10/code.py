import sys
# Advent of code Year 2021 Day 10 solution
# Author = Joao Antunes
# Date = December 2021

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open((__file__.rstrip("code.py")+filename), 'r') as input_file:
    lines = input_file.readlines()

OPEN = set("[({<")
CLOSE = { ']': '[', ')': '(', '}': '{', '>': '<' }
POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

score = 0
for line in lines:

    stack = []
    for c in line:
        if c in OPEN:
            # print(f"open: {c}")
            stack.append(c)
        elif c in CLOSE:
            # print(f"close: {c}")
            expected = stack.pop()
            if CLOSE[c] != expected:
                score += POINTS[c]
                break
print(score)
