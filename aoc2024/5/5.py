#!/bin/python3
from collections import defaultdict

R = []
D = []

with open("input.in", "r") as file:
    for line in file:
        if line.find('|') > 0:
            R.append(tuple(map(int,line.strip().split("|"))))
        elif line != '\n':
            D.append(list(map(int,line.strip().split(","))))

# Key = number, Values = list(numbers that must be before key number (<=> must not be after that number))
K = defaultdict(list)

for r in R:
    K[r[1]].append(r[0])


def check(d):
    l = len(d)
    for i in range(l):
        v = d[i]
        for j in range(i+1, l):
            if d[j] in K[v]:
                return False, j, i
    return True, 0, 0

def order(d: list):
    works, j, i = check(d)
    while not works:
        d[j], d[i] = d[i], d[j]
        works, j, i = check(d)

p1 = 0
p2 = 0

for d in D:
    if check(d)[0]:
        p1 += d[len(d)//2]
    else:
        order(d)
        p2 += d[len(d)//2]

print(p1)
print(p2)