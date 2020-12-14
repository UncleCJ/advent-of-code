# Advent of code Year 2020 Day 11 solution
# Author = BNAndras
# Date = December 2020

from collections import namedtuple
from copy import deepcopy

def RunThroughSeatingChart(currentStateOfChart):
    workingCopyOfChart = deepcopy(currentStateOfChart)
    for currentSeat in workingCopyOfChart:
        if currentSeat == symbolSeatUnavailable: continue
        countOfOccupiedNeighbors = CountAvailableNeighboringSeats(currentStateOfChart, currentSeat)
        if workingCopyOfChart[currentSeat] == symbolSeatAvailable and not countOfOccupiedNeighbors:
            workingCopyOfChart[currentSeat] = symbolSeatOccupied
        elif workingCopyOfChart[currentSeat] == symbolSeatOccupied and countOfOccupiedNeighbors >= 4:
            workingCopyOfChart[currentSeat] = symbolSeatAvailable
    return workingCopyOfChart

def CountAvailableNeighboringSeats(currentStateOfChart, seatPosition):
    countOfOccupiedNeighbors = 0
    for relativeOffset in relativeOffsetsForNeighbors:
        currentNeighborPosition = Position(seatPosition.X + relativeOffset.X, seatPosition.Y + relativeOffset.Y)
        if currentStateOfChart.get(currentNeighborPosition, symbolSeatAvailable) == symbolSeatOccupied: countOfOccupiedNeighbors += 1
    return countOfOccupiedNeighbors

with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
    inp = input_file.read()
    lines = inp.splitlines()


symbolSeatUnavailable = "."
symbolSeatAvailable = "L"
symbolSeatOccupied = "#"

Position = namedtuple("Position", "X Y")
relativeOffsetsForNeighbors = [
    Position(X=-1,Y=-1),
    Position(X=-1,Y=0),
    Position(X=-1,Y=1),
    Position(X=0,Y=-1),
    Position(X=0,Y=1),
    Position(X=1,Y=-1),
    Position(X=1,Y=0),
    Position(X=1,Y=1),
]

initialStateOfChart = dict()
for indexRow, row in enumerate(lines): # initial state
    for indexColumn, column in enumerate(row):
        currentPosition = Position(indexColumn, indexRow)
        initialStateOfChart[currentPosition] = column

currentStateOfChart = deepcopy(initialStateOfChart)
nextStateOfChart = RunThroughSeatingChart(deepcopy(currentStateOfChart))
while nextStateOfChart != currentStateOfChart:
    currentStateOfChart = nextStateOfChart
    nextStateOfChart = RunThroughSeatingChart(nextStateOfChart)


countOfOccupiedSeats = sum(1 for seat in currentStateOfChart.values() if seat == symbolSeatOccupied)
print("Part One : {}".format(countOfOccupiedSeats))


#print("Part Two : {}".format())