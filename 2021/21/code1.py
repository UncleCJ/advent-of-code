import os, sys
# Advent of code Year 2021 Day 21 solution
# Author = Joao Antunes
# Date = December 2021

next_roll = 1
def roll():
    global next_roll
    val = next_roll
    next_roll += 1
    if next_roll == 101:
        next_roll = 1
    return val

players = [8, 4]
scores = [0, 0]
rolls = 0
while scores[0] < 1000 and scores[1] < 1000:
    for i in range(len(players)):
        die = 0
        for _ in range(3):
            die += roll()
        rolls += 3
        players[i] = (die + players[i]-1) % 10 + 1 # 0..9 + 1
        scores[i] += players[i]
        if scores[i] >= 1000:
            break

print(min(scores) * rolls)
