import os, sys
from collections import defaultdict
# Advent of code Year 2021 Day 12 solution
# Author = Joao Antunes
# Date = December 2021

this_file_name = os.path.basename(sys.argv[0])
filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open((__file__.rstrip(this_file_name) + filename), 'r') as input_file:
    edges = defaultdict(list)
    for line in input_file:
        edge = line.rstrip().split("-")
        edges[edge[0]].append(edge[1])
        edges[edge[1]].append(edge[0])

paths = []
def find_path(node, visited, path):
    if node == 'end':
        paths.append(path)
        return
    if node.islower():
        if node in visited:
            return
        else:
            visited.add(node)
    for n in edges[node]:
        find_path(n, visited.copy(), path + [n])

for n in edges['start']:
    find_path(n, set(['start']), ['start', n])

nl = "\n"
print(f'paths: {nl.join([",".join(p) for p in paths])}')
print(len(paths))
