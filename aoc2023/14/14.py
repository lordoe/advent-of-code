import sys
import numpy as np

M = np.array(list(list(line) for line in open(sys.argv[1]).read().split()))

Known = {}
Loop = {}
def calc_cycles(M, cycles):
    M = np.rot90(M, -2)
    first = -1
    loop_size = -1
    for c in range(cycles):
        if c % 1000000 == 0: print(c)
        before = ''.join(''.join(l) for l in M)
        if before in Known.keys():
            first = Known[before][0]
            loop_size = c-first
            print(loop_size, first, c)
            break

        for i in range(4):
            M = np.rot90(M, -1)
            Xlen = len(M[0])
            for line in M:
                i = 0
                while i < Xlen-1:
                    if line[i] == '.':
                        for j in range(i+1, Xlen):
                            if line[j] == '#':
                                i = j
                                break
                            if line[j] == 'O':
                                line[i], line[j] = line[j], line[i]
                                break
                    i+=1
        
        # after = ''.join(''.join(l) for l in M)
        Known[before] = (c, M.copy())
    
    if loop_size != -1:
        for m in Known.keys():
            k = Known[m][0]
            if k >= first:
                Loop[k] = Known[m][1]

        wanted = cycles%loop_size
        print('wanted: ', wanted+first)
        M = Loop[wanted+first]

    M = np.rot90(M, -2)

## ursprüngliche position hier

# for m in M:
#     print(''.join(m))

# M = np.rot90(M, -1)

calc_cycles(M, 15)

for l in M:
    print(''.join(l))

M = np.rot90(M, -1)

p1 = 0

for line in M:
    for i, cell in enumerate(line):
        if cell == 'O':
            p1+=(i+1)

print(p1)
