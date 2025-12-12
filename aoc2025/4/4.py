import sys
import numpy as np

M = [list(x) for x in open(sys.argv[1]).read().split()]
s_x, s_y = len(M[0]), len(M)

# add padding '.' on all edges so no out of bound access can occour
p_x = ['.']*(s_x+2)
N = []
N.append(p_x)
for r in M:
    N.append(['.'] + r + ['.'])
N.append(p_x)

N = np.array(N)

# print(N)

map_val = lambda c: 1 if c == '@' else 0
c_neighbour = lambda x, y: sum([map_val(N[x+i][y+j]) for i in [-1,0,1] for j in [-1,0,1]]) - 1

s = 0
for x, R in enumerate(N):
    for y, c in enumerate(R):
        s += 0 if c == '.' else (1 if c_neighbour(x, y) < 4 else 0)
print(s)

# part 2

s = 0
while True:
    removed = 0
    for x, R in enumerate(N):
        for y, c in enumerate(R):
            if c != '.':
                if c_neighbour(x, y) < 4:
                    s+=1
                    removed+=1
                    N[x][y] = '.'
    if removed == 0:
        break

print(s)