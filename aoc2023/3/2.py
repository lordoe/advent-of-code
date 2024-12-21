#!/bin/python3

mat = []

with open('input.in') as f:
    while True:
        line = f.readline()
        if not line:
            break
        mat.append(list(line.strip()))

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

dim = len(mat)
used = [[False for _ in range(dim)] for _ in range(dim)]

# access like 
# mat[row][col]

sum = 0
collect = []
gears = []
for i, row in enumerate(mat):
    for j, cell in enumerate(row):
        if cell == '*':
            for dir in dirs:
                i_temp = i + dir[0]
                j_temp = j + dir[1]
                if i_temp >= 0 and i_temp < dim and j_temp >= 0 and j_temp < dim:
                    if mat[i_temp][j_temp].isdigit() and not used[i_temp][j_temp]:
                        t = j_temp
                        while t > 0 and mat[i_temp][t - 1].isdigit():
                            t -= 1
                        while t < dim and mat[i_temp][t].isdigit():
                            collect.append(mat[i_temp][t])
                            used[i_temp][t] = True
                            t += 1
                        gears.append(int(''.join(collect)))
                        collect = []
            if len(gears) == 2:
                sum += gears[0] * gears[1]
            gears = []

print(sum)