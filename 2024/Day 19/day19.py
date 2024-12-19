from functools import cache

input = open("./input.txt").read().split("\n")
patterns = input[0].split(", ")
designs = input[2:]


@cache
def count(d):
    if not d:
        return 1
    total_combinations = 0
    for p in patterns:
        if d.startswith(p):
            remaining_design = d[len(p) :]
            total_combinations += count(remaining_design)

    return total_combinations


def total_designs(designs):
    total = 0
    sum = 0
    for d in designs:
        if count(d) != 0:
            sum += count(d)
            total += 1
    return total, sum


print(total_designs(designs))
