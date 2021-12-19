import os, sys
from collections import deque

# Advent of code Year 2021 Day 17 solution
# Author = Joao Antunes
# Date = December 2021

# target area: x=20..30, y=-10..-5
left, right = 20, 30
lower, upper = -10, -5
left, right = 56, 76
lower, upper = -162, -134

def simulate(pos, velocity, max_height=0):
    x, y = pos
    max_height = max(max_height, y)
    if x > right or y < lower:
        return 0, (x, y)
    if x >= left and y <= upper:
        return max_height, (x, y)

    # The probe's x position increases by its x velocity.
    # The probe's y position increases by its y velocity.
    # Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
    # Due to gravity, the probe's y velocity decreases by 1.
    pos[0] += velocity[0]
    pos[1] += velocity[1]
    if velocity[0] > 0:
        velocity[0] -= 1
    elif velocity[0] < 0:
        velocity[0] += 1
    velocity[1] -= 1
    return simulate(pos, velocity, max_height)

heights = {}
highest = 0
probes = deque([(1,1)])
while probes:
    (i, j) = probes.popleft()
    if (i, j) in heights or not (1 <= i < right and 1 <= j < abs(lower)):
        continue
    h, last = simulate([0,0], [i,j])
    heights[(i,j)] = h
    if h > highest:
        highest = h
        probes.append((i+1, j+1))
        print(f"{' *' if h > highest else '  '}{h}\t({i}, {j})")
    else:
        x, y = last
        if x < right:
            probes.append((i+1, j))
            probes.append((i, j+1))
        elif x > right:
            probes.append((i-1, j))
            probes.append((i, j-1))
        if y > lower:
            probes.append((i, j+1))
            probes.append((i, j-1))
            probes.append((i-1, j+1))
            probes.append((i+1, j-1))


highest = 0
for i in range(1, right):
    for j in range(1, 1000):
        h, last = simulate([0,0], [i,j])
        if h > highest:
            print(f" *{h}\t({i}, {j})")
            highest = h
