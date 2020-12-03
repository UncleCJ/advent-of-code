# Advent of code Year 2020 Day 3 solution
# Author = BNAndras
# Date = December 2020

from collections import namedtuple

with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()
    grid = [x for x in input.splitlines() if x]
    widthOfGrid = len(grid[0])
    heightOfGrid = len(grid)

def countEncounteredTreesAtSlopeRepresentedAs(deltaSlope):
    Position = namedtuple('Position', 'X Y')
    currentPosition = Position(0, 0)
    treesEncountered = 0
    while currentPosition.Y < heightOfGrid:
        if (grid[currentPosition.Y][currentPosition.X % widthOfGrid] == "#"): treesEncountered += 1
        currentPosition = Position(
            (currentPosition.X + deltaSlope.deltaX), (currentPosition.Y + deltaSlope.deltaY)
        )
    return treesEncountered

Slope = namedtuple('Slope', 'deltaX deltaY')
treesSlope3and1 = countEncounteredTreesAtSlopeRepresentedAs( Slope(3, 1) )
print("Part One : {}".format(treesSlope3and1))

allTreesEncountered = treesSlope3and1
remainingSlopes = [Slope(1, 1), Slope(5, 1), Slope(7, 1), Slope(1, 2)]

for slope in remainingSlopes:
    allTreesEncountered *= countEncounteredTreesAtSlopeRepresentedAs(slope)

print("Part Two : {}".format(allTreesEncountered))