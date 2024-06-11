
data = open("./input", "r").read()

rows = [[int(i) for i in line.split(" ")]for line in data.split('\n')]


def next_value(row):
    if all(x==0 for x in row):
        return 0
    differences=[]
    for j in range(len(row)-1):
        differences.append(row[j+1]-row[j])
    return row[-1]+ next_value(differences)
 
part_1=0
for row in rows:
    part_1+=next_value(row)

print(part_1)


part_2=0
for row in rows:
    reverse_row = list(reversed(row))
    part_2+=next_value(reverse_row)


print(part_2)