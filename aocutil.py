import itertools
from collections import defaultdict
from collections.abc import MutableMapping
from enum import Enum
from multiset import Multiset
import networkx as nx
import numpy as np
import re


def guess_input(raw):
    """Prints summary information about input.txt"""
    lines = raw.splitlines()
    print(f"# lines: {len(lines)}")
    line_lengths = set(filter(lambda x: x > 0, [len(line) for line in lines]))
    print(f"Line length range: {min(line_lengths)} to {max(line_lengths)}")
    print(f"# chars: {len(raw)}")
    double_newline = len(raw.split("\n\n")) - 1
    print(f"# double newlines: {double_newline}")
    whitespace, tabs = False, False
    seen = []
    for ch in raw:
        if ch == '\n':
            continue
        if ch == '\t':
            tabs = True
        elif ch.isspace():
            whitespace = True
        elif ch not in seen:
            seen.append(ch)
    print(f"Contains tabs: {tabs}")
    print(f"Contains whitespace: {whitespace}")
    print(f"Chars: {''.join(sorted(seen))}")
    ints = list(extract_ints(raw, negative=True))
    print(f"# Ints: {len(ints)}")
    if len(ints) > 0:
        print(f"Int range: {min(ints)} to {max(ints)}")
    ms = Multiset()
    for word in raw.split():
        if word.isnumeric():
            continue
        ms.add(word)
    common = sorted(ms.items(), key=by_index(1), reverse=True)
    print(f"Most common words: {common}")
    print()


# From https://github.com/salt-die/Advent-of-Code/blob/master/2020/aoc_helper/__init__.py
def extract_ints(raw, negative=False):
    """Utility function to extract all integers from some string."""
    regex = r'(-?\d+)' if negative else r'(\d+)'
    return map(int, re.findall(regex, raw))


def sorted_with_index(iterable, reverse=False):
    """Sorts a list while keeping track of the original index
    Returns a list of (i, x) where i = index and x = value"""
    return sorted([(i, iterable[i]) for i in enumerate(iterable)], key=by_index(1), reverse=reverse)


def neq(x):
    """Function to filter items that are not equal to x"""
    return lambda item: item != x


def by_index(index):
    """Function to pick a specific index as the key of a tuple"""
    return lambda tup: tup[index]


def invert_dict(dic):
    """Inverts a one-to-one dictionary"""
    return {v: k for k, v in dic.items()}


def flatten(iterable):
    """Flattens a one-layer deep list of lists"""
    return list(itertools.chain.from_iterable(iterable))


def manhattan(coord1, coord2):
    """Gets the manhattan distance between two points"""
    if len(coord1) != len(coord2):
        raise IndexError("coord1 and coord2 are different lengths!")
    return sum(sum(abs(c) for c in coord) for coord in (coord1, coord2))


def manhattan_origin(*coords, dim=3):
    """Sums the manhattan distance of each point from the origin.
    Returns the total distance, then a tuple of the distance in each direction.
    If no coords are specified, a zero distance and a tuple with dim zeroes is returned."""
    if len(coords) == 0:
        return 0, (0,) * dim
    dist = sum(sum(c for c in coord) for coord in coords)
    cardinals = tuple(sum(abs(coord[i]) for coord in coords) for i in range(len(coords[0])))
    return dist, cardinals


def matching(items):
    G = nx.from_dict_of_lists(items)
    return tuple((k, v) for k, v in nx.bipartite.maximum_matching(G, top_nodes=items).items() if k in items)


class Direction(bytes, Enum):
    """Direction helper class, 0 is up, CW"""
    def __new__(cls, value, cardinal):
        obj = bytes.__new__(cls)
        obj._value_ = value
        obj.cardinal = cardinal
        return obj
    UP = (0, (0, 1))
    RIGHT = (1, (1, 0))
    DOWN = (2, (0, -1))
    LEFT = (3, (-1, 0))

    @staticmethod
    def from_standard(n):
        """Convert from 0 is right, CCW"""
        return Direction((1 - n) % 4)

    def to_standard(self):
        """Convert to 0 is right, CCW"""
        return (1 - self._value_) % 4

    @property
    def x(self):
        return self.cardinal[0]

    @property
    def y(self):
        return self.cardinal[1]

    def add_to(self, x, y, mult=1):
        """Moves mult steps in this direction and adds it to x,y"""
        return x + self.x * mult, y + self.y * mult

    def __rshift__(self, other):
        return self.rotate_cw(other)

    def rotate_cw(self, n=1):
        """Get this direction rotated clockwise n times"""
        return Direction((self._value_ + n) % 4)

    def __lshift__(self, other):
        return self.rotate_ccw(other)

    def rotate_ccw(self, n=1):
        """Get this direction rotated counterclockwise n times"""
        return Direction((self._value_ - n) % 4)

    def __neg__(self):
        return self.invert()

    def __invert__(self):
        return self.invert()

    def invert(self):
        """Get the opposite of this direction"""
        return self.rotate_cw(2)


class Particle:
    def __init__(self, dim, p=None, v=None, a=None):
        self.dim = dim
        self.p = np.zeros(dim) if p is None else p
        self.v = np.zeros(dim) if v is None else v
        self.a = np.zeros(dim) if a is None else a

    @staticmethod
    def from_existing(other):
        return Particle(other.dim, other.p, other.v, other.a)

    def __add__(self, other):
        if self.dim != other.dim:
            raise ValueError
        return Particle(self.dim, self.p + other.p, self.v + other.v, self.a + other.a)

    def __neg__(self):
        return Particle(self.dim, -self.p, -self.v, -self.a)

    def __str__(self):
        return f"<Particle{self.dim}D p={self.p}, v={self.v}, a={self.a}>"

    def tick(self, n=1):
        for _ in range(n):
            self.v += self.a
            self.p += self.v


class Multimap(MutableMapping):
    dic = defaultdict(list)

    def __len__(self):
        return len(self.dic)

    def __iter__(self):
        return iter(self.dic)

    def __getitem__(self, k):
        return self.dic[k]

    def __setitem__(self, key, value):
        self.dic[key].append(value)

    def __delitem__(self, key):
        del self.dic[key]

    def __str__(self):
        return str(self.dic)

    def pop(self, key, default=None):
        if key in self.dic:
            popped = self.dic[key].pop()
            if len(self.dic[key]) == 0:
                del self.dic[key]
            return popped
        if default is None:
            raise KeyError
        return default

    def popitem(self):
        if len(self.dic) == 0:
            raise KeyError
        k, v_list = list(self.dic.items())[-1]
        v = v_list.pop()
        if len(v_list) == 0:
            del self.dic[k]
        return k, v

    def put_values(self, key, *values):
        for v in values:
            self[key] = v

    def remove(self, key, value):
        if value in self[key]:
            self[key].remove(value)
            if len(self[key]) == 0:
                del self[key]
            return True
        return False

    def remove_values(self, key, *values):
        for v in values:
            self.remove(key, v)


def off_by_one(n):
    """Sometimes guessing works"""
    return n - 1, n, n + 1
