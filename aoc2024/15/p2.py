import sys
import numpy as np
from collections import deque

G, M = open(sys.argv[1]).read().split('\n\n')

G = [list(l) for l in G.strip().split()]
M = deque(''.join(M.strip().split()))

replace = {
    '#': ['#', '#'],
    'O': ['[', ']'],
    '.': ['.', '.'],
    '@': ['@', '.']
}

for y, line in enumerate(G):
    newline = []
    for x, cell in enumerate(line):
        for new in replace[cell]:
            newline.append(new)
    G[y] = newline

G = np.array(G)

# for g in G:
#     print(''.join(g))

# print(M[0])

Ylen = len(G)
Xlen = len(G[0])

pos = ()

for y, line in enumerate(G):
    for x, cell in enumerate(line):
        if cell == '@': pos = (y, x)

directions = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

def apply_move(G, pos, m):
    # print(pos, m)
    ret_pos = pos
    dir = directions[m]
    move_blocks = deque([pos])
    next_pos = deque([(pos[0]+dir[0], pos[1]+dir[1])])
    while next_pos:

        pos = next_pos.popleft()
        if G[pos] == '[':
            assert(G[(pos[0], pos[1]+1)] == ']')
            move_blocks.append(pos)
            if m in '^v':
                # move_blocks.append((pos[0], pos[1]+1))
                if (pos[0], pos[1]+1) not in move_blocks:
                    next_pos.append((pos[0], pos[1]+1))
            next_pos.append((pos[0]+dir[0], pos[1]+dir[1]))
        
        elif G[pos] == ']':
            assert(G[(pos[0], pos[1]-1)] == '[')
            move_blocks.append(pos)
            if m in '^v':
                # move_blocks.append((pos[0], pos[1]-1))
                if (pos[0], pos[1]-1) not in move_blocks:
                    next_pos.append((pos[0], pos[1]-1))
            next_pos.append((pos[0]+dir[0], pos[1]+dir[1]))
        
        elif G[pos] == '#':
            move_blocks.clear()
            break

    if not len(move_blocks) == 0:
        ret_pos = ret_pos[0]+dir[0], ret_pos[1]+dir[1]

    # assert we dont move twice
    # this check shouldnt be necessary
    # the error must be in appending the next blocks to move
    moved = set()

    while move_blocks:
        block = move_blocks.pop()
        if block not in moved:
            pos = block[0]+dir[0], block[1]+dir[1]
            G[block], G[pos] = G[pos], G[block]
            moved.add(block)

    return ret_pos

while M:
    m = M.popleft()
    pos = apply_move(G, pos, m)

# for g in G:
#     print(''.join(g))

p2 = 0
for y, line in enumerate(G):
    for x, cell in enumerate(line):
        p2 += (100*y + x) if cell == '[' else 0

print(p2)