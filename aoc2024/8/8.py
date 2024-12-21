import numpy as np
from collections import defaultdict

with open('input.in') as file:
    M = np.array([list(line.strip()) for line in file])

Xmax = len(M[0])-1
Ymax = len(M)-1

Obj = defaultdict(list)

for i, line in enumerate(M):
    for j, cell in enumerate(line):
        if cell != '.':
            Obj[cell].append((i, j))

A = list()

for key in Obj.keys():
    for obj in Obj[key]:
        for other in Obj[key]:
            if obj == other:
                continue
            A.append(obj)
            diff = obj[0] - other[0], obj[1] - other[1]
            assert obj[0]-diff[0]==other[0] and obj[1]-diff[1]==other[1]
            ax, ay = obj[0]+diff[0], obj[1]+diff[1]
            while 0 <= ax <= Xmax and 0 <= ay <= Ymax:
                A.append((ax, ay))
                ax, ay = ax+diff[0], ay+diff[1]

for a in A:
    if M[a]=='.':
        M[a] = '#'

print(len(set(A)))