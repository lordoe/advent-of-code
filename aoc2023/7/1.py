#!/bin/python3

with open('dc.in') as f:
    lines = f.readlines()

games = [line.split() for line in lines]
print(games)

cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5' ,'4', '3', '2']
card_vals = {
    'A': 0,
    'K': 1, 
    'Q': 2,
    'J': 3,
    'T': 4,
    '9': 5,
    '8': 6,
    '7': 7,
    '6': 8,
    '5': 9,
    '4': 10,
    '3': 11,
    '2': 12
}
# count = 0
poss_hands = {}

# five of a kind
for c in cards:
    poss_hands[c*5] = 0
    # count += 1
# four of a kind
for c in cards:
    for other_c in cards:
        if c != other_c:
            poss_hands[''.join(sorted(c*4 + other_c))] = 1
            # count += 1
# full house
for c in cards:
    for other_c in cards:
        if c != other_c:
            poss_hands[''.join(sorted(c*3 + other_c*2))] = 2
            # count += 1
# three of a kind
for c in cards:
    for other_c in cards:
        for other_other_c in cards:
            if c != other_c and c != other_other_c and other_c != other_other_c:
                poss_hands[''.join(sorted(c*3 + other_c + other_other_c))] = 3
                # count += 1
# two pair
for i in range(len(cards)):
    for j in range(i+1, len(cards)):
        for k in range(len(cards)):
            if k != i and k != j:
                poss_hands[''.join(sorted(cards[i]*2 + cards[j]*2 + cards[k]))] = 4
                # count += 1
# one pair
for i in range(len(cards)):
    for j in range(len(cards)):
        for k in range(len(cards)):
            for l in range(len(cards)):
                if i != j and i != k and i != l and j != k and j != l and k != l:
                    poss_hands[''.join(sorted(cards[i]*2 + cards[j] + cards[k] + cards[l]))] = 5
                    # count += 1
# high card
for i in range(len(cards)):
    for j in range(len(cards)):
        for k in range(len(cards)):
            for l in range(len(cards)):
                for m in range(len(cards)):
                    if i != j and i != k and i != l and i != m and j != k and j != l and j != m and k != l and k != m and l != m:
                        poss_hands[''.join(sorted(cards[i] + cards[j] + cards[k] + cards[l] + cards[m]))] = 6
                        # count += 1

types = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: []
}

def translate(string):
    return [card_vals[c] for c in string]

print(translate('AAAAA'))

# print(games)

for game in games:
    # print(game, poss_hands[''.join(sorted(game[0]))])
    types[poss_hands[''.join(sorted(game[0]))]].append(game)

for t in types.values():
    t.sort(key=lambda x: translate(x[0]))

score = 0

count = 1
for t in reversed(types.values()):
    if t:
        for g in reversed(t):
            if g:
                print(g, count)
                score += count * int(g[1])
                count += 1

print(score)

# answer part1
# 248559379