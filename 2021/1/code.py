# Advent of code Year 2021 Day 1 solution
# Author = Joao Antunes
# Date = December 2021

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    numbers = [int(line) for line in input_file]

incs = 0
for i in range(len(numbers) - 1):
    if numbers[i] < numbers[i + 1]:
        incs += 1

print(f"Part One : {incs}")

incs = 0
sum0 = numbers[0] + numbers[1] + numbers[2]
sum1 = numbers[1] + numbers[2]
print(f"{sum0}: (N/A - no previous sum)")
for i in range(3, len(numbers)):
    sum1 += numbers[i]
    print(f"{sum1}: ", end="")
    if sum0 < sum1:
        incs += 1
        print(f"(increased)")
    elif sum0 == sum1:
        print(f"(no change)")
    else:
        print(f"(decreased)")
    sum0 = sum1
    sum1 -= numbers[i-2]

print(f"Part Two : {incs}")
