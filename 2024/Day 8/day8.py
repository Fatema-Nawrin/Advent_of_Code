from collections import defaultdict

data = open("./input", "r").read().split("\n")


def parse_input(data):
    rows, cols = len(data), len(data[0])
    antennas = defaultdict(list)
    for i in range(rows):
        for j in range(cols):
            if data[i][j] != ".":
                antennas[data[i][j]].append((i, j))
    return rows, cols, antennas


def part1(data):
    rows, cols, antennas = parse_input(data)
    antinodes = set()
    for antenna, positions in antennas.items():
        for i, p1 in enumerate(list(positions)):
            for p2 in list(positions)[i + 1 :]:
                dis = (p2[0] - p1[0], p2[1] - p1[1])
                antinode1 = (p1[0] - dis[0], p1[1] - dis[1])
                antinode2 = (p2[0] + dis[0], p2[1] + dis[1])
                for pos in [antinode1, antinode2]:
                    if 0 <= pos[0] < rows and 0 <= pos[1] < cols:
                        antinodes.add(pos)

    return len(antinodes)


def part2(data):
    rows, cols, antennas = parse_input(data)
    antinodes = set()
    for antenna, positions in antennas.items():
        for i, p1 in enumerate(list(positions)):
            for p2 in list(positions)[i + 1 :]:
                dis = (p2[0] - p1[0], p2[1] - p1[1])
                antinode1 = p1
                antinode2 = p2
                while (0 <= antinode1[0] < rows and 0 <= antinode1[1] < cols) or (
                    0 <= antinode2[0] < rows and 0 <= antinode2[1] < cols
                ):
                    if 0 <= antinode1[0] < rows and 0 <= antinode1[1] < cols:
                        antinodes.add(antinode1)
                    if 0 <= antinode2[0] < rows and 0 <= antinode2[1] < cols:
                        antinodes.add(antinode2)
                    antinode1 = (antinode1[0] - dis[0], antinode1[1] - dis[1])
                    antinode2 = (antinode2[0] + dis[0], antinode2[1] + dis[1])

    return len(antinodes)


print(part1(data))
print(part2(data))
