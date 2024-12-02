#!/usr/bin/env python3

with open('input', 'r') as f:
    lines = f.readlines()

    matrix: list[list[int]] = []

    for line in lines:
        matrix.append(list(map(int, line.strip().split())))

    safe = 0
    for row in matrix:
        if len(row) < 5:
            print(row)
        is_increase = row[0] < row[1]
        curr_safe = True
        msg = ""
        if abs(row[0] - row[1]) not in [1, 2, 3]:
            curr_safe = False
            msg = "First two elements"
        for i in range(1, len(row) - 1):
            if (row[i] < row[i + 1]) != is_increase:
                curr_safe = False
                msg = "Not all increasing or decreasing"
                break
            diff = row[i + 1] - row[i]
            diff = diff if is_increase else -diff
            if diff not in [1, 2, 3]:
                msg = f"Diff is {diff}"
                curr_safe = False
                break
        safe += 1 if curr_safe else 0

    print(safe)

