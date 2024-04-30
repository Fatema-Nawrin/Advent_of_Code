import re
data = open("./input", "r").read().split('\n')

s=0
p=0

for i, game in enumerate(data,1):
    r,g,b = [max(int(count) for count, color in re.findall('(\d+) (red|green|blue)', game) if color == c) for c in ['red', 'green', 'blue']]
    if r <= 12 and g <= 13 and b <= 14:
        s += i
    p+=r*g*b
    

print(s)
print(p)

    
