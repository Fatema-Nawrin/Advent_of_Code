data = open("./input", "r").read().split('\n')
sum_1=0
sum_2=0

for line in data:
    first, second = line.split(',')
    start_1, end_1 = first.split('-')
    start_2, end_2 = second.split('-')
    start_1,end_1 = [int(x) for x in [start_1,end_1]]
    start_2,end_2 = [int(x) for x in [start_2,end_2]]
    if start_1<=start_2 and end_1>=end_2 or start_2<=start_1 and end_2>=end_1:
        sum_1 += 1
    if not (end_1 < start_2 or end_2 < start_1):
        sum_2 += 1

print(sum_1)
print(sum_2)
