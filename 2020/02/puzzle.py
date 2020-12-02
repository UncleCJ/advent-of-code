# Advent of code Year 2020 Day 2 solution
# Author = BNAndras
# Date = December 2020

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    lines = input_file.read().splitlines()

counter = 0
for line in lines:
    numbers, character, password = line.split()
    low, high = map(int, numbers.split("-"))
    # low = int(numbers[0])
    # high = int(numbers[-1])
    character = character[:-1]
    if (low <= password.count(character)) & (password.count(character) <= high): counter += 1


print("Part One : "+ str(counter))

counter = 0
for line in lines:
    numbers, character, password = line.split()
    firstPosition, secondPosition = map(int, numbers.split("-"))
    character = character[0]
    if (password[firstPosition - 1] == character) | (password[secondPosition - 1] == character): counter += 1

print("Part Two : "+ str(counter))