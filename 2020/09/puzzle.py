# Advent of code Year 2020 Day 9 solution
# Author = BNAndras
# Date = December 2020

from itertools import combinations

with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
    inp = input_file.read()
    numbers = [int(line) for line in inp.splitlines()]

def IsNumberNotValidForSequence(number, sequence):
    combinationSums = {sum(combination) for combination in combinations(sequence, 2)}
    return False if number in combinationSums else True

preambleLength = 25
firstNotValidNumber = 0

for position in range(preambleLength, len(numbers)):
    clippedSequence = numbers[(position - preambleLength) : position]
    if IsNumberNotValidForSequence(numbers[position], clippedSequence):
        firstNotValidNumber = numbers[position]
        break

print("Part One : {}".format(firstNotValidNumber))

targetInvalidNumber = firstNotValidNumber
encryptionWeakness = 0
for firstPosition in range(len(numbers)):
    accumulatorUpToTargetInvalidNumber = 0
    for secondPosition in range(firstPosition, len(numbers)):
        accumulatorUpToTargetInvalidNumber += numbers[secondPosition]
        if accumulatorUpToTargetInvalidNumber > targetInvalidNumber: break
        if accumulatorUpToTargetInvalidNumber == targetInvalidNumber:
            contiguousSequence = numbers[firstPosition : (secondPosition + 1)]
            encryptionWeakness = min(contiguousSequence) + max(contiguousSequence)
        if encryptionWeakness: break
    if encryptionWeakness: break


print("Part Two : {}".format(encryptionWeakness))