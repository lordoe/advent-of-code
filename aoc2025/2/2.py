import sys
import re
import itertools

I = [tuple(map(int,s.split('-'))) for s in open(sys.argv[1]).read().split(',')]

res = []
for i, j in I:
    for k in range(i, j+1):
        s_k = str(k)
        if len(s_k)%2==0 and s_k[:int(len(s_k)/2)]==s_k[int(len(s_k)/2):]:
            res.append(k)

print(sum(res))

# part 2

cand = [s for inner in [[str(x) for x in range(i,j+1)] for (i,j) in I] for s in inner]

# match strings that contain of repeating strings
pattern = r"^(.+)\1+$"
matches = [int(x.group()) for x in [re.search(pattern, c) for c in cand] if x is not None]
print(sum(matches))

# also right
matches = map(lambda x: int(x.group()), [x for x in map(lambda c: re.search(pattern, c), cand) if x is not None])
print(sum(matches))