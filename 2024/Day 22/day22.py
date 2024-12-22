from collections import defaultdict


input = open("./input").read().split("\n")


def part1(input):
    total = 0
    prune = 16777216
    for s in map(int, input):
        for _ in range(2000):
            s = ((s * 64) ^ s) % prune
            s = ((s // 32) ^ s) % prune
            s = ((s * 2048) ^ s) % prune
        total += s
    return total


def part2(input):
    total = defaultdict(int)
    prune = 16777216
    for s in map(int, input):
        seen = set()
        seq = (0, 0, 0, 0)
        for i in range(2000):
            prev = s % 10
            s = ((s * 64) ^ s) % prune
            s = ((s // 32) ^ s) % prune
            s = ((s * 2048) ^ s) % prune
            seq = seq[1:] + (s % 10 - prev,)

            if i >= 3 and seq not in seen:
                seen.add(seq)
                total[seq] += s % 10
    return max(total.values())


print(part1(input))

print(part2(input))
