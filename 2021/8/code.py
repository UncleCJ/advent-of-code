import sys
from collections import defaultdict
from itertools import permutations

# Advent of code Year 2021 Day 8 solution
# Author = Joao Antunes
# Date = December 2021

lines = []
# optionally use input file as argument: python 2021/8/code.py custom_test.txt
with open(__file__.rstrip("code.py") + "input.txt", 'r') as input_file:
    for line in input_file:
        pattern, output = line.split(" | ")
        lines.append((pattern.split(), output.split()))

NUMBERS = {
    "ABCEFG": 0,
    "CF": 1,
    "ACDEG": 2,
    "ACDFG": 3,
    "BCDF": 4,
    "ABDFG": 5,
    "ABDEFG": 6,
    "ACF": 7,
    "ABCDEFG": 8,
    "ABCDFG": 9,
}

SEGMENTS = {v: set(k) for k, v in NUMBERS.items()}
# same as: { 0: set("ABCEFG"), 1: set("CF"), ...}

MAP_COUNT_OUTPUT = defaultdict(list)
for output, segment in SEGMENTS.items():
    count = len(segment)
    MAP_COUNT_OUTPUT[count].append(output)
# same as: { 2: [1], 3: [7], 4: [4], 7: [8], 5: [2, 3, 5], 6: [0, 6, 9] }

# Use the order of the letters to generate a dictionary of the type:
# dictionary['a'] = 'D', which is a segment 'a' is interpreted as 'D'
ALPHABET_ORIGINAL = list("ABCDEFG") # original segments
ALPHABET_MIXED_UP = list("abcdefg") # mixed-up segments in lowercase
ALPHABET_PERMUTATIONS = list(permutations(ALPHABET_MIXED_UP))
def generateDictionary(permutation):
    dictionary = {}
    for i, letter in enumerate(permutation):
        dictionary[letter] = ALPHABET_ORIGINAL[i]
    return frozenset(dictionary.items())

ALL_DICTIONARIES = set(map(lambda x: generateDictionary(x), ALPHABET_PERMUTATIONS))


def translate(dictionary, pattern):
    number_list = []
    for p in pattern:
        number_list.append(dictionary[p])
    number_str = "".join(sorted(number_list))
    if number_str in NUMBERS:
        return NUMBERS[number_str]
    return None



def isValid(dictionary, keys, set_values):
    # return true if every k:v for all keys and values matches the dictionary
    for key in keys:
        val = dictionary[key]
        if val not in set_values:
            return False
    return True

ans = 0
for patterns, output in lines:

    # patterns-to-segments reset at each new line
    dictionaries = ALL_DICTIONARIES
    while len(dictionaries) > 1:
        for pattern in patterns:
            count = len(pattern)
            possible_outputs = MAP_COUNT_OUTPUT[count]

            all_valid_dictionaries = set()
            for possible_output in possible_outputs:
                set_values = SEGMENTS[possible_output]
                valid_dictionaries = set(filter(lambda d: isValid(dict(d), pattern, set_values), dictionaries))
                all_valid_dictionaries.update(valid_dictionaries)
            dictionaries = all_valid_dictionaries
    dictionary = dict(next(iter(dictionaries)))
    # print(f"only one possible dictionary left: {dictionary}")

    res = 0
    for pattern in output:
        number = translate(dictionary, pattern)
        if number is None:
            print("ERROR")
        print(f"{pattern} => {number}")
        res *= 10
        res += number

    ans += res

print(f"DONE: {ans}")
