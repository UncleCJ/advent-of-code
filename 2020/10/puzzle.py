# Advent of code Year 2020 Day 10 solution
# Author = BNAndras
# Date = December 2020

#from itertools import combinations
#from collections import defaultdict

with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
    inp = input_file.read()
    adapters = [int(line) for line in inp.splitlines()]
    adapters.append(0) # charging outlet
    adapters.append(max(adapters) + 3) # my device
    adapters.sort()

differencesOfOneJolt = 0
differencesOfThreeJolts = 0

#differencesInJoltage = [(adapter2 - adapter1) for (adapter1, adapter2) in combinations(adapters, 2)]
#differencesOfOneJolt = differencesInJoltage[1]
#differencesOfThreeJolts = differencesInJoltage[3]
for i in range(len(adapters) - 1):
    differenceInAdjacentAdapters = adapters[i+1] - adapters[i]
    if differenceInAdjacentAdapters == 1: differencesOfOneJolt += 1
    elif differenceInAdjacentAdapters == 3: differencesOfThreeJolts += 1


print("Part One : {}".format(differencesOfOneJolt * differencesOfThreeJolts))

#possibleArrangements = defaultdict(int)
possibleArrangements = [0] * len(adapters)
possibleArrangements[0] = 1 # Represents cached arrangement from above
for firstAdapterIndex in range(1, len(adapters)): # skip above cached
    for secondAdapterIndex in range(0, firstAdapterIndex):
        if adapters[firstAdapterIndex] - adapters[secondAdapterIndex] <= 3:
            possibleArrangements[firstAdapterIndex] += possibleArrangements[secondAdapterIndex]

print("Part Two : {}".format(max(possibleArrangements)))
