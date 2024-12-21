import numpy as np

with open('input.in') as file:
    M = np.array([np.array(list(line.strip())) for line in file])
    Mrot = np.rot90(M)


s = 0

for m in [M, Mrot]:
    for i in range(-len(m)+1,len(m)):
        l = ''.join(m.diagonal(offset=i))
        s += l.count('XMAS')
        s += l[::-1].count('XMAS')

    for line in m:
        l = ''.join(line)
        s += l.count('XMAS')
        s += l[::-1].count('XMAS')

print(s)

## part 2

s2 = 0

def count_mas(i, j):
    mas = 0
    d1, d2 = M[i-1][j-1]+M[i][j]+M[i+1][j+1], M[i+1][j-1]+M[i][j]+M[i-1][j+1]
    d1r, d2r = d1[::-1], d2[::-1]
    for d in [d1, d2, d1r, d2r]:
        if d == 'MAS':
            mas+=1
    return mas

for i in range(1, len(M)-1):
    for j in range(1, len(M[i])-1):
        if M[i][j] == 'A':
            if count_mas(i,j) == 2:
                s2 +=1

print(s2)