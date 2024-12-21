#!/bin/python3

with open('input.in') as f:
    lines = f.readlines()

instructions = lines.pop(0).strip()
lines.pop(0)
lines = [line.strip() for line in lines]

ghosts = []
D = {}
for line in lines:
    k = line.split('=')[0].strip()
    rest = line.split('=')[1].strip()
    l, r = rest.split(',')
    l = l.replace('(','').strip()
    r = r.replace(')','').strip()
    D[k] = {'L':l,'R': r}
    if k[-1] == 'A':
        ghosts.append(k)
    print(k, D[k])

g_steps = []

for state in ghosts:
    print(state)
    rep = 0
    while state[-1] != 'Z':
        for i in instructions:
            state = D[state][i]
        rep += 1
    g_steps.append(rep * len(instructions))
    print(state, rep * len(instructions))

# calculate least common multiple of all ghost steps
from math import gcd
lcm = 1
for i in g_steps:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)