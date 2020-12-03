# Advent of code Year 2020 Day 3 solution
# Author = BNAndras
# Date = December 2020

with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()
    grid = [x for x in input.splitlines() if x]
    widthOfGrid = len(grid[0])
    heightOfGrid = len(grid)

def countEncounteredTreesAtSlopeRepresentedAs(deltaXY):
    currentX = 0
    currentY = 0
    treesEncountered = 0
    while currentY < heightOfGrid:
        if (grid[currentY][currentX % widthOfGrid] == "#"): treesEncountered += 1
        currentX += deltaXY[0]
        currentY += deltaXY[1]
    return treesEncountered

treesSlope3and1 = countEncounteredTreesAtSlopeRepresentedAs( (3, 1) )
print("Part One : {}".format(treesSlope3and1))

allTreesEncountered = treesSlope3and1

slopes = [(1, 1), (5, 1), (7, 1), (1, 2)]

for slope in slopes:
    allTreesEncountered *= countEncounteredTreesAtSlopeRepresentedAs(slope)

print("Part Two : {}".format(allTreesEncountered))