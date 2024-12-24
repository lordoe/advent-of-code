import sys
import numpy as np
from collections import deque, defaultdict
from queue import PriorityQueue

M = np.array([list(l) for l in open(sys.argv[1]).read().split()])

Xlen = len(M[0])
Ylen = len(M)

start = (Ylen -2, 1)
assert M[start] == 'S'

seen = set()
nexts = PriorityQueue()
nexts.put((0, (start, (0, 1), (start, 0))))

p1 = 0
backtrack = defaultdict(list)

"""
Dijkstra algorithm for part1
For part 2 we have create a backtrack dict that saves pairs of (node, cost_to_next_node): [(prev, actual_cost), ..]
We break when we processed all minimal paths that lead to the E node
"""

while not nexts.empty():
    cost, (pos, dir, prev_pcost) = nexts.get()
    prev, pcost = prev_pcost
    if M[pos] == 'E':
        if p1 == 0:
            p1 = cost
        elif cost > p1:
            break
        backtrack[(pos, None)].append((prev, cost))

    if (pos, dir) in seen:
        continue
    seen.add((pos, dir))
    y, x = pos
    for yy, xx in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        if M[(y+yy, x+xx)] == '#' or ((y+yy, x+xx), (yy, xx)) in seen:
            continue
        turn = 1000 if dir != (yy, xx) else 0
        ncost = cost + 1 + turn
        nexts.put((ncost, ((y+yy, x+xx), (yy, xx), ((y, x), cost))))
        backtrack[(pos, ncost)].append((prev, cost))


seen = set()
path = deque([((1, Xlen-2), None)])

while path:
    pos, ncost = path.popleft()
    M[pos] = 'O'
    if pos == start:
        print(path)
        break
    if (pos, ncost) in seen:
        continue
    seen.add((pos, ncost))
    for prev, cost  in backtrack[(pos, ncost)]:
        if not (prev, cost) in seen:
            path.append((prev, cost))

for line in M:
    print(''.join(line))

p2 = 0

for line in M:
    for cell in line:
        if cell == 'O':
            p2 += 1

print(p1)
print(p2)
