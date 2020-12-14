# Advent of code Year 2020 Day 11 solution
# Author = BNAndras
# Date = December 2020

from collections import namedtuple
from copy import deepcopy

def RunThroughSeatingChartForPart1(currentStateOfChart):
    workingCopyOfChart = deepcopy(currentStateOfChart)

    for currentPosition in workingCopyOfChart:
        if currentPosition == symbolSeatUnavailable: continue
        countOfOccupiedNeighbors = CountAvailableNeighboringSeatsForPart1(currentStateOfChart, currentPosition)
        if workingCopyOfChart[currentPosition] == symbolSeatAvailable and not countOfOccupiedNeighbors:
            workingCopyOfChart[currentPosition] = symbolSeatOccupied
        elif (workingCopyOfChart[currentPosition] == symbolSeatOccupied
                and countOfOccupiedNeighbors >= 4):
            workingCopyOfChart[currentPosition] = symbolSeatAvailable

    return workingCopyOfChart

def RunThroughSeatingChartForPart2(currentStateOfChart):
    workingCopyOfChart = deepcopy(currentStateOfChart)

    for currentPosition in workingCopyOfChart:
        if currentPosition == symbolSeatUnavailable: continue
        countOfOccupiedNeighbors = CountAvailableNeighboringSeatsForPart2(currentStateOfChart, currentPosition)
        if workingCopyOfChart[currentPosition] == symbolSeatAvailable and not countOfOccupiedNeighbors:
            workingCopyOfChart[currentPosition] = symbolSeatOccupied
        elif (workingCopyOfChart[currentPosition] == symbolSeatOccupied
                and countOfOccupiedNeighbors >= 5):
            workingCopyOfChart[currentPosition] = symbolSeatAvailable

    return workingCopyOfChart

def CountAvailableNeighboringSeatsForPart1(currentStateOfChart, seatPosition):

    relativeOffsetsForNeighbors = [
        Position(X=-1, Y=-1),
        Position(X=-1, Y=0),
        Position(X=-1, Y=1),
        Position(X=0, Y=-1),
        Position(X=0, Y=1),
        Position(X=1, Y=-1),
        Position(X=1, Y=0),
        Position(X=1, Y=1),
    ]

    countOfOccupiedNeighbors = 0
    for relativeOffset in relativeOffsetsForNeighbors:
        currentNeighborPosition = Position(seatPosition.X + relativeOffset.X, seatPosition.Y + relativeOffset.Y)
        if currentStateOfChart.get(currentNeighborPosition, symbolSeatAvailable) == symbolSeatOccupied:
            countOfOccupiedNeighbors += 1

    return countOfOccupiedNeighbors

def CountAvailableNeighboringSeatsForPart2(currentStateOfChart, seatPosition):

    relativeOffsetsForNeighbors = [
        Position(X=-1, Y=-1),
        Position(X=-1, Y=0),
        Position(X=-1, Y=1),
        Position(X=0, Y=-1),
        Position(X=0, Y=1),
        Position(X=1, Y=-1),
        Position(X=1, Y=0),
        Position(X=1, Y=1),
    ]

    countOfOccupiedNeighbors = 0
    for relativeOffset in relativeOffsetsForNeighbors:
        currentNeighborPosition = Position(seatPosition.X + relativeOffset.X, seatPosition.Y + relativeOffset.Y)
        currentRadius = 1
        while currentStateOfChart.get(currentNeighborPosition) == symbolSeatUnavailable:
            currentNeighborPosition = currentStateOfChart.get(
                Position(
                    currentNeighborPosition.X + (relativeOffset.X * currentRadius),
                    currentNeighborPosition.Y + (relativeOffset.Y * currentRadius),
                )
            )
            currentRadius += 1
        if currentStateOfChart.get(currentNeighborPosition) == symbolSeatOccupied: countOfOccupiedNeighbors += 1

    return countOfOccupiedNeighbors

with open((__file__.rstrip("puzzle.py")+"debuginput.txt"), 'r') as input_file:
    inp = input_file.read()
    lines = inp.splitlines()


symbolSeatUnavailable = "."
symbolSeatAvailable = "L"
symbolSeatOccupied = "#"

Position = namedtuple("Position", "X Y")

# initialStateOfChart = dict()
# for indexRow, row in enumerate(lines): # initial state
#     for indexColumn, column in enumerate(row):
#         currentPosition = Position(indexColumn, indexRow)
#         initialStateOfChart[currentPosition] = column
#
# currentStateOfChart = deepcopy(initialStateOfChart)
# nextStateOfChart = RunThroughSeatingChartForPart1(currentStateOfChart)
# while nextStateOfChart != currentStateOfChart:
#     currentStateOfChart = nextStateOfChart
#     nextStateOfChart = RunThroughSeatingChartForPart1(nextStateOfChart)
#
#
# countOfOccupiedSeatsPart1 = sum(1 for seat in currentStateOfChart.values() if seat == symbolSeatOccupied)
# print("Part One : {}".format(countOfOccupiedSeatsPart1))

initialStateOfChart = dict()
for indexRow, row in enumerate(lines): # initial state
    for indexColumn, column in enumerate(row):
        currentPosition = Position(indexColumn, indexRow)
        initialStateOfChart[currentPosition] = column

currentStateOfChart = deepcopy(initialStateOfChart)
nextStateOfChart = RunThroughSeatingChartForPart2(currentStateOfChart)
while nextStateOfChart != currentStateOfChart:
    currentStateOfChart = nextStateOfChart
    nextStateOfChart = RunThroughSeatingChartForPart2(nextStateOfChart)

countOfOccupiedSeatsPart2 = sum(1 for seat in currentStateOfChart.values() if seat == symbolSeatOccupied)
print("Part Two : {}".format(countOfOccupiedSeatsPart2))