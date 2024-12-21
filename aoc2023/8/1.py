#!/bin/python3

with open('input.in') as f:
    lines = f.readlines()

instructions = lines.pop(0).strip()
lines.pop(0)
lines = [line.strip() for line in lines]

D = {}
for line in lines:
    k = line.split('=')[0].strip()
    rest = line.split('=')[1].strip()
    l, r = rest.split(',')
    l = l.replace('(','').strip()
    r = r.replace(')','').strip()
    D[k] = {'L':l,'R': r}
    print(k, D[k])

rep = 0
state = 'AAA'
while state != 'ZZZ':
    for i in instructions:
        state = D[state][i]
    rep += 1

print(rep * len(instructions))
