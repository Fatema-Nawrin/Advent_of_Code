input = open("./input", "r").read()
data = list(map(int, input.split()))


def solve(n, data):

    while n > 0:
        n -= 1
        current_data = []
        for i in data:
            if i == 0:
                current_data.append(1)

            elif len(str(i)) % 2 == 0:
                s = str(i)
                first, second = int(s[: len(s) // 2]), int(s[len(s) // 2 :])
                current_data.append(first)
                current_data.append(second)
            else:
                current_data.append(i * 2024)
        data = current_data

    return len(current_data)


print(solve(25, data))


store = {}


def solve2(stone, n):
    if n == 0:
        return 1
    # Memoization check
    if (stone, n) in store:
        return store[(stone, n)]
    if stone == 0:
        size = solve2(1, n - 1)
    else:
        if len(str(stone)) % 2 == 0:
            s = str(stone)
            first, second = int(s[: len(s) // 2]), int(s[len(s) // 2 :])
            size = solve2(first, n - 1) + solve2(second, n - 1)
        else:
            size = solve2(stone * 2024, n - 1)

    store[(stone, n)] = size
    return size


print(sum(solve2(stone, 75) for stone in data))
