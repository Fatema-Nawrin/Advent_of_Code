input = open("./input.txt").read().split("\n\n")
keys = []
locks = []
for schematics in input:
    lines = schematics.strip().split("\n")
    heights = [r.count("#") - 1 for r in zip(*lines)]
    if lines[0] == "#####":
        locks.append(heights)

    else:
        keys.append(heights)


def part1(keys, locks):
    sum = 0
    for lock in locks:
        for key in keys:
            if all(k + l < 6 for k, l in zip(key, lock)):
                # print(lock, key)
                sum += 1
    return sum


print(part1(keys, locks))
