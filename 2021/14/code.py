import os, sys
from collections import Counter
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
# print(rules)

steps = 10
for _ in range(steps):
    new_template = []
    for i in range(len(template)-1):
        pair = tuple(template[i:i+2])
        # print(pair)
        new_template.append(pair[0])
        if pair in rules:
            new_template.append(rules[pair])
    new_template.append(pair[1])
    template = new_template
    # print("".join(template))

counter = Counter(template)
print(counter)
print(counter.most_common(1)[0][1] - counter.most_common()[-1][1])
