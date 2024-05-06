import re
s_pattern = r'[^\d.]'
n_pattern= r'\d+'
sum=0

data = open("./input", "r").read().split('\n')

for i, line in enumerate(data):
    for m in re.finditer(n_pattern, line):
        j = max(0, m.start() - 1)
        k=min(len(line), m.end() + 1)
        before = data[i-1][j:k] if i > 0 else ''
        after = data[i+1][j:k] if i < len(data)-1 else ''
        side1=line[j] if j>0 else ''
        side2=line[k-1] if k < len(line) else ''
        
        if re.findall(s_pattern, before + after + side1 + side2):
            sum+=int(m.group())

print(sum)

# Part 2

g_pattern = r'\*'
gears = dict()
ratio_sum = 0

for i, line in enumerate(data):
    for m in re.finditer(g_pattern, line):
        gears[(i, m.start())] = []

for i, line in enumerate(data):
    for m in re.finditer(n_pattern, line):
        for r in range(max(i-1, 0), min(i+2, len(data))):
                for c in range(max(m.start()-1, 0), min(m.end()+1, len(line))):
                    if (r, c) in gears:
                        gears[(r, c)].append(int(m.group()))

for n in gears.values():
    if len(n) == 2:
       ratio_sum += n[0] * n[1]
        
       

print(ratio_sum)




