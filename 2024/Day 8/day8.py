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
        for i, a in enumerate(list(positions)):
            for b in list(positions)[i + 1 :]:
                dis = (b[0] - a[0], b[1] - a[1])
                an1 = (a[0] - dis[0], a[1] - dis[1])
                an2 = (b[0] + dis[0], b[1] + dis[1])
                for p in [an1, an2]:
                    if 0 <= p[0] < rows and 0 <= p[1] < cols:
                        antinodes.add(p)

    return len(antinodes)


def part2(data):
    rows, cols, antennas = parse_input(data)
    antinodes = set()
    for antenna, positions in antennas.items():
        for i, a in enumerate(list(positions)):
            for b in list(positions)[i + 1 :]:
                dis = (b[0] - a[0], b[1] - a[1])
                an1 = a
                an2 = b
                while (0 <= an1[0] < rows and 0 <= an1[1] < cols) or (
                    0 <= an2[0] < rows and 0 <= an2[1] < cols
                ):
                    if 0 <= an1[0] < rows and 0 <= an1[1] < cols:
                        antinodes.add(an1)
                    if 0 <= an2[0] < rows and 0 <= an2[1] < cols:
                        antinodes.add(an2)
                    an1 = (an1[0] - dis[0], an1[1] - dis[1])
                    an2 = (an2[0] + dis[0], an2[1] + dis[1])

    return len(antinodes)


print(part1(data))
print(part2(data))
