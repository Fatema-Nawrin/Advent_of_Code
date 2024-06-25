data = open("./input", "r").read().split('\n')

win_pair=[('A','Y'),('B','Z'),('C','X')]
lose_pair=[('A','Z'),('B','X'),('C','Y')]

sum_1=0
sum_2=0

for line in data:
    op,me=line.split(' ')
    p1 = "ABC".index(op)+1
    p2 = "XYZ".index(me)+1
    if p1 == p2:
        v=3
    elif (op,me) in win_pair:
        v=6
    else:
        v=0
    sum_1+=v+p2
print(sum_1)


for line in data:
    op,me=line.split(' ')
    if me == 'X':
        v=0
        p2 = "XYZ".index(dict(lose_pair).get(op))+1  
    elif me =='Y':
        v=3
        p2 = "ABC".index(op)+1
    else:
        v=6
        p2 = "XYZ".index(dict(win_pair).get(op))+1
    sum_2+=v+p2
print(sum_2)

