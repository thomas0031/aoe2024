#!/usr/bin/env python3

import bisect

with open('input', 'r') as f:
    lines = f.readlines()
    l1: list[int] = []
    l2: list[int] = []
    for i in range(len(lines)):
        split = lines[i].split()
        bisect.insort(l1, int(split[0]))
        bisect.insort(l2, int(split[1]))
    
    sum = 0
    for a, b in zip(l1, l2):
        sum += abs(a - b)

    print(sum)

