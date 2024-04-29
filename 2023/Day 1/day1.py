import re

data = open("input", "r").read().strip()

def calibration(data):
    lines = data.split('\n')
    numbers = [re.findall("\d", line) for line in lines]
    return sum(int(n[0] + n[-1]) for n in numbers)
   
ans1=calibration(data)
print(ans1)

# Part2
to_num = {
    'one': 'one1one',
    'two': 'two2two',
    'three': 'three3three',
    'four': 'four4four',
    'five': 'five5five',
    'six': 'six6six',
    'seven': 'seven7seven',
    'eight': 'eight8eight',
    'nine': 'nine9nine'
}

for x, n in to_num.items():
    data = data.replace(x, n)

ans2=calibration(data)
print(ans2)