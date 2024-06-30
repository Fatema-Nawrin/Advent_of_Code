data = open("./input", "r").read().split('\n')

def priority(item):
    if "a" <= item <= "z":
        return ord(item) - ord('a') + 1
    else:
        return ord(item)- ord('A') +  27

sum_1=0

for l in data:
    mid = len(l) // 2
    p1, p2 = l[:mid], l[mid:]
    common_char=set(p1) & set(p2)
    for c in common_char:
        sum_1+=priority(c)
    


print(sum_1)

sum_2=0
index = 0            
for i in range(0, len(data), 3):   
    p1, p2, p3 = data[i:i+3]
    common_char=set(p1) & set(p2) & set(p3)
    for c in common_char:
        sum_2+=priority(c)


print(sum_2)