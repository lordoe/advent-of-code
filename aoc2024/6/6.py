import numpy as np
import pprint
from collections import defaultdict

with open("input.in", "r") as file:
    M = np.array([list(line.strip()) for line in file])

Xmax = len(M[0])-1
Ymax = len(M)-1

turn_right = {
    (-1, 0): (0, 1), # up
    (0, 1): (1, 0),  # right
    (1, 0): (0, -1), # down
    (0, -1): (-1, 0) # left
}

def apply_dir(pos, dir):
    return pos[0] + dir[0], pos[1] + dir[1]

def is_outside(pos):
    y, x = pos[0], pos[1]
    return x < 0 or y < 0 or x > Xmax or y > Ymax


for i, line in enumerate(M):
    for j, cell in enumerate(line):
        if cell == '^':
            start_pos = (i, j)

pos = start_pos
start_dir = (-1, 0)
dir = start_dir

def walk1(M, pos, dir):
    visited = set()
    visited.add((pos, dir))
    while True:

        n_pos = apply_dir(pos, dir)
        if is_outside(n_pos):
            break

        while M[n_pos] == '#':
            dir = turn_right[dir]
            n_pos = apply_dir(pos, dir)

        visited.add((pos,dir))
        pos = n_pos
        assert(M[pos] in ['.','^'])

        visited.add((pos, dir))
    return visited

visited = walk1(M, pos,dir)
positions = set([c[0] for c in visited])

print(len(visited))
print(len(positions))

def walk2(M, pos, dir, run):
    visited = set()
    visited.add((pos, dir))
    while True:

        n_pos = apply_dir(pos, dir)

        if is_outside(n_pos):
            return False
        
        while M[n_pos] == '#':
            dir = turn_right[dir]
            visited.add((pos, dir))
            n_pos = apply_dir(pos, dir)

        pos = n_pos

        if (pos, dir) in visited:
            return True
        
        assert(M[pos] in ['.','^'])

        visited.add((pos, dir))

count = 0

for i, p in enumerate(positions):
    if M[p] == '.':
        before = M[p]
        M[p] = '#'
        if walk2(M, pos, dir, i):
            count +=1
        M[p] = before

print(count)
