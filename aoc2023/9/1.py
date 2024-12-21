#!/bin/bash

with open('input.in') as f:
    lines = f.readlines()

lines = [list(map(int,line.strip().split())) for line in lines]

V = []

for line in lines:
    lasts = [line[-1]]
    while any(line):
        line = [line[i+1]-line[i] for i in range(len(line)-1)]
        lasts.append(line[-1])

    t = 0
    for l in reversed(lasts):
        t = t+l

    V.append(t)

print(sum(V))