#!/bin/python3

from collections import Counter

with open('input.in') as f:
    lines = f.readlines()

games = [line.split() for line in lines]
print(games)

cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5' ,'4', '3', '2']
card_vals = {
    'A': 0,
    'K': 1, 
    'Q': 2,
    'T': 3,
    '9': 4,
    '8': 5,
    '7': 6,
    '6': 7,
    '5': 8,
    '4': 9,
    '3': 10,
    '2': 11,
    'J': 12,
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

for hand, val in games:

    t = poss_hands[''.join(sorted(hand))]

    # five of a kind
    if t == 0:
        types[t].append((hand, val))

    # four of a kind
    elif t == 1:
        if hand.count('J') == 1 or hand.count('J') == 4:
            types[0].append((hand, val))
        else:
            types[1].append((hand, val))
    
    # full house
    elif t == 2:
        if hand.count('J') in [2,3]:
            types[0].append((hand, val))
        else:
            types[2].append((hand, val))

    # three of a kind
    elif t == 3:
        if hand.count('J') == 3:
            c = Counter(hand)
            if sorted(c.values()) == [1, 1, 3]:
                types[1].append((hand, val))
            elif sorted(c.values()) == [2, 3]:
                types[0].append((hand, val))
            else:
                assert False, f'J: {hand}'
        elif hand.count('J') == 2:
            assert False, f'should be fh , is toak: {hand}'
        elif hand.count('J') == 1:
            types[1].append((hand, val))
        else:
            types[3].append((hand, val))
    
    # two pair
    elif t == 4:
        if hand.count('J') == 2:
            types[1].append((hand, val))
        elif hand.count('J') == 1:
            types[2].append((hand, val))
        else:
            assert hand.count('J') == 0, f'J: {hand}'
            types[4].append((hand, val))
    
    # one pair
    elif t == 5:
        if hand.count('J') == 1:
            types[3].append((hand, val))
        elif hand.count('J') == 2:
            types[3].append((hand, val))
        else:
            assert hand.count('J') == 0, f'J: {hand}'
            types[5].append((hand, val))

    # high card
    elif t == 6:
        if hand.count('J') == 1:
            types[5].append((hand, val))
        else:
            assert hand.count('J') == 0, f'J: {hand}'
            types[6].append((hand, val))

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

# 249631254