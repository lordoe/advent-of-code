import sys
import numpy as np

G = np.array((list(map(list,open(sys.argv[1]).read().split()))))

Ymax = len(G)-1
Xmax = len(G[0])-1

p2 = True

def traverse(G, y, x, sum_signs_orig, visited: set, edgeset: set):
    visited.add((y, x))
    sum_signs = sum_signs_orig + 1
    edges = 0
    sign = G[y][x]
    for yy, xx, c in [(-1, 0, 'u'), (1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r')]:
        ny, nx = y+yy, x+xx
        if 0 <= ny <= Ymax and 0 <= nx <= Xmax:
            nsign = G[ny][nx]
            if sign != nsign:
                edgeset.add(((y+ny)/2, (x+nx)/2, c))
                edges += 1
            elif (ny, nx) not in visited:
                r = traverse(G, ny, nx, sum_signs, visited, edgeset)
                edges += r[0]
                sum_signs = r[1]
        else:
            edgeset.add(((y+ny)/2, (x+nx)/2, c))
            edges += 1
            
    if sum_signs_orig == 0 and p2:
        # print(edgeset)
        new_edges = 0
        while not len(edgeset) == 0:
            ye, xe, ce = edgeset.pop()
            new_edges += 1
            for yy, xx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                yn = ye+yy if ye%1==0 else ye
                xn = xe+xx if xe%1==0 else xe
                while (yn, xn, ce) in edgeset:
                    edgeset.remove((yn, xn, ce))
                    yn = yn+yy if ye%1==0 else ye
                    xn = xn+xx if xe%1==0 else xe
        return new_edges, sum_signs

    return edges, sum_signs

visited = set()

s = 0
for y, line in enumerate(G):
    for x, cell in enumerate(line):
        if (y, x) not in visited:
            visited.add((y,x))
            edges, sums = traverse(G, y, x, 0, visited, edgeset = set())
            s += sums*edges
            # exit()

print(s)
