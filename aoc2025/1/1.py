import sys
import itertools
import pandas as pd

I = open(sys.argv[1]).read().split()

ops = list(map(lambda y: y[0]*y[1], [(-1 if x[0] == 'L' else 1, int(x[1:])) for x in I]))

pos = list(itertools.accumulate([50] + ops, lambda x, y: (x+y)%100))
print(pos.count(0))

# part 2

# if the wheel goes over zero it ticks
tick = lambda pos, mov: pos != 0 and ((pos+mov)%100 != pos+mov or pos+mov == 0)
sig = lambda x: -1 if x<0 else 1

# ops without rounds
n_ops = [sig(o)*(abs(o)%100) for o in ops]
rounds = [abs(o)//100 for o in ops]

ticks = sum([tick(pos,mov) for (pos, mov) in zip(pos, n_ops)])+sum(rounds)

print(ticks)