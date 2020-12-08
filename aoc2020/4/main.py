#!/usr/bin/env python3
import sys

"""
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)
"""

def check_digits(x, a, b):
    if len(x) != 4: return False
    i = int(x)
    if i < a: return False
    if i > b: return False
    return True

def check_height(x):
    if x.endswith("cm"):
        a = int(x[:-2])
        if a < 150 or a > 193: return False
        return True
    if x.endswith("in"):
        a = int(x[:-2])
        if a < 59 or a > 76: return False
        return True
    return False

def check_color(x):
    if not x.startswith("#"): return False
    if len(x) != 7: return False
    try:
        int(x[1:], 16)
    except:
        return False
    return True 

def check_eye(x):
    if x not in set(("amb", "blu", "brn", "gry", "grn", "hzl", "oth")):
        return False
    return True

def check_pid(x):
    if len(x) != 9: return False
    try:
        int(x)
    except:
        return False
    return True

class Passport:
    def __init__(self):
        self.fields = {}
    def add_fields(self, pairs):
        for p in pairs:
            k, v = p.split(":")
            self.fields[k] = v
    def is_valid(self):
        for f in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"):
            if f not in self.fields:
                return False
        return True
    def is_valid2(self):
        if not check_digits(self.fields.get("byr", ""), 1920, 2002): return False
        if not check_digits(self.fields.get("iyr", ""), 2010, 2020): return False
        if not check_digits(self.fields.get("eyr", ""), 2020, 2030): return False
        if not check_height(self.fields.get("hgt", "")): return False
        if not check_color(self.fields.get("hcl", "")): return False
        if not check_eye(self.fields.get("ecl", "")): return False
        if not check_pid(self.fields.get("pid", "")): return False
        
        return True

def part1(input):
    passports = []
    p = Passport()
    passports.append(p)
    for row in open(input):
        if row == "\n":
            p = Passport()
            passports.append(p)
            continue
        p.add_fields(row.split())

    count = 0
    for p in passports:
        if p.is_valid():
            count += 1
    print(count)

def part2(input):
    passports = []
    p = Passport()
    passports.append(p)
    for row in open(input):
        if row == "\n":
            p = Passport()
            passports.append(p)
            continue
        p.add_fields(row.split())

    count = 0
    for p in passports:
        if p.is_valid2():
            count += 1
    print(count)

if __name__ == "__main__":
    if sys.argv[1] == "1": part1(sys.argv[2])
    if sys.argv[1] == "2": part2(sys.argv[2])
