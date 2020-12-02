# Advent of code Year 2020 Day 1 solution
# Author = BNAndras
# Date = December 2020
from itertools import combinations
with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read().splitlines()
    data = [int(row.rstrip()) for row in input if row.rstrip()]

for a,b in combinations(data, 2):
    if a + b == 2020: p1 = a * b

print("Part One : {}".format(p1))

for a,b,c in combinations(data, 3):
    if a + b + c == 2020: p2 = a * b * c

print("Part Two : {}".format(p2))