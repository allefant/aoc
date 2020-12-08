#!/usr/bin/env python3
import sys

def part1(input):
    rows = []
    found = 0
    for row in open(input):
        row = row.rstrip()
        if not row: continue
        rows.append(row)
        w = len(row)
        print(row)
    h = len(rows)
    print(w, h)

    trees = 0
    x, y = 3, 1
    while y < h:
        if rows[y][x % w] == "#":
            trees += 1
        x += 3
        y += 1
        
    print(trees)

def check(rows, w, h, dx, dy):
    trees = 0
    x, y = dx, dy
    while y < h:
        if rows[y][x % w] == "#":
            trees += 1
        x += dx
        y += dy
    return trees

def part2(input):
    rows = []
    found = 0
    for row in open(input):
        row = row.rstrip()
        if not row: continue
        rows.append(row)
        w = len(row)
        print(row)
    h = len(rows)
    print(w, h)

    a = check(rows, w, h, 1, 1)
    b = check(rows, w, h, 3, 1)
    c = check(rows, w, h, 5, 1)
    d = check(rows, w, h, 7, 1)
    e = check(rows, w, h, 1, 2)

    print(a, b, c, d, e)
    print(a * b * c * d * e)

if __name__ == "__main__":
    part2(sys.argv[1])
