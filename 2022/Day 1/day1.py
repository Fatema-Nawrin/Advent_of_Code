data = open("./input", "r").read().split('\n\n')

sum_arr=[]

for line in data:
    el=line.split('\n')
    nums=[int(i) for i in el]
    s=sum(nums)
    sum_arr.append(s)


part_1=max(sum_arr)
print(part_1)

sorted_arr=sorted(sum_arr)[-3:]
part_2=sum(sorted_arr)
print(part_2)