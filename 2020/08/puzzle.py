# Advent of code Year 2020 Day 8 solution
# Author = BNAndras
# Date = December 2020

from copy import deepcopy

with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
    inp = input_file.read()
    lines = inp.splitlines()

def RunThroughBootCodeAndReturnAccumulatorP1(lines):
    accumulator = 0
    currentPosition = 0
    seenPositions = set()
    while currentPosition not in seenPositions:
        accumulator, currentPosition = RunThroughPositions(accumulator, currentPosition, lines, seenPositions)
    return accumulator

def RunThroughBootCodeAndReturnAccumulatorP2(lines):
    accumulator = 0
    currentPosition = 0
    seenPositions = set()
    while currentPosition not in seenPositions:
        if currentPosition >= len(lines): return accumulator
        accumulator, currentPosition = RunThroughPositions(accumulator, currentPosition, lines, seenPositions)
    return 0


def RunThroughPositions(accumulator, currentPosition, lines, seenPositions):
    seenPositions.add(currentPosition)
    currentLine = lines[currentPosition % len(lines)]
    instruction, argument = currentLine.split()
    argument = int(argument)
    if instruction == 'acc':
        accumulator += argument
    elif instruction == 'jmp':
        currentPosition += argument - 1
    elif instruction == "nop":
        pass
    currentPosition += 1
    return accumulator, currentPosition


accumulator = RunThroughBootCodeAndReturnAccumulatorP1(lines)
print("Part One : {}".format(accumulator))

for i in range(len(lines)):
    copiedLines = deepcopy(lines)
    if copiedLines[i].startswith("nop"):
        copiedLines[i] = copiedLines[i].replace("nop", "jmp")
    elif copiedLines[i].startswith("jmp"):
        copiedLines[i] = copiedLines[i].replace("jmp", "nop")
    accumulator = RunThroughBootCodeAndReturnAccumulatorP2(copiedLines)
    if accumulator: print("Part Two : {}".format(accumulator))