#!/usr/bin/env python3
import sys

def get_id(seat):
    x = 0
    for i in range(7):
        if seat[i] == "B":
            x += 1 << (6 - i)
    y = 0
    for i in range(3):
        if seat[7 + i] == "R":
            y += 1 << (2 - i)

    #print(seat, x, y, x * 8 + y)
    return x * 8 + y

def part1(input):
    seats = []
    for row in open(input):
        seat = row.strip()
        seats.append(seat)

    mid = 0
    for seat in seats:
        mid = max(mid, get_id(seat))
    print(mid)

def part2(input):
    seats = []
    for row in open(input):
        seat = row.strip()
        seats.append(seat)

    ids = set()
    for seat in seats:
        ids.add(get_id(seat))

    for s in range(1024):
        if s in ids and (s + 1) not in ids and (s + 2) in ids:
            print(s + 1)
    

if __name__ == "__main__":
    if sys.argv[1] == "1": part1(sys.argv[2])
    if sys.argv[1] == "2": part2(sys.argv[2])
