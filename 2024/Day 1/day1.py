data = open("./input", "r").read().split("\n")

left_list = []
right_list = []

for line in data:
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)

sorted_left = sorted(left_list)
sorted_right = sorted(right_list)
distance = 0


for i in range(len(sorted_left)):
    distance += abs(sorted_left[i] - sorted_right[i])
print(distance)


score = sum(x * right_list.count(x) for x in left_list)
print(score)
