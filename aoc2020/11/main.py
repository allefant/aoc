#!/usr/bin/env python3
import sys
import re

def step(m, w, h):
    m2 = []
    for y in range(h):
        row = m[y]
        row2 = []
        for x in range(w):
            occupied = 0
            if row[x] != "B":
                for j in range(-1, 2):
                    for i in range(-1, 2):
                        if m[y + j][x + i] == "#":
                            occupied += 1
            if row[x] == "L":
                if occupied == 0:
                    row2.append("#")
                else:
                    row2.append(row[x])

            elif row[x] == "#":
                if occupied >= 5:
                    row2.append("L")
                else:
                    row2.append(row[x])
            else:
                row2.append(row[x])
        m2.append(row2)
    return m2

def count(m, w, h, what):
    c = 0
    for y in range(h):
        row = m[y]
        c += row.count(what)
    return c

def part1(input):
    m0 = []
    for row_ in open(input):
        row = row_.strip()
        m0.append(row)

    h = len(m0)
    w = len(m0[0])

    print(w, h)
    m = []
    m.append("B" * (w + 2))
    for i in range(h):
        m.append("B" + m0[i] + "B")
    m.append("B" * (w + 2))

    w += 2
    h += 2

    while True:
        m2 = step(m, w, h)
        if m == m2:
            print(count(m, w, h, "#"))
            break
        m = m2

def step2(m, w, h):
    m2 = []
    for y in range(h):
        row = m[y]
        row2 = []
        for x in range(w):
            occupied = 0
            if row[x] != "B":
                for j in range(-1, 2):
                    for i in range(-1, 2):
                        if i == 0 and j == 0: continue
                        dx = 0
                        dy = 0
                        while True:
                            dx += i
                            dy += j
                            if m[y + dy][x + dx] == ".":
                                continue
                            if m[y + dy][x + dx] == "#":
                                occupied += 1
                            break
            if row[x] == "L":
                if occupied == 0:
                    row2.append("#")
                else:
                    row2.append(row[x])

            elif row[x] == "#":
                if occupied >= 5:
                    row2.append("L")
                else:
                    row2.append(row[x])
            else:
                row2.append(row[x])
        m2.append(row2)
    return m2

def part2(input):
    m0 = []
    for row_ in open(input):
        row = row_.strip()
        m0.append(row)

    h = len(m0)
    w = len(m0[0])

    print(w, h)
    m = []
    m.append("B" * (w + 2))
    for i in range(h):
        m.append("B" + m0[i] + "B")
    m.append("B" * (w + 2))

    w += 2
    h += 2

    while True:
        m2 = step2(m, w, h)
        if m == m2:
            print(count(m, w, h, "#"))
            break
        m = m2

if __name__ == "__main__":
    if sys.argv[1] == "1": part1(sys.argv[2])
    if sys.argv[1] == "2": part2(sys.argv[2])
