from functools import cache

@cache
def func(x):
    print('called', x)
    if x == 1:
        return
    return func(x-1)

print("eval func(3)", func(3))
print()
print("eval func(4)", func(4))

DP = {}
def my_cached_func(x):
    print("called", x)
    if x in DP: return DP[x]
    if x == 1:
        return
    res = my_cached_func(x-1)
    DP[x] = res
    return res

print("\n")
print("eval my_cached_func(3)", my_cached_func(3))
print()
print("eval my_cached_func(4)", my_cached_func(4))
