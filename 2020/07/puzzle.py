# Advent of code Year 2020 Day 7 solution
# Author = BNAndras
# Date = December 2020

from collections import defaultdict
from re import findall, search

with open((__file__.rstrip("puzzle.py")+"input.txt"), 'r') as input_file:
    inp = input_file.read()
    lines = inp.splitlines()

def CountUpParentBags(bagName):
    uniqueParentBags = set().union(parentsOf[bagName])
    for bagName in parentsOf[bagName]:
        uniqueParentBags = uniqueParentBags.union(CountUpParentBags(bagName))
    return uniqueParentBags

def CountUpChildrenInside(bagName):
    countOfChildrenInsideCurrentBag = 0
    for innerBagName, bagCount in childrenOf[bagName].items():
        countOfChildrenInsideCurrentBag += bagCount
        countOfChildrenInsideCurrentBag += bagCount * CountUpChildrenInside(innerBagName)
    return countOfChildrenInsideCurrentBag


childrenOf = defaultdict(dict)
parentsOf = defaultdict(list)

for line in lines:
    parentName = search(r"^[\w]+\s+[\w]+", line).group()
    bagContents = findall(r"(\d+)[\s](\w+\s\w+)",line)
    for count, childName in bagContents:
        childrenOf[parentName][childName] = int(count)
        parentsOf[childName].append(parentName)

print(
    "Part One : {}".format
    (
        len(CountUpParentBags("shiny gold"))
    )
)

print(
    "Part Two : {}".format
    (
        CountUpChildrenInside("shiny gold")
    )
)