import sys
import numpy as np

R = [tuple(tuple(map(int,x.split('=')[1].split(','))) for x in r.split(' ')) for r in open(sys.argv[1]).read().split('\n')]

Xlen = 101 if 'input' in sys.argv[1] else 11
Ylen = 103 if 'input' in sys.argv[1] else 7

steps = 100

M = np.array([[0]*Xlen]*Ylen)

for r in R:
    pos, vel = r
    x, y = pos
    vx, vy = vel
    ny = (steps*vy + y) % Ylen
    nx = (steps*vx + x) % Xlen
    M[ny][nx] += 1

Xh = Xlen//2
Yh = Ylen//2

p1 = 1
p1 *= sum(sum(M[:Yh, :Xh]))
p1 *= sum(sum(M[:Yh, Xh+1:]))
p1 *= sum(sum(M[Yh+1:, :Xh]))
p1 *= sum(sum(M[Yh+1:, Xh+1:]))

print(p1)

## p2

M = np.array([[' ']*Xlen]*Ylen)

def M_after_steps(M, step):
    Mt = M.copy()
    for r in R:
        pos, vel = r
        x, y = pos
        vx, vy = vel
        ny = (step*vy + y) % Ylen
        nx = (step*vx + x) % Xlen
        Mt[ny][nx] = '#'
    return Mt

# do this till you find the tree
# step = 0
# while True:
#     print('='*80)
#     print('step: ', step)
#     Mt = M_after_steps(M, step)
#     for line in Mt:
#         print(''.join(line))
#     step += 1
#     if input() == 'x':
#         break

Mtree = M_after_steps(M, 7916)

for line in Mtree:
    print(''.join(line))