import sys
import numpy as np
from collections import deque

G, M = open(sys.argv[1]).read().split('\n\n')

G = np.array([list(l) for l in G.strip().split()])
M = deque(''.join(M.strip().split()))

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
    while True:
        pos = pos[0] + dir[0], pos[1] + dir[1]
        if G[pos] == 'O':
            move_blocks.append(pos)
        elif G[pos] == '#':
            move_blocks.clear()
            break
        elif G[pos] == '.':
            break
    if not len(move_blocks) == 0:
        ret_pos = ret_pos[0]+dir[0], ret_pos[1]+dir[1]
    while move_blocks:
        block = move_blocks.pop()
        pos = block[0]+dir[0], block[1]+dir[1]
        G[block], G[pos] = G[pos], G[block]
    return ret_pos

while M:
    m = M.popleft()
    pos = apply_move(G, pos, m)

p1 = 0
for y, line in enumerate(G):
    for x, cell in enumerate(line):
        p1 += (100*y + x) if cell == 'O' else 0

print(p1)