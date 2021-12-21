import os, sys
from itertools import product
from functools import cache
from collections import Counter
# Advent of code Year 2021 Day 21 solution
# Author = Joao Antunes
# Date = December 2021
DIRAC_DICE = Counter(list(sum(die) for die in product([1,2,3], repeat=3)))

@cache
def backtrack(player0, player1, i):
    if player0[1] >= 21:
        return [1, 0]
    if player1[1] >= 21:
        return [0, 1]

    i = (1 + i) % 2
    player = player0 if i == 0 else player1

    wins = [0, 0]
    for total, count in DIRAC_DICE.items():
        new_position = (total + player[0] - 1) % 10 + 1  # 0..9 + 1
        new_score = player[1] + new_position
        if i == 0:
            w = backtrack((new_position, new_score), player1, i)
        else:
            w = backtrack(player0, (new_position, new_score), i)

        for j in range(2):
            wins[j] += count * w[j]

    return wins

wins = backtrack((8, 0), (4, 0), 1)


print(max(wins))
