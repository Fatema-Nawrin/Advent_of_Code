import re

data = open("./input", "r").read()


def part1(data):
    matches = re.findall("mul\((\d+),(\d+)\)", data)
    result = sum(int(x) * int(y) for x, y in matches)
    print(result)
    return result


part1(data)


def part2(data):
    matches = re.findall("(mul\((\d+),(\d+)\)|do\(\)|don't\(\))", data)
    enabled_match = True
    part2 = 0
    for match in matches:
        if match[0] == "don't()":
            enabled_match = False
        elif match[0] == "do()":
            enabled_match = True
        else:
            if enabled_match:
                part2 += int(match[1]) * int(match[2])

    print(part2)
    return part2


part2(data)
