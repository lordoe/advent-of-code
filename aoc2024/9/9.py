from itertools import accumulate
import sys

with open(sys.argv[1]) as file:
    line = list(map(int,file.read().strip()))

sumline = sum(line)-1

blocks = line[0::2]
spaces = line[1::2]

blocks = [(id, len) for id, len in enumerate(blocks)]

O = []
for i, block in enumerate(blocks):
    O.append([block[0]]*block[1])
    if i < len(blocks)-1:
        O.append([-1]*spaces[i])

def p1(O):
    O = [i for sublist in O for i in sublist]
    i, j = 0, len(O)-1
    while i <= j:
        if O[i] != -1:
            i+=1
        elif O[j] == -1:
            j-=1
        else:
            O[i]=O[j]
            i+=1
            j-=1

    O = O[:j+1]
    count = 0
    for i, el in enumerate(O):
        count += i*el
    return count

blocks = [list(b) for b in blocks]
for i in range(len(spaces)):
    blocks.insert(i*2+1,[-spaces[i]])

for j in reversed(range(len(blocks))):
    # print(blocks)
    if blocks[j][-1] <= 0:
        continue
    # print(j)
    i = 0
    while i<j:
        if blocks[i][-1] >= 0:
            i+=1
        else:
            av = blocks[i][-1]
            # print(av)
            # print(blocks[j])
            b_id, b_len = blocks[j]
            if b_len + av <= 0:
                blocks[i].insert(-1, blocks[j])
                blocks[j] = [-b_len]
                av = b_len + av
                blocks[i][-1] = av
                break
            else:
                i+=1

p2 = []
for i, sublist in enumerate(blocks):
    if len(sublist) > 1 and isinstance(sublist[0], int):
        p2.append([sublist[0]]*sublist[1])
    elif len(sublist) == 1 and sublist[0] < 0:
        p2.append([0]*(-1*sublist[0]))
    else:
        for inner in sublist:
            if isinstance(inner, list):
                p2.append([inner[0]]*inner[1])
            elif inner < 0:
                p2.append([0]*(-1*inner))

p2 = [i for sublist in p2 for i in sublist]

count = 0
for i, el in enumerate(p2):
    count += i*el

print(line)
print(blocks)
print(p1(O))
print(p2)
print(count)