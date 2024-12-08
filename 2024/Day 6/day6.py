data = open("./input", "r").read()
# up, , down ,left
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def get_start_pos(lines):
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "^":
                return (i, j)


def walk(data):
    grids = list(map(list, data.splitlines()))
    start_pos = get_start_pos(grids)
    print(start_pos)
    # up dir
    d = 0

    rows, cols = len(grids), len(grids[0])

    visited = set()
    visited.add((start_pos[0], start_pos[1]))

    while True:
        dirs = directions[d]
        current_loc = (start_pos[0] + dirs[0], start_pos[1] + dirs[1])
        if current_loc[0] not in range(rows) or current_loc[1] not in range(cols):
            return visited

        if grids[current_loc[0]][current_loc[1]] == "#":
            d += 1
            d %= 4
            continue
        else:
            visited.add((current_loc[0], current_loc[1]))
            start_pos = current_loc


def is_loop(grids):
    start_pos = get_start_pos(grids)
    # up dir
    d = 0

    rows, cols = len(grids), len(grids[0])

    visited = set()
    visited.add((start_pos[0], start_pos[1], d))
    while True:
        dirs = directions[d]
        current_loc = (start_pos[0] + dirs[0], start_pos[1] + dirs[1])
        if current_loc[0] not in range(rows) or current_loc[1] not in range(cols):
            # return visited
            return False

        if grids[current_loc[0]][current_loc[1]] == "#":
            d += 1
            d %= 4
            continue

        start_pos = current_loc

        if (current_loc, d) in visited:
            return True

        visited.add((current_loc, d))


def part1(data):
    walked = walk(data)
    print(len(walked))


def part2(data):
    grids = list(map(list, data.splitlines()))
    count = 0
    for i in range(len(grids)):
        for j in range(len(grids[0])):
            if grids[i][j] == ".":
                previous = grids[i][j]
                grids[i][j] = "#"
                loop = is_loop(grids)
                if loop:
                    count += 1
                grids[i][j] = previous
    print(count)
    return count


part1(data)
part2(data)
