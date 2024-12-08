data = open("./input", "r").read().split("\n")


def solve(data, new_op):
    count = []
    for line in data:
        parts = line.split(":")
        target = int(parts[0])
        numbers = list(map(int, parts[1].split()))

        res = [numbers.pop(0)]
        while numbers:
            j = numbers.pop(0)
            next_res = []
            for i in res:
                next_res.append(i + j)
                next_res.append(i * j)
                if new_op == True:
                    next_res.append(int(str(i) + str(j)))
            res = next_res
        if target in res:
            count.append(target)

    return sum(count)


# part1
print(solve(data, False))
# part2
print(solve(data, True))
