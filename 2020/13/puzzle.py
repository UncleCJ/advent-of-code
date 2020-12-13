# Advent of code Year 2020 Day 13 solution
# Author = BNAndras
# Date = December 2020

with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
    inp = input_file.read().splitlines()
    departureTime = int(inp[0])
    busIds = [int(bus) for bus in inp[1].split(",") if bus != "x"]

earliestBusId = 0
minTimeWaitedForAnyBus = None
for busId in busIds:
    firstStopAfterDepartureTime = (departureTime // busId + 1) * busId
    timeWaitedForThisBus = firstStopAfterDepartureTime - departureTime
    if not minTimeWaitedForAnyBus: minTimeWaitedForAnyBus = timeWaitedForThisBus
    elif timeWaitedForThisBus < minTimeWaitedForAnyBus:
        minTimeWaitedForAnyBus = timeWaitedForThisBus
        earliestBusId = busId

print("Part One : {}".format(earliestBusId * minTimeWaitedForAnyBus))