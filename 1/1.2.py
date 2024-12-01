#!/usr/bin/env python3

with open('input', 'r') as f:
    lines = f.readlines()
    l1: list[int] = []
    m2: dict[int, int] = {}
    for line in lines:
        split = line.split()
        l1.append(int(split[0]))
        key = int(split[1])
        if key in m2:
            m2[key] += 1
        else:
            m2[key] = 1
    
    sum = 0
    for a in l1:
        print(a)
        sum += a * m2.get(a, 0)

    print(sum)

