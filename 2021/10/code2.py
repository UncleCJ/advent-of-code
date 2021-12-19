import os, sys
import bisect
# Advent of code Year 2021 Day 10 solution
# Author = Joao Antunes
# Date = December 2021

this_file_name = os.path.basename(sys.argv[0])
filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open((__file__.rstrip(this_file_name) + filename), 'r') as input_file:
    lines = input_file.readlines()

OPEN = {'[': ']', '(': ')', '{': '}', '<': '>'}
CLOSE = {']': '[', ')': '(', '}': '{', '>': '<'}
POINTS = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

scores = []
for line in lines:
    score = 0
    stack = []
    corrupted = False
    for c in line:
        if c in OPEN:
            stack.append(c)
        elif c in CLOSE:
            expected = stack.pop()
            if CLOSE[c] != expected:
                corrupted = True
                break
    if not corrupted:
        while stack:
            open_chunk = stack.pop()
            missing_close = OPEN[open_chunk]
            score = 5 * score + POINTS[missing_close]
        bisect.insort_left(scores, score)

middle = len(scores)//2
print(scores[middle])