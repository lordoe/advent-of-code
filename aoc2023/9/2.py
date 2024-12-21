#!/bin/bash

with open('input.in') as f:
    lines = f.readlines()

lines = [list(map(int,line.strip().split())) for line in lines]

V = []

for line in lines:
    firsts = [line[0]]
    while any(line):
        line = [line[i+1]-line[i] for i in range(len(line)-1)]
        firsts.append(line[0])

    r = 0
    for l in list(reversed(firsts))[1:]:
        r = -(r - l)
    
    print(r)
    V.append(r)

print(sum(V))
