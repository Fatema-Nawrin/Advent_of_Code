from collections import defaultdict

data = open("./input", "r").read().split("\n")


def part1(data):
    row_array = data
    column_array = ["".join([row[i] for row in data]) for i in range(len(data[0]))]
    diagonal_array = find_diagonals(data)
    combined_array = row_array + column_array + diagonal_array[0] + diagonal_array[1]
    count = sum(item.count("XMAS") + item.count("SAMX") for item in combined_array)
    return count


def part2(data):
    rows, cols = len(data), len(data[0])
    count = 0
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if data[row][col] == "A":
                if (
                    data[row - 1][col - 1] == "M" and data[row + 1][col + 1] == "S"
                ) or (data[row - 1][col - 1] == "S" and data[row + 1][col + 1] == "M"):
                    if (
                        data[row - 1][col + 1] == "M" and data[row + 1][col - 1] == "S"
                    ) or (
                        data[row - 1][col + 1] == "S" and data[row + 1][col - 1] == "M"
                    ):
                        count += 1

    return count


def find_diagonals(grid):
    rows, cols = len(grid), len(grid[0])
    #  top-left to bottom-right
    diagonals = defaultdict(list)
    # top-right to bottom-left
    reversed_diagonals = defaultdict(list)

    for row in range(rows):
        for col in range(cols):
            diagonals[row - col].append(grid[row][col])
            reversed_diagonals[row + col].append(grid[row][col])

    diagonals = ["".join(diagonal) for diagonal in diagonals.values()]
    reversed_diagonals = ["".join(diagonal) for diagonal in reversed_diagonals.values()]

    return diagonals, reversed_diagonals


print(part1(data))
print(part2(data))
