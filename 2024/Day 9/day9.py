lines = open("./input", "r").read()

disk = []


def parse(lines):
    disk = []
    for i, c in enumerate(lines):
        if i % 2 == 0:
            disk.extend([i // 2] * int(c))
        else:
            disk.extend("." * int(c))
    return disk


def fill_space(disk):
    l = 0
    r = len(disk) - 1
    while l < r:
        if disk[l] != ".":
            l += 1
            continue
        if disk[r] == ".":
            r -= 1
            continue
        disk[l], disk[r] = disk[r], "."
        l += 1
        r -= 1
    return disk


def part1(lines):
    disk = parse(lines)
    updated = fill_space(disk)
    sum = 0
    for i, c in enumerate(updated):
        if c != ".":
            sum += i * c
    return sum
