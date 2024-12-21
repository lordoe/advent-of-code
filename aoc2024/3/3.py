import re

L = []

with open('input.in', 'r') as file:
    for line in file:
        L.append(line)

pattern = r"(mul\(\d+,\d+\)|do\(\)|don't\(\))"
matches = [re.findall(pattern, l) for l in L]

S = 0

do = True

for match in matches:
    for exp in match:
        if exp == 'do()':
            do = True
        elif exp == 'don\'t()':
            do = False
        elif do:
            x, y = exp.split(',')
            x = int(x[4:])
            y = int(y[:-1])
            S += x*y

print(S)