#!/usr/bin/env python3
import sys
import re

class Bag:
    def __init__(self):
        self.contains = {}
        self.contained_by = {}

def part1(input):
    bags = {}
    for row_ in open(input):
        row = row_.strip()
        i = row.find(" bags contain ")
        color = row[:i]
        bag = bags.get(color, None)
        if not bag:
            bag = bags[color] = Bag()
        remain = row[i + len(" bags contain "):]
        while remain:
            comma = remain.find(",")
            if comma < 0:
                comma = remain.find(".")
            c2 = remain[:comma]
            mob = re.match(r"\s*(\d+) (.+) bag", c2)
            if not mob:
                if c2 == "no other bags":
                    pass
                else:
                    print(" no match", c2)
            else:
                amount = int(mob.group(1))
                color = mob.group(2)
                if color in bag.contains:
                    print("overwriting rule")
                bag.contains[color] = amount
            remain = remain[comma + 1:]

    for c in bags.keys():
        #print(c, end = " ")
        for c2, a in bags[c].contains.items():
            # print("(", a, c2, ")", end = " ")
            b2 = bags[c2]
            b2.contained_by[c] = a
        #print()

    r = set()
    to_check = ["shiny gold"]
    while to_check:
        color = to_check.pop()
        bag = bags[color]
        for c in bag.contained_by.keys():
            if c not in r:
                r.add(c)
                to_check.append(c)
    print(r)
    print(len(r))

def part2(input):
    bags = {}
    for row_ in open(input):
        row = row_.strip()
        i = row.find(" bags contain ")
        color = row[:i]
        bag = bags.get(color, None)
        if not bag:
            bag = bags[color] = Bag()
        remain = row[i + len(" bags contain "):]
        while remain:
            comma = remain.find(",")
            if comma < 0:
                comma = remain.find(".")
            c2 = remain[:comma]
            mob = re.match(r"\s*(\d+) (.+) bag", c2)
            if not mob:
                if c2 == "no other bags":
                    pass
                else:
                    print(" no match", c2)
            else:
                amount = int(mob.group(1))
                color = mob.group(2)
                if color in bag.contains:
                    print("overwriting rule")
                bag.contains[color] = amount
            remain = remain[comma + 1:]

    for c in bags.keys():
        #print(c, end = " ")
        for c2, a in bags[c].contains.items():
            # print("(", a, c2, ")", end = " ")
            b2 = bags[c2]
            b2.contained_by[c] = a
        #print()

    r = 0
    to_check = [(1, "shiny gold")]
    while to_check:
        amount, color = to_check.pop()
        bag = bags[color]

        r += amount
        for c in bag.contains.keys():
            amount2 = bag.contains[c]
            to_check.append((amount2 * amount, c))

    print(r - 1)

if __name__ == "__main__":
    if sys.argv[1] == "1": part1(sys.argv[2])
    if sys.argv[1] == "2": part2(sys.argv[2])
