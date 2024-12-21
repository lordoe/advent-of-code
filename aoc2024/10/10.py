import sys
import numpy as np

M = []
with open(sys.argv[1]) as file:
    M = np.array([list(map(int,line.strip())) for line in file])

Ymax = len(M)-1
Xmax = len(M[0])-1

# trailheads
T = []
for i, line in enumerate(M):
    for j, th in enumerate(line):
        if th == 0:
            T.append((i,j))

def neighbours(pos):
    y, x = pos
    nbs = [(y-1,x), (y+1,x), (y,x-1), (y,x+1)]
    return [nb for nb in nbs if 0<=nb[0]<=Ymax and 0<=nb[1]<=Xmax]
    
p2 = 0

def get_scores(pos, scores: set):
    if M[pos] == 9:
        global p2
        p2+=1
        scores.add(pos)
    for n in neighbours(pos):
        if M[n] == M[pos]+1:
            scores.add(get_scores(n, scores))

p1 = 0
for th in T:
    scores = set()
    get_scores(th, scores)
    p1 += len(set(scores))-1

print(p1)
print(p2)