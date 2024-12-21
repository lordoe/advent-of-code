#!/bin/python3

with open('input.in') as f:
    lines = f.readlines()

times = list(lines.pop(0).split()[1:])
t = ""
for i in times:
    t += i
t = [int(t)]

distances = list(lines.pop(0).split()[1:])
d = ""
for i in distances:
    d += i
d = [int(d)]

out = []
for t, d in zip(t, d):
    wins = 0
    for i in range(t+1):
        if i*(t-i) > d:
            wins += 1
    out.append(wins)

p = 1
for i in out:
    p *= i

print(p)