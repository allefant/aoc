#!/usr/bin/env python3
import sys

class Row: pass

def check_pw(r):
    count = 0
    for i in range(len(r.pw)):
        c = r.pw[i]
        if c == r.letter:
            count += 1
    if count >= r.a and count <= r.b:
        return True
    return False

def part1(input):
    rows = []
    found = 0
    for row in open(input):
        r = Row()
        a, b, r.pw = row.split()
        r.a, r.b = a.split("-")
        r.a = int(r.a)
        r.b = int(r.b)
        r.letter = b.rstrip(":")
        rows.append(r)

        if check_pw(r):
            found += 1
    print(found)

def check_pw2(r):
    count = 0
    for i in range(len(r.pw)):
        pos = 1 + i
        c = r.pw[i]
        if c == r.letter and (pos == r.a or pos == r.b):
            count += 1
    return count == 1

def part2(input):
    rows = []
    found = 0
    for row in open(input):
        r = Row()
        a, b, r.pw = row.split()
        r.a, r.b = a.split("-")
        r.a = int(r.a)
        r.b = int(r.b)
        r.letter = b.rstrip(":")
        rows.append(r)

        if check_pw2(r):
            found += 1
    print(found)


if __name__ == "__main__":
    part2(sys.argv[1])
