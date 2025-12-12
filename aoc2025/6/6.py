import sys
import math

F = [x.split() for x in open(sys.argv[1]).read().splitlines()]
ops = F.pop()
F = [list(map(int,l)) for l in F]

# O = 0
L = [[F[j][i] for j in range(len(F))] for i, op in enumerate(ops)]
# for i, op in enumerate(ops):
#     l = [F[j][i] for j in range(len(F))]
#     O += math.prod(l) if op == '*' else sum(l)

O = sum([math.prod(l) if op == '*' else sum(l) for l,op in zip(L,ops)])
print(O)

# p2
print(L)
for l in L:
    print("coming soon...")