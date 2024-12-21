from functools import cache
import sys

sys.setrecursionlimit(10**6)

L = open(sys.argv[1]).read().strip().split()

## part 2 dynamic programming

DP = {}
def len_after_steps(stone: str, steps):
    if steps == 0:
        return 1
    elif (stone, steps) in DP: return DP[(stone, steps)]
    if stone == '0':
        res = len_after_steps('1', steps-1)
    elif len(stone)%2==0:
        res = len_after_steps(str(int(stone[:len(stone)//2])), steps-1) + len_after_steps(str(int(stone[len(stone)//2:])), steps-1)
    else:
        res = len_after_steps(str(int(stone)*2024), steps-1)
    DP[(stone, steps)] = res
    return res

@cache
def cached_func(stone: str, steps):
    if steps == 0:
        return 1
    if stone == '0':
        return cached_func('1', steps-1)
    elif len(stone)%2==0:
        return cached_func(str(int(stone[:len(stone)//2])), steps-1) + cached_func(str(int(stone[len(stone)//2:])), steps-1)
    else:
        return cached_func(str(int(stone)*2024), steps-1)

print(sum([len_after_steps(x, 75) for x in L]))
print(sum([cached_func(x, 75) for x in L]))