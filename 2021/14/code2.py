import os, sys
from collections import Counter
from functools import cache

# Advent of code Year 2021 Day 14 solution
# Author = Joao Antunes
# Date = December 2021

this_file_name = os.path.basename(sys.argv[0])
filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open((__file__.rstrip(this_file_name) + filename), 'r') as input_file:
    template = list(input_file.readline().rstrip())
    input_file.readline()

    rules = {}
    for line in input_file:
        pair, insert = line.rstrip().split(" -> ")
        rules[tuple(pair)] = insert

print(template)

@cache
def count(n, pair):
    insert = rules[pair]
    if n == 1:
        return Counter([insert])
    left = count(n-1, (pair[0], insert))
    right = count(n-1, (insert, pair[1]))
    return left + Counter([insert]) + right

steps = 40
counters = {}
for pair in rules:
    counters[pair] = count(steps, pair)

counter = Counter(template)
for i in range(len(template) - 1):
    pair = tuple(template[i:i+2])
    if pair in rules:
        counter += counters[pair]

print(counter)
print(counter.most_common(1)[0][1] - counter.most_common()[-1][1])
