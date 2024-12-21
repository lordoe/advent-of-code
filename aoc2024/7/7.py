import itertools

with open('input.in', 'r') as file:
    L = [[list(map(int,p.split())) for p in line.strip().split(':')] for line in file]

L = [[l[0][0], l[1]] for l in L]
# e.g. [[3267, [81, 40, 27]], ... ]

part = [False, True]

def main(p2):
    def apply_calc(l):
        acc = 0
        for o, p in l:
            if o == '+':
                acc += p
            elif o == '|':
                acc = int(str(acc) + str(p))
            else:
                acc *= p
        return acc

    count = 0

    for s, calc in L:
        ops = '+*|' if p2 else '+*'
        perm = itertools.product(ops, repeat = len(calc)-1)
        for p in perm:
            l = list(zip(p, calc[::-1]))[::-1]
            l.insert(0, ('+', calc[0]))
            # print(l)
            if apply_calc(l) == s:
                # print(calc)
                count += s
                break

    print(count)

for p in part:
    main(p)

# p = itertools.product('*+', repeat=5)

# for prod in p:
#     print(''.join(prod))