#!/usr/bin/env python3
import sys

def part1(input):
    nums = [int(x) for x in open(input).read().splitlines()]

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == 2020:
                print(nums[i], nums[j], nums[i] * nums[j])

def part2(input):
    nums = [int(x) for x in open(input).read().splitlines()]

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 2020:
                    print(nums[i], nums[j], nums[k], nums[i] * nums[j] * nums[k])

if __name__ == "__main__":
    part2(sys.argv[1])
