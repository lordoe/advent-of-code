#!/bin/bash

with open('input.in') as f:
    lines = f.readlines()

lines = [x.strip() for x in lines]

rounds = []

for line in lines:
    nr = line.split(':')[0].split()[1]
    winning = line.split(':')[1].split('|')[0].split()
    mycards = line.split(':')[1].split('|')[1].split()
    round = {}

    matching = len(set(winning) & set(mycards))

    round['matching'] = matching
    round['copies'] = 1

    rounds.append(round)

for nr, round in enumerate(rounds):
    matching = round['matching']
    copies = round['copies']

    for m in range(1, matching+1):
        rounds[nr + m]['copies'] += copies


sum = 0
for round in rounds:
    sum += round['copies']

print(sum)