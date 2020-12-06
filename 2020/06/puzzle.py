# Advent of code Year 2020 Day 6 solution
# Author = BNAndras
# Date = December 2020

#from itertools import chain

with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
    inp = input_file.read()
    groups = inp.split("\n\n")


sum = 0
for group in groups:
    personalAnswers = [set(answers) for answers in group.split()]
    sum += len(set.union(*personalAnswers))
    #sum += len(set(chain.from_iterable(personalAnswers)))


print("Part One : {}".format(sum))

count = 0
for group in groups:
    personalAnswers = [set(answers) for answers in group.split()]
    count += len(set.intersection(*personalAnswers))

print("Part Two : {}".format(count))