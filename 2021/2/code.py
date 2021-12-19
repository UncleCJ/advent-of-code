# Advent of code Year 2021 Day 2 solution
# Author = Joao Antunes
# Date = December 2021


# down X increases your aim by X units.
# up X decreases your aim by X units.
# forward X does two things:
# It increases your horizontal position by X units.
# It increases your depth by your aim multiplied by X.
with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    lines = [line.split() for line in input_file]
    lines = [(comm, int(arg)) for comm, arg in lines]

aim = horiz = depth = 0
for command, arg in lines:
    if command == "forward":
        horiz += arg
    elif command == "down":
        depth += arg
    elif command == "up":
        depth -= arg

print(f"Part One : {horiz*depth}")

aim = horiz = depth = 0
for command, arg in lines:
    if command == "forward":
        horiz += arg
        depth += arg * aim
    elif command == "down":
        aim += arg
    elif command == "up":
        aim -= arg

print(f"Part Two : {horiz*depth}")
