input = open("./input.txt")
data = [tuple(map(int, line.strip().split(","))) for line in input]


def steps(i):
    seen = set(data[:i])
    # print(seen)
    queue = [(0, (0, 0))]

    for dist, (cx, cy) in queue:  # cx, cy: current cell
        if (cx, cy) == (70, 70):

            return dist

        for nx, ny in [(cx, cy + 1), (cx, cy - 1), (cx + 1, cy), (cx - 1, cy)]:
            if (nx, ny) not in seen and 0 <= nx <= 70 and 0 <= ny <= 70:
                queue.append((dist + 1, (nx, ny)))  # Add to queue
                seen.add((nx, ny))  # Mark as seen

    return None


print("Shortest path length:", steps(1024))

left = 0
right = len(data)
while left < right - 1:
    m = (left + right) // 2
    if steps(m):
        left = m
    else:
        right = m

print(data[left])
