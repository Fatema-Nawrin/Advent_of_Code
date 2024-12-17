lines = open("./input.txt", "r").read().split("\n")


def get_minimum(part):
    tokens = 0
    for line in lines:
        parts = line.split(" ")
        if parts[0] == "Button":
            btn = parts[1].split(":")[0]
            if btn == "A":
                x1 = int(parts[2][2:-1])
                y1 = int(parts[3][2:])
            else:
                x2 = int(parts[2][2:-1])
                y2 = int(parts[3][2:])

        elif parts[0] == "Prize:":
            s1 = int(parts[1][2:-1])
            s2 = int(parts[2][2:])
            if part == 2:
                s1 = s1 + 10000000000000
                s2 = s2 + 10000000000000
            a = (s1 * y2 - s2 * x2) / (x1 * y2 - y1 * x2)
            b = (s2 * x1 - s1 * y1) / (x1 * y2 - y1 * x2)
            if a == int(a) and b == int(b):
                tokens += 3 * a + b

    print(int(tokens))


get_minimum(1)
get_minimum(2)
