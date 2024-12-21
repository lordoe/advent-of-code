#!/bin/bash

with open('input.in') as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]

sum = 0

for line in lines:
    nr = line.split(':')[0].split()[1]
    winning = line.split(':')[1].split('|')[0].split()
    mycards = line.split(':')[1].split('|')[1].split()

    pow = len(set(winning) & set(mycards)) - 1

    if pow >= 0:
        sum += 2**pow
    
print(sum)