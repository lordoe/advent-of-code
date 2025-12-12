import sys
import itertools
from collections import deque

Rs, I = (x.splitlines() for x in open(sys.argv[1]).read().split("\n\n"))

incl_tuples = [(int(x),int(y)) for x,y in (i.split('-') for i in Rs)]
I = list(map(int,I))

print(sum([any([i in range(r[0],r[1]+1) for r in incl_tuples]) for i in I]))

# part2

incl_tuples.sort(key= lambda x: x[0])
incl_tuples = deque(incl_tuples)

incl_sums = []
l,u = incl_tuples.popleft()
while len(incl_tuples)>=1:
    sl,su = incl_tuples.popleft()
    if l <= su and sl <= u: # overlapping
        l, u = min(l, sl), max(u, su)
    else:
        incl_sums.append((l, u))
        l,u = sl,su
incl_sums.append((l, u))

print(sum([len(range(x,y+1)) for x,y in incl_sums]))
