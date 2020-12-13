# Advent of code Year 2020 Day 12 solution
# Author = BNAndras
# Date = December 2020

from collections import namedtuple

with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
    inp = input_file.read()
    Movement = namedtuple("Movement", "direction amount")
    movements = [Movement(x[:1], int(x[1:])) for x in inp.splitlines()]

Position = namedtuple("Position", "X Y")
currentShipPosition = Position(0, 0)

currentGeographicDirection = 90 # east
for movement in movements:
    if movement.direction == "F":
        currentGeographicDirection = currentGeographicDirection % 360
        if currentGeographicDirection == 0: movement = Movement("N", movement.amount)
        elif currentGeographicDirection == 90: movement = Movement("E", movement.amount)
        elif currentGeographicDirection == 180: movement = Movement("S", movement.amount)
        elif currentGeographicDirection == 270: movement = Movement("W", movement.amount)
    if movement.direction == "N":
        currentShipPosition = Position(currentShipPosition.X, currentShipPosition.Y + movement.amount)
    elif movement.direction == "S":
        currentShipPosition = Position(currentShipPosition.X, currentShipPosition.Y - movement.amount)
    elif movement.direction == "E":
        currentShipPosition = Position(currentShipPosition.X + movement.amount, currentShipPosition.Y)
    elif movement.direction == "W":
        currentShipPosition = Position(currentShipPosition.X - movement.amount, currentShipPosition.Y)
    elif movement.direction == "R": currentGeographicDirection += movement.amount
    elif movement.direction == "L": currentGeographicDirection -= movement.amount

manhattanDistanceForShipPart1 = abs(currentShipPosition.X) + abs(currentShipPosition.Y)

print("Part One : {}".format(manhattanDistanceForShipPart1))

currentWaypointPosition = Position(10, 1)
currentShipPosition = Position(0, 0)
for movement in movements:
    if movement.direction == "F":
        currentShipPosition = Position(
            currentShipPosition.X + (currentWaypointPosition.X * movement.amount),
            currentShipPosition.Y + (currentWaypointPosition.Y * movement.amount)
        )
    elif movement.direction == "N":
        currentWaypointPosition = Position(currentWaypointPosition.X, currentWaypointPosition.Y + movement.amount)
    elif movement.direction == "S":
        currentWaypointPosition = Position(currentWaypointPosition.X, currentWaypointPosition.Y - movement.amount)
    elif movement.direction == "E":
        currentWaypointPosition = Position(currentWaypointPosition.X + movement.amount, currentWaypointPosition.Y)
    elif movement.direction == "W":
        currentWaypointPosition = Position(currentWaypointPosition.X - movement.amount, currentWaypointPosition.Y)
    elif movement.direction == "R":
        while movement.amount:
            movement = Movement(movement.direction, movement.amount - 90)
            currentWaypointPosition = Position(X = -currentWaypointPosition.Y, Y = currentWaypointPosition.X)
    elif movement.direction == "L":
        while movement.amount:
            movement = Movement(movement.direction, movement.amount - 90)
            currentWaypointPosition = Position(X = currentWaypointPosition.Y, Y = -currentWaypointPosition.X)

manhattanDistanceForShipPart2 = abs(currentShipPosition.X) + abs(currentShipPosition.Y)
print("Part Two : {}".format(manhattanDistanceForShipPart2))