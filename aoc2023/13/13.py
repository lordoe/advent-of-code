import sys
import numpy as np

M = []
with open(sys.argv[1]) as file:
    I = file.read().split('\n')
    tmp = []
    for m in I:
        if m == '':
            M.append(tmp)
            tmp = []
        else:
            tmp.append(list(m.strip()))

# M = np.array(M)

def switch(arr, i, j):
    if arr[i][j] == '.':
        arr[i][j] = '#' 
    else:
        arr[i][j] = '.'

def check_reflection(m, i, j):
    if j >= len(m):
        return False
    while i >= 0 and j <= len(m)-1:
        one = m[i]
        two = m[j]
        if not (one==two).all():
            return False
        i-=1
        j+=1
    return True

reflections = {}

for p2 in [False, True]:

    s = 0
    for KEY, m in enumerate(M):
        reflects = False
        m = np.array(m)
        for y, line in enumerate(m):
            for x, cell in enumerate(line):
                assert m[y][x] == cell

                # check horicontal reflections
                test = m.copy()
                if p2:
                    switch(test, y, x)

                for i, line in enumerate(test):
                    reflects = check_reflection(test, i, i+1)
                    if reflects:
                        if p2 and (i, i+1, 'h') == reflections[KEY]: continue
                        s+=100*(i+1)
                        if not p2: reflections[KEY] = (i, i+1, 'h')
                        break

                if reflects:
                    break

                # check vertical reflections
                test = np.rot90(test, -1)
                for i, line in enumerate(test):
                    reflects = check_reflection(test, i, i+1)
                    if reflects:
                        if p2 and (i, i+1, 'v') == reflections[KEY]: continue
                        s+=i+1
                        if not p2: reflections[KEY] = (i, i+1, 'v')
                        break
                
                if reflects:
                    break

            if reflects:
                break

        assert reflects

    print(s)
