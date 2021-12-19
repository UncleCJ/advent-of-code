import os, sys
from collections import defaultdict
# Advent of code Year 2021 Day 12 solution
# Author = Joao Antunes
# Date = December 2021

this_file_name = os.path.basename(sys.argv[0])
filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open((__file__.rstrip(this_file_name) + filename), 'r') as input_file:
    edges = defaultdict(list)
    can_be_used_twice = set()
    for line in input_file:
        edge = line.rstrip().split("-")
        edges[edge[0]].append(edge[1])
        edges[edge[1]].append(edge[0])
        for n in (edge[0], edge[1]):
            if n not in ("start", "end") and n.islower():
                can_be_used_twice.add(n)

paths = set()
def find_path(node, visited, path, twice):
    if node == 'end':
        paths.add(tuple(path))
        return
    if node.islower():
        if node in visited:
            if node == twice:
                twice = None
            else:
                return
        else:
            visited.add(node)
    for n in edges[node]:
        find_path(n, visited.copy(), path + [n], twice)

for n in edges['start']:
    for t in can_be_used_twice:
        find_path(n, set(['start']), ['start', n], t)

nl = "\n"
print(f'paths: {nl.join([",".join(p) for p in paths])}')
print(len(paths))
