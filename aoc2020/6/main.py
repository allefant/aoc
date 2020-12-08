#!/usr/bin/env python3
import sys

class Group:
    def __init__(self):
        self.persons = []
    def count(self):
        q = set()
        for p in self.persons:
            for a in p.answers:
                q.add(a)
        return len(q)
    def count2(self):
        q = {}
        for p in self.persons:
            for a in p.answers:
                q[a] = q.get(a, 0) + 1
        n = len(self.persons)
        r = 0
        for k in q.keys():
            if q[k] == n:
                r += 1
        return r

class Person:
    def __init__(self, answers):
        self.answers = set()
        for a in answers:
            self.answers.add(a)

def part1(input):
    groups = []
    g = Group()
    groups.append(g)
    for row in open(input):
        answers = row.strip()
        if answers:
            p = Person(answers)
            g.persons.append(p)
        else:
            g = Group()
            groups.append(g)

    s = 0
    for g in groups:
        s += g.count()
    print(s)

def part2(input):
    groups = []
    g = Group()
    groups.append(g)
    for row in open(input):
        answers = row.strip()
        if answers:
            p = Person(answers)
            g.persons.append(p)
        else:
            g = Group()
            groups.append(g)

    s = 0
    for g in groups:
        s += g.count2()
    print(s)

if __name__ == "__main__":
    if sys.argv[1] == "1": part1(sys.argv[2])
    if sys.argv[1] == "2": part2(sys.argv[2])
