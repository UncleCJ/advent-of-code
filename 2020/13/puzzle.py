# Advent of code Year 2020 Day 13 solution
# Author = BNAndras
# Date = December 2020

from sys import maxsize

with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
    inp = input_file.read().splitlines()
    departureTime = int(inp[0])
    busIntervals = [int(bus) for bus in inp[1].split(",") if bus != "x"]

earliestBusInterval = 0
minTimeWaited = maxsize
for busInterval in busIntervals:
    firstStopAfterDepartureTime = (departureTime // busInterval + 1) * busInterval
    timeWaited = firstStopAfterDepartureTime - departureTime
    if timeWaited < minTimeWaited:
        minTimeWaited = timeWaited
        earliestBusInterval = busInterval

print("Part One : {}".format(earliestBusInterval * minTimeWaited))