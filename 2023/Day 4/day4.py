data = open("./input", "r").read().split('\n')

points=0
cards = [1] * len(data)
# a list filled with ones.

for i, line in enumerate(data):
    win, input = line.split(":")[1].split("|")
    common=set(win.split()) & set(input.split())
    # print(len(common))
    if common:
        points +=2**(len(common)-1)
        
    for j in range(len(common)):
       cards[i+j+1] += cards[i]

print(points)
print(sum(cards))



