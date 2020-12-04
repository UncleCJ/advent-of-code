# Advent of code Year 2020 Day 4 solution
# Author = BNAndras
# Date = December 2020
import re

with open((__file__.rstrip("puzzle.py") + "input.txt"), 'r') as input_file:
    input = input_file.read()
    lines = input.splitlines()
    lines.append("")

requiredFields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
optionalFields = {"cid"}
validEyeColors = ["amb", "brn", "gry", "grn", "hzl", "oth", "blu"]

counterValidPassports = 0
passportFields = []
for line in lines:
    distinctPassportFields = set(passportFields)
    if ((line == "") & (distinctPassportFields == requiredFields)): counterValidPassports += 1
    if (line == ""): passportFields = []
    segments = line.split(" ")
    for segment in segments:
        fieldName, *_ = segment.split(":")
        if (fieldName in requiredFields): passportFields.append(fieldName)

print("Part One : {}".format(counterValidPassports))

counterValidPassports = 0
passportFields = []
for line in lines:
    if (line == "" and set(passportFields) == requiredFields): counterValidPassports += 1
    if line == "": passportFields = []
    segments = [x for x in line.split(" ") if x]
    for segment in segments:
        fieldName, valueToValidate = segment.split(":")
        validationToggle = False
        try:
            yearToValidate = int(valueToValidate)
        except:
            pass
        if fieldName == "byr":
            if ((1920 <= yearToValidate) and (yearToValidate <= 2002)): validationToggle = True
        elif fieldName == "iyr":
            if ((2010 <= yearToValidate) and (yearToValidate <= 2020)): validationToggle = True
        elif fieldName == "eyr":
            if ((2020 <= yearToValidate) and (yearToValidate <= 2030)): validationToggle = True
        elif fieldName == "hgt":
            unit = valueToValidate[-2:]
            try:
                height = int(valueToValidate[:-2])
                if unit == "cm" & ((150 <= height) and (height <= 193)):
                    validationToggle = True
                elif unit == "in" & ((59 <= height) and (height <= 76)):
                    validationToggle = True
            except:
                pass
        elif fieldName == "hcl":
            regex = re.compile(r"^#[0-9a-f]{6}$")
            if re.match(regex, valueToValidate): validationToggle = True
        elif fieldName == "ecl":
            if valueToValidate in validEyeColors: validationToggle = True
        elif fieldName == "pid":
            regex = re.compile(r"^\d{9}$")
            if re.match(regex, valueToValidate): validationToggle = True
        if validationToggle: passportFields.append(fieldName)

print("Part Two : {}".format(counterValidPassports))
