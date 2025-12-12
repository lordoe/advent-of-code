import sys

F = list(map(lambda l: [int(x) for x in l], map(list, open(sys.argv[1], 'r').read().split())))

print(sum([int(str(a)+str(b)) for a,b in map( lambda l: ( max(l[:-1]), max(l[l.index(max(l[:-1]))+1:]) ), F)]))

## part 2

D = 12
s = 0
for l in F:
    o = []
    i = 0
    for d in reversed(range(1, D)):
        m = max(l[:-d])
        assert(m!=-1)
        l = l[l.index(m)+1:]
        o.append(m)
    o.append(max(l))
    assert(len(o)==12)
    s += int(''.join([str(x) for x in o]))

print(s)
# 172162399742349
    