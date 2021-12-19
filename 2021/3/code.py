from collections import defaultdict

# Advent of code Year 2021 Day 3 solution
# Author = Joao Antunes
# Date = December 2021

ans = None
with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    lines = [line for line in input_file]

# The first parameter to check is the power consumption.
# The power consumption can then be found by multiplying the gamma rate by the epsilon_list rate.

# Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report.
bits = defaultdict(int)
max_bits = None
numbers = [] # for part2
for line in lines:
    number = []
    for i, val in enumerate(line):
        if max_bits is None:
            max_bits = len(line) - 1
        if val == "1":
            val = 1
            number.append(1)
        elif val == "0":
            val = -1
            number.append(0)
        else:
            break
        bits[i] += val
    numbers.append(number)

gamma_list = []
epsilon_list = []
for i in range(max_bits):
    if  bits[i] > 0:
        gamma_list.append("1")
        epsilon_list.append("0")
    else:
        gamma_list.append("0")
        epsilon_list.append("1")

gamma_binary = "".join(gamma_list)
gamma = int(gamma_binary, 2)

epsilon_binary = "".join(epsilon_list)
epsilon = int(epsilon_binary, 2)

print(f"Part One : {gamma * epsilon}")

# Next, you should verify the life support rating, which can be determined by multiplying the oxygen generator rating by the CO2 scrubber rating.

# start with the full list of binary numbers from your diagnostic report and consider just the first bit of those numbers. Then:
# Keep only numbers selected by the bit criteria for the type of rating value for which you are searching. Discard numbers which do not match the bit criteria.
# If you only have one number left, stop; this is the rating value for which you are searching.
# Otherwise, repeat the process, considering the next bit to the right.

# The bit criteria depends on which type of rating value you want to find:
# To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 1 in the position being considered.
# To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 0 in the position being considered.

def get_zeroes_and_ones(numbers, bit):
    zeroes = []
    ones = []
    for number in numbers:
        destination = ones if number[bit] == 1 else zeroes
        destination.append(number)
    return (zeroes, ones)

def oxygen_criteria(zeroes, ones):
    return ones if len(zeroes) <= len(ones) else zeroes

def co2_criteria(zeroes, ones):
    return zeroes if len(zeroes) <= len(ones) else ones

def bit_criteria(numbers, criteria):
    for i in range(max_bits):
        (zeroes, ones) = get_zeroes_and_ones(numbers, i)
        numbers = criteria(zeroes, ones)

        if len(numbers) == 1:
            break
    return numbers[0]


number = bit_criteria(numbers, oxygen_criteria)
oxygen_binary = "".join([str(n) for n in number])
oxygen = int(oxygen_binary, 2)

number = bit_criteria(numbers, co2_criteria)
co2_binary = "".join([str(n) for n in number])
co2 = int(co2_binary, 2)

print(f"Part Two : {oxygen * co2}")

