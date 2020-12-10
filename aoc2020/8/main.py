#!/usr/bin/env python3
import sys
import re

class IntCode:
    def __init__(self):
        self.acc = 0
        self.ip = 0
        self.code = []

    def com(self, icom, arg):
        if icom == 0:
            self.ip += 1
        elif icom == 1:
            self.acc += arg
            self.ip += 1
        elif icom == 2:
            self.ip += arg

commands = {
    "nop":0,
    "acc":1,
    "jmp":2,
    }

def part1(input):
    code = IntCode()
    for row_ in open(input):
        row = row_.strip()
        sp = row.find(" ")
        com = row[:sp]
        arg = int(row[sp + 1:])
        icom = commands[com]
        code.code.append((icom, arg))

    already = set()
    while True:
        icom, arg = code.code[code.ip]
        if code.ip in already:
            print(code.acc)
            break
        already.add(code.ip)
        code.com(icom, arg)

class Node:
    nodes_by_ip = {}
    def __init__(self, ip, parent):
        Node.nodes_by_ip[ip] = self
        self.children = []
        self.ip = ip
        self.acc = 0
        self.changes = 1
        if parent:
            self.acc = parent.acc
            self.changes = parent.changes
            parent.children.append(self)

    def out(self, n):
        print(" " * n, end = "")
        print(self.ip, self.acc)
        for c in self.children:
            c.out(n + 1)

def want(ip, parent, change):
    if ip not in Node.nodes_by_ip:
        return True
    a = Node.nodes_by_ip[ip]
    if parent.changes - change > a.changes:
        return True
    return False

def part2(input):
    global code
    code = IntCode()
    for row_ in open(input):
        row = row_.strip()
        sp = row.find(" ")
        com = row[:sp]
        arg = int(row[sp + 1:])
        icom = commands[com]
        code.code.append((icom, arg))

    print(f"{len(code.code)} lines")

    tree = Node(0, None)
    stack = [tree]
    while stack:
        parent = stack.pop()
        if parent.ip >= len(code.code):
            print(parent.ip, parent.acc)
            break
            
        icom, arg = code.code[parent.ip]
        p = parent.ip
        if icom == 0:
            if want(p + 1, parent, 0):
                n1 = Node(p + 1, parent)
                stack.append(n1)
            if parent.changes > 0:
                if want(p + arg, parent, 1):
                    n2 = Node(p + arg, parent)
                    stack.append(n2)
                    n2.changes -= 1
        if icom == 1:
            if want(p + 1, parent, 0):
                n1 = Node(p + 1, parent)
                stack.append(n1)
                n1.acc += arg
        if icom == 2:
            if want(p + arg, parent, 0):
                n1 = Node(p + arg, parent)
                stack.append(n1)
            if parent.changes > 0:
                if want(p + 1, parent, 1):
                    n2 = Node(p + 1, parent)
                    stack.append(n2)
                    n2.changes -= 1

    #tree.out(0)

if __name__ == "__main__":
    if sys.argv[1] == "1": part1(sys.argv[2])
    if sys.argv[1] == "2": part2(sys.argv[2])
