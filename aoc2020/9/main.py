#!/usr/bin/env python3
import sys
import re

x = []

def part1(input):
    for row_ in open(input):
        row = row_.strip()
        x.append(int(row))

    for i in range(25, len(x)):
        for j in range(1, 26):
            for k in range(j + 1, 26):
                if x[i - j] + x[i - k] == x[i]:
                    print(x[i - j], "+", x[i - k], "=", x[i])
                    break
            else:
                continue
            break
        else:
            print(i, x[i], "is not a sum")
            break

def part2(input):
    for row_ in open(input):
        row = row_.strip()
        x.append(int(row))

    y = 0
    for i in range(25, len(x)):
        for j in range(1, 26):
            for k in range(j + 1, 26):
                if x[i - j] + x[i - k] == x[i]:
                    break
            else:
                continue
            break
        else:
            y = x[i]
            break

    for i in range(len(x)):
        ysum = 0
        j = 0
        while ysum < y and i + j < len(x):
            ysum += x[i + j]
            j += 1
        if j >= 2 and ysum == y:
            a = min(x[i:i + j])
            b = max(x[i:i + j])
            print(a, "+ ... +", b, "0", ysum, "=", y)
            print(a + b)
            break

if __name__ == "__main__":
    if sys.argv[1] == "1": part1(sys.argv[2])
    if sys.argv[1] == "2": part2(sys.argv[2])
