import numpy as np

a = np.array([[j*10+i for i in range(15)] for j in range(10)])

print(a)

for i, line in enumerate(a):
    for j, cell in enumerate(line):
        print(a[i][j], cell)