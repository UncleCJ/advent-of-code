# Advent of code Year 2021 Day 7 solution
# Author = Joao Antunes
# Date = December 2021

with open((__file__.rstrip("code1.py")+"input.txt"), 'r') as input_file:
    line = input_file.readline().split(",")

crabs = [int(l) for l in line]
lo, hi = min(crabs), max(crabs)

fuel_min = float("+inf")
for target in range(lo, hi+1):
    fuel = sum(map(lambda x: abs(target-x), crabs))
    fuel_min = min(fuel_min, fuel)

print(fuel_min)
