import os, sys
from operator import mul
from functools import reduce
# Advent of code Year 2021 Day 16 solution
# Author = Joao Antunes
# Date = December 2021

class Packet:
    versions = 0
    op = {
        0: lambda x: sum(x),
        1: lambda x: reduce(mul, x),
        2: lambda x: min(x),
        3: lambda x: max(x),
        5: lambda x: int(x[0] > x[1]),
        6: lambda x: int(x[0] < x[1]),
        7: lambda x: int(x[0] == x[1]),
        # 4: lambda x: x[0],
    }
    op_str = {
        0: "-sum",
        1: "-mul",
        2: "-min",
        3: "-max",
        5: "--gt",
        6: "--lt",
        7: "--eq",
        # 4: lambda x: x[0],
    }

    def __init__(self, header):
        self.v = int(header[0:3], 2)
        self.t = int(header[3:6], 2)
        self.inner = []

    def versions(self):
        versions = [self.v]
        if self.t == 4:
            return versions

        for subpacket in self.inner:
            versions.extend(subpacket.versions())
        return versions

    def calculate(self, tab=0):
        if self.t == 4:
            return self.inner[0]

        values = [subpacket.calculate(tab+1) for subpacket in self.inner]
        # print(f"{tab*' '}{Packet.op_str[self.t]}: {values}")
        return Packet.op[self.t](values)

    @classmethod
    def parse(cls, binary, start_at):
        i = start_at
        header = binary[i:i+6]
        outer = Packet(header)
        i += 6

        # literal
        if outer.t == 4:
            data = []
            type = '1'
            while type == '1':
                type = binary[i]
                chunk = binary[i+1:i+5]
                data.append(chunk)
                i += 5
            literal = int("".join(data), 2)
            outer.inner.append(literal)

        # operator
        else:
            remaining_len = None
            remaining_count = None
            length_id = binary[i]
            i += 1
            if length_id == '0':
                remaining_len = int(binary[i:i+15], 2)
                i += 15
            else:
                remaining_count = int(binary[i:i+11], 2)
                i += 11

            while remaining_len or remaining_count:
                inner, i, len = Packet.parse(binary, i)
                outer.inner.append(inner)
                if remaining_len:
                    remaining_len -= len
                elif remaining_count:
                    remaining_count -= 1

        return outer, i, i-start_at

this_file_name = os.path.basename(sys.argv[0])
filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open((__file__.rstrip(this_file_name) + filename), 'r') as input_file:
    hex = input_file.readline().rstrip()


h_size = len(hex) * 4
binary = (bin(int(hex, 16))[2:]).zfill(h_size)

p, i, _ = Packet.parse(binary, 0)

print(f"Part I: {sum(p.versions())}")
print(f"Part II: {p.calculate()}")
