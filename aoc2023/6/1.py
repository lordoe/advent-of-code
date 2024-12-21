#!/bin/python3

with open('input.in') as f:
    lines = f.readlines()

times = list(map(int,lines.pop(0).split()[1:]))
distances = list(map(int,lines.pop(0).split()[1:]))

out = []
for t, d in zip(times, distances):
    wins = 0
    for i in range(t+1):
        if i*(t-i) > d:
            wins += 1
    out.append(wins)

p = 1
for i in out:
    p *= i

print(p)