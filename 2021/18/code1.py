import os, sys, copy, math
# Advent of code Year 2021 Day 18 solution
# Author = Joao Antunes
# Date = December 2021

input = [
    [[4,[3,[2,8]]],[[[8,5],4],[[3,5],[4,9]]]],
    [[[8,[6,8]],2],[4,[[1,0],[4,5]]]],
    [[4,3],[[[3,3],[1,8]],[[0,8],[5,8]]]],
    [[[8,[5,8]],[[8,7],[2,1]]],[3,[[0,3],1]]],
    [[9,[[9,2],3]],[3,[[9,7],[2,8]]]],
    [[[7,[0,0]],[[4,3],[6,3]]],[6,[4,5]]],
    [[[[4,2],[0,0]],[4,2]],[[[8,7],8],[[9,4],5]]],
    [[4,[1,[1,1]]],[[[0,6],8],[[7,5],[7,3]]]],
    [[[1,[9,9]],[4,3]],[[1,[5,8]],9]],
    [[2,[6,[6,7]]],[[6,[1,5]],8]],
    [4,[[[9,8],[1,3]],[7,[7,4]]]],
    [[[[2,6],8],2],[[[2,2],8],[[3,7],8]]],
    [[[[1,5],2],[[8,9],[8,3]]],[[[7,3],[1,1]],[[3,7],7]]],
    [[[4,4],[8,9]],[5,3]],
    [[[[1,4],[4,5]],9],[[2,8],0]],
    [[[[4,4],[7,3]],[[9,7],[3,9]]],[9,[5,[5,1]]]],
    [[5,[[5,9],6]],[[[5,9],[6,3]],1]],
    [[[[1,0],[1,6]],5],[1,9]],
    [[[[6,3],[7,2]],1],[[0,6],6]],
    [[[3,4],[4,0]],[[[6,4],[2,0]],[7,[7,2]]]],
    [[[[1,3],[9,6]],[[1,1],[9,3]]],[[3,8],[[9,5],2]]],
    [[[[9,4],6],5],[[[7,6],[2,3]],[6,6]]],
    [[6,[2,[0,7]]],[[3,0],[8,[1,9]]]],
    [[[6,0],[1,7]],[[[4,2],[5,7]],[[5,0],9]]],
    [[[7,[4,9]],0],[[5,[7,5]],[8,[5,1]]]],
    [[[[6,1],[8,0]],[3,[4,5]]],[[[8,3],4],[0,2]]],
    [[[[3,8],5],[4,8]],9],
    [[0,[7,[9,4]]],[2,2]],
    [[[[9,6],[4,0]],[1,1]],[3,[[3,6],8]]],
    [[[6,[3,3]],[[7,6],3]],[[[2,8],[0,7]],3]],
    [[[[3,2],[2,4]],[[8,7],7]],[[[0,2],[1,3]],[8,3]]],
    [[[[4,2],[6,8]],6],[[[2,1],[0,3]],[[6,6],[5,6]]]],
    [[[[9,0],[1,7]],[[0,3],1]],[[0,[4,3]],7]],
    [[[1,[1,4]],1],[[[8,1],9],[[7,1],[7,2]]]],
    [2,[2,[[4,2],2]]],
    [6,0],
    [[[[9,7],7],[2,3]],[[8,[9,4]],[2,3]]],
    [[[[4,5],8],6],[5,9]],
    [[[5,[6,7]],[[1,9],[8,6]]],7],
    [7,[[0,5],4]],
    [[[2,4],[2,[1,9]]],[8,[5,6]]],
    [3,[[6,[4,8]],[[3,0],9]]],
    [[[[4,4],[0,5]],[7,3]],[1,[4,5]]],
    [8,[[2,[1,1]],9]],
    [[[[5,6],[5,1]],[[7,6],[8,8]]],[2,[[2,1],[3,1]]]],
    [[0,[2,[4,6]]],[[[6,0],[3,9]],[0,[1,6]]]],
    [[[6,[9,5]],[0,[9,4]]],0],
    [[[[5,6],[7,8]],[7,[8,8]]],[[7,[4,7]],[[3,9],7]]],
    [1,0],
    [[7,2],[9,[3,0]]],
    [[[[4,8],9],[1,[0,4]]],[[[5,2],0],8]],
    [[[9,[2,5]],[2,[5,8]]],[1,6]],
    [[[[0,5],1],[0,4]],7],
    [8,[5,9]],
    [[[[8,8],[4,8]],[[7,8],7]],[[0,4],8]],
    [[[0,6],[9,6]],2],
    [[[[2,5],[0,6]],8],[[8,9],1]],
    [[[0,9],[1,[1,2]]],[[[4,1],6],7]],
    [[[[5,7],[4,6]],[[6,3],[8,2]]],[[[2,5],[0,9]],[5,1]]],
    [[[5,0],[[4,5],[6,2]]],[[[1,7],[3,0]],[[8,2],[6,1]]]],
    [[[[8,9],9],[9,0]],[4,[[7,2],9]]],
    [[[[2,3],[0,5]],[8,8]],[9,[[9,1],8]]],
    [[[5,9],[0,[6,2]]],[[3,2],[[1,2],[9,5]]]],
    [[[5,2],[8,[0,0]]],[[6,9],[4,[8,4]]]],
    [7,3],
    [[[6,4],[[0,4],7]],[[5,[0,3]],[8,7]]],
    [[1,2],[[3,[5,9]],0]],
    [[[6,9],[3,0]],[[[2,1],4],6]],
    [[[8,[7,9]],1],[[[2,2],8],8]],
    [[[0,1],[6,[3,3]]],5],
    [[[[3,9],0],7],2],
    [[[3,0],[1,[7,6]]],0],
    [[[[3,5],3],8],[[[1,2],[8,8]],[[1,6],[8,1]]]],
    [[[9,7],[[1,3],[6,9]]],6],
    [[[[1,8],1],[[6,4],[1,8]]],[[[1,7],[5,9]],[[7,0],0]]],
    [[[1,[9,3]],[4,0]],7],
    [[5,[9,6]],[[4,[0,8]],2]],
    [3,[[1,0],[0,2]]],
    [[[3,1],[2,7]],[[4,4],5]],
    [[8,6],[[4,[5,9]],[[3,7],9]]],
    [[[3,2],2],[[3,9],8]],
    [[[[4,5],[4,5]],[[0,2],[7,0]]],[[1,4],2]],
    [7,[[8,[3,8]],[[5,6],4]]],
    [[[[2,8],[2,2]],[[4,4],0]],[[2,[8,0]],2]],
    [4,[[[8,8],0],[[1,8],[4,6]]]],
    [[[5,[1,2]],7],9],
    [[9,[[0,0],9]],[[5,[1,3]],[4,[4,7]]]],
    [[3,4],[8,[2,[9,6]]]],
    [[[[3,0],1],[[7,6],[5,2]]],[[[9,9],[9,2]],[0,[2,2]]]],
    [[[[0,8],[6,1]],[2,0]],[6,[[8,8],[9,1]]]],
    [[[5,[1,9]],6],6],
    [[[3,5],[[9,9],[2,2]]],[[1,0],4]],
    [[4,0],[2,[[8,8],[5,4]]]],
    [[6,1],5],
    [[[2,[3,7]],0],[1,5]],
    [[[[5,9],[5,3]],[6,2]],[[7,9],4]],
    [[[5,[0,9]],[[5,6],3]],[3,[7,8]]],
    [8,[[[4,6],5],[0,2]]],
    [[[0,[6,2]],[6,[6,6]]],[[3,1],6]],
    [1,[[6,4],[0,6]]],
]

test = [
    [[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]],
    [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]],
    [[2, [[0, 8], [3, 4]]], [[[6, 7], 1], [7, [1, 6]]]],
    [[[[2, 4], 7], [6, [0, 5]]], [[[6, 8], [2, 8]], [[2, 1], [4, 5]]]],
    [7, [5, [[3, 8], [1, 4]]]],
    [[2, [2, 2]], [8, [8, 1]]],
    [2, 9],
    [1, [[[9, 3], 9], [[9, 0], [0, 7]]]],
    [[[5, [7, 4]], 7], 1],
    [[[[4, 2], 2], 6], [8, 7]],
]

def is_number(snailfish):
    return type(snailfish) is int

def explode(snailfish):
    last,add_to_next = None, None
    mode = 0
    def df(snailfish, level=1):
        nonlocal last, add_to_next, mode
        if mode == 0 and level == 5:
            print(f"explode {snailfish}")
            # explode
            if last:
                ref, j = last
                ref[j] += snailfish[0]
            add_to_next = snailfish[1]
            print(f"add to next: {add_to_next}")
            return 1

        for idx in (0, 1):
            if is_number(snailfish[idx]):
                if mode == 2 and add_to_next is not None:
                    snailfish[idx] += add_to_next
                    return 3 # finished
                else:
                    last = (snailfish, idx)
            else:
                mode = df(snailfish[idx], level + 1)
                if mode == 1:
                    snailfish[idx] = 0
                    mode = 2
                elif mode == 3:
                    return 3
        return mode
    df(snailfish)
    return add_to_next is not None


