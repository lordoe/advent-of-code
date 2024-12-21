#!/bin/python3

with open('input.in') as f:
    lines = f.readlines()

R = 12
G = 13
B = 14

def get_number(setup, nr):
    d = dict()
    d['red'], d['green'], d['blue'] = [0], [0], [0]
    for draw in setup:
        for c in draw:
            c = c.strip().split()
            d[c[1]].append(int(c[0]))
    if max(d['red']) > R or max(d['green']) > G or max(d['blue']) > B:
        return 0
    return int(nr)

out = 0

for line in lines:
    l = line.split(':')
    nr = l[0].split()[1]
    setup = l[1].strip().split(';')
    setup = [x.split(',') for x in setup]
    out += get_number(setup, nr)

print(out)
