#!/usr/bin/env python3
import sys
import re

x = []

def part1(input):
    for row_ in open(input):
        row = row_.strip()
        x.append(int(row))

    x.sort()
    start = 0
    end = x[-1] + 3

    x.append(end)

    diffs = {}
    prev = start
    for a in x:
        d = a - prev
        count = diffs.get(d, 0)
        diffs[d] = count + 1
        prev = a

    print(diffs)
    print(diffs[1] * diffs[3])

def part2(input):
    for row_ in open(input):
        row = row_.strip()
        x.append(int(row))

    x.sort()
    start = 0
    end = x[-1] + 3

    x.append(end)

    diffs = {}
    spans = {}
    span = False
    prev = start
    for a in x:
        d = a - prev
        count = diffs.get(d, 0)
        diffs[d] = count + 1
        if d == 1:
            if not span:
                span_start = prev
                span = True
        else:
            if span:
                span = False
                l = prev - span_start + 1
                count = spans.get(l, 0)
                spans[l] = count + 1
        prev = a

    print(diffs)
    print(spans)

    # 0 [3 4 5 6 7] [10 11 12 13] [16 17 18]

    print(((4 + 3) ** spans[5]) * (4 ** spans[4]) * (2 ** spans[3]))
   

if __name__ == "__main__":
    if sys.argv[1] == "1": part1(sys.argv[2])
    if sys.argv[1] == "2": part2(sys.argv[2])
