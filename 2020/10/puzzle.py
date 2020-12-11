# Advent of code Year 2020 Day 10 solution
# Author = BNAndras
# Date = December 2020

#from itertools import combinations
#from collections import Counter, defaultdict

with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
    inp = input_file.read()
    adapters = [int(line) for line in inp.splitlines()]
    adapters.append(0) # charging outlet
    adapters.append(max(adapters) + 3) # my device
    adapters.sort()

differencesOfOneJolt = 0
differencesOfThreeJolts = 0

for i in range(len(adapters) - 1):
    differenceInAdjacentAdapters = adapters[i+1] - adapters[i]
    if differenceInAdjacentAdapters == 1: differencesOfOneJolt += 1
    elif differenceInAdjacentAdapters == 3: differencesOfThreeJolts += 1


print("Part One : {}".format(differencesOfOneJolt * differencesOfThreeJolts))

possibleArrangements = [0] * len(adapters)
possibleArrangements[0] = 1 # Represents no adapter, device directly connected
for firstAdapterIndex in range(1, len(adapters)):
    for secondAdapterIndex in range(firstAdapterIndex - 3, first):
              possibleArrangements[firstAdapterIndex] += possibleArrangements[secondAdapterIndex]

print("Part Two : {}".format(max(possibleArrangements)))
