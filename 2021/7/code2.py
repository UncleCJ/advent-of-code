from functools import cache

# Advent of code Year 2021 Day 7 solution
# Author = Joao Antunes
# Date = December 2021

with open((__file__.rstrip("code2.py")+"test.txt"), 'r') as input_file:
    line = input_file.readline().split(",")

crabs = [int(l) for l in line]
lo, hi = min(crabs), max(crabs)

# Causes: RecursionError: maximum recursion depth exceeded.
# Had to use bottom-up DP w/ tabulation instead.
# @cache
# def cost(distance):
#     if distance == 0:
#         return distance
#     return distance + cost(distance - 1)
cost = [0] * (hi+1)
for i in range(1, hi+1):
    cost[i] = i + cost[i-1]

fuel_min = float("+inf")
for target in range(lo, hi+1):
    fuel = sum(map(lambda x: cost[abs(target - x)], crabs))
    fuel_min = min(fuel_min, fuel)

print(fuel_min)