def split(snailfish):
    if is_number(snailfish):
        if snailfish >= 10:
            print(f"split: {snailfish}")
            return True, [math.floor(snailfish / 2), math.ceil(snailfish / 2)]
    else:
        status, left = split(snailfish[0])
        if status:
            if left:
                snailfish[0] = left
            return status, []
        status, right = split(snailfish[1])
        if status:
            if right:
                snailfish[1] = right
            return status, []
    return False, []


# To check whether it's the right answer, the snailfish teacher
# only checks the magnitude of the final sum.
# The magnitude of a pair is 3 times the magnitude of its left element
# plus 2 times the magnitude of its right element.
# The magnitude of a regular number is just that number.
def magnitude(snailfish):
    if is_number(snailfish):
        return snailfish
    else:
        return 3 * magnitude(snailfish[0]) + 2 * magnitude(snailfish[1])

# tests = [
#     # ([[[[[9,8],1],2],3],4], [[[[0,9],2],3],4]),
#     # ([7,[6,[5,[4,[3,2]]]]], [7,[6,[5,[7,0]]]]),
#     # ([[6,[5,[4,[3,2]]]],1], [[6,[5,[7,0]]],3]),
#     # ([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]], [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]),
#     # ([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]], [[3,[2,[8,0]]],[9,[5,[7,0]]]]),
#     # ([[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]], [[[[0,7],4],[[7,8],[6,0]]],[8,1]]),
#     # ([[[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]], [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]],
#     # [[[[4, 0], [5, 0]], [[[4, 5], [2, 6]], [9, 5]]],      [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]]),

#     ([[[[4, 0], [5, 0]], [[[4, 5], [2, 6]], [9, 5]]], [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]],
#     [[[[4, 0], [5, 4]], [[ 0, [7, 6]], [9, 5]]],     [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]]),

#     ([[[[4, 0], [5, 4]], [[ 0, [7, 6]], [9, 5]]], [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]],
#     [[[[4, 0], [5, 4]], [[ 7,  0], [15, 5]]],    [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]]),

#     ([[[[4, 0], [5, 4]], [[ 7,  0], [15, 5]]], [7,  [[[3, 7],  [4, 3]], [[6, 3], [8, 8]]]]],
#     [[[[4, 0], [5, 4]], [[ 7,  0], [15, 5]]], [10, [[ 0,     [11, 3]], [[6, 3], [8, 8]]]]]),

#     ([[[[4, 0], [5, 4]], [[ 7,  0], [15, 5]]], [10, [[ 0, [11, 3]], [[6, 3], [8, 8]]]]],
#     [[[[4, 0], [5, 4]], [[ 7,  0], [15, 5]]], [10, [[ 11, 0 ], [[9, 3], [8, 8]]]]]),

#     ([[[[4, 0], [5, 4]], [[ 7,  0], [15, 5]]], [10, [[ 11, 0], [[9, 3],  [8, 8]]]]],
#     [[[[4, 0], [5, 4]], [[ 7,  0], [15, 5]]], [10, [[ 11, 9], [0,      [11, 8]]]]]),

#     ([[[[4, 0], [5, 4]], [[ 7,  0], [15, 5]]], [10, [[ 11, 9], [0, [11, 8]]]]],
#     [[[[4, 0], [5, 4]], [[ 7,  0], [15, 5]]], [10, [[ 11, 9], [11, 0]]]]),
# ]
# for input, expected in tests:
#     received = copy.deepcopy(input)
#     explode(received)
#     assert received == expected, f"\n   input: {input}\nexpected: {expected}\nreceived: {received}"
#     print("OK")


def reduce(snailfish):
    print(f"Adding: {snailfish}")
    modified = True
    while modified:
        modified = False
        print(snailfish)
        print("######### EXPLODE")
        while explode(snailfish) > 0:
            print("exploded")
            print(snailfish)
            modified = True

        print("######### SPLIT")
        modified = split(snailfish)[0] or modified

    print("done")
    print(snailfish)


# tests = [
#     ([[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]], [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]])
# ]
# for input, expected in tests:
#     received = copy.deepcopy(input)
#     reduce(received)
#     assert received == expected, f"\n   input: {input}\nexpected: {expected}\nreceived: {received}"
#     print("OK")




data = input

snailfish = data[0]
print(snailfish)
reduce(snailfish)
for i in range(1, len(data)):
    reduce(data[i])
    snailfish = [snailfish, data[i]]
    reduce(snailfish)
    print(snailfish)
print(snailfish)
print(f"magnitude: {magnitude(snailfish)}")
