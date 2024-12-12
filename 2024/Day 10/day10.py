lines = open("./input", "r").read().split("\n")
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
trail_starts = []
rows, cols = len(lines), len(lines[0])
for i in range(rows):
    for j in range(cols):
        if int(lines[i][j]) == 0:
            trail_starts.append((i, j))


print(trail_starts)


def get_count(grid, start, part_2=False):
    seen = set()
    count = 0
    queue = [start]
    while queue:
        i, j = queue.pop()
        current_height = int(grid[i][j])

        if (part_2 or (i, j) not in seen) and current_height == 9:
            seen.add((i, j))
            count += 1
            continue

        for dx, dy in directions:
            nx = i + dx
            ny = j + dy
            if nx in range(len(grid)) and ny in range(len(grid[0])):
                next_height = int(grid[nx][ny])
                if next_height == 1 + current_height:
                    queue.append((nx, ny))

    return count


print(sum([get_count(lines, i) for i in trail_starts]))
print(sum([get_count(lines, i, True) for i in trail_starts]))
