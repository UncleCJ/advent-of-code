# Advent of code Year 2021 Day 6 solution
# Author = Joao Antunes
# Date = December 2021

ans = None
with open((__file__.rstrip("code1.py")+"input.txt"), 'r') as input_file:
    school = [int(val) for val in input_file.readline().split(",")]

days = 80

# print(school)
for day in range(1, days+1):
    offspring = []
    for i in range(len(school)):
        school[i] -= 1
        if school[i] == -1:
            school[i] = 6
            offspring.append(8)
    school.extend(offspring)
    # print(school)

print(len(school))

