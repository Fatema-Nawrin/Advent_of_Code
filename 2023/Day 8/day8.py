from math import lcm

data = open("./input", "r").read()
directions, nodes = data.split('\n\n')

modified_directions=directions.replace('L', '0').replace('R', '1')

path={}
for line in nodes.split('\n'):
    node, lr = line.strip().split(' = ')
    l, r = lr.strip('()').split(', ')
    path[node] = (l, r)

part_1 = 0
current = "AAA"
while current != "ZZZ":
    for i in modified_directions:
        if current != "ZZZ":
            current = path[current][int(i)]
            part_1 += 1
        else: 
            break
print(part_1)



steps=[]
for node in path.keys():
    if node[-1] == 'A':
        step = 0
        current_node = node
        while current_node[-1] != 'Z':
            for i in modified_directions:
                current_node = path[current_node][int(i)]
                step += 1
        steps.append(step)

part_2 = lcm(*steps)
print(part_2)