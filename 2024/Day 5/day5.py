from collections import defaultdict

data = open("./input", "r").read()
first_sec, second_sec = data.split("\n\n")

rules = defaultdict(set)
updates = []

for line in first_sec.split("\n"):
    if "|" in line:
        a, b = map(int, line.split("|"))
        rules[a].add(b)

for line in second_sec.split("\n"):
    updates.append(list(map(int, line.split(","))))


def check_valid(rules, line):
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            if line[j] not in rules[line[i]]:
                return False
    return True


part1 = 0
part2 = 0


def correct_order(rules, update):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if update[j] not in rules[update[i]]:
                update[i], update[j] = update[j], update[i]
    return update


for update in updates:
    if check_valid(rules, update):
        part1 += update[len(update) // 2]
for update in updates:
    if not check_valid(rules, update):
        correct_update = correct_order(rules, update)
        part2 += correct_update[len(correct_update) // 2]


print(part1)
print(part2)
