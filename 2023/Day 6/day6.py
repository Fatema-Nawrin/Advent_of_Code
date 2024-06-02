times,distances = open("./input", "r").read().split('\n')

times_1 = [int(x) for x in times.split(':')[1].split()]
distances_1 = [int(x) for x in distances.split(':')[1].split()]

def solve(times, distances):
    result = 1
    for t, d in zip(times, distances):
        p = 0
        for i in range(t):
            s = (t - i) * i
            if s > d:
                p += 1
        result *= p
    return result

result_1 = solve(times_1, distances_1)
print(result_1)

times_2 = int(''.join(times.split()[1:]))
distances_2 = int(''.join(distances.split()[1:]))

result_2 = solve([times_2], [distances_2])
print(result_2)
