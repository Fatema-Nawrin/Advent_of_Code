data = open("./input", "r").read().split("\n")

part1 = 0
part2 = 0


def is_safe(line):
    difference = [a - b for a, b in zip(line, line[1:])]
    if all(i > 0 for i in difference) or all(i < 0 for i in difference):
        if all(0 < abs(i) <= 3 for i in difference):
            return True
    return False


for line in data:
    line_array = [int(x) for x in line.split()]
    if is_safe(line_array):
        part1 += 1

    for i in range(len(line_array)):
        new_line = line_array[0:i] + line_array[i + 1 :]
        if is_safe(new_line):
            part2 += 1
            break


print(part1)
print(part2)
