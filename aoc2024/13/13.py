import numpy as np
import sys

# a*94 + b*34 = 8400
# a*22 + b*67 = 5400

# a = np.array([[10, 5], [20, 10]])
# b = np.array([10, 0])

# x = np.linalg.solve(a,b)

# print(x)

# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400

E = []

with open(sys.argv[1]) as file:
    eq = []
    A = []
    B = []
    for line in file:
        if 'Button' in line:
            a, b = tuple(map(int,[x.split('+')[1] for x in line.strip().split(': ')[1].split(', ')]))
            A.append(a)
            B.append(b)
        if 'B' in line:
            eq = [[A, B]]
        if 'Prize' in line:
            prize = list(map(int,[x.split('=')[1] for x in line.strip().split(': ')[1].split(', ')]))
            eq.append(prize)
            E.append(eq)
            eq = []
            A = []
            B = []

#    x1  x2    y1  y2     xp    yp
# [[[94, 22], [34, 67]], [8400, 5400]]
# A*x1 + B*x2 = xp
# A*y1 + B*y2 = yp

def solve_linalg(E, p2):
    """solves linear equation with two unknown variables using np.linalg.solve function"""
    p1 = 0
    for system in E:
        eq, r = np.array(system[0]), np.array(system[1])
        if p2:
            r = [i+10000000000000 for i in r]
        res = np.linalg.solve(eq, r)
        # Attention here!
        # the result of np.linalg.solve consists of float64 numbers
        # possible error:
        # 0.9999999 % 1 == 0.9999999
        # so for a number x to check if x is an int we have to do:
        # abs(round(x)-x) < 0.001
        is_possible = all([abs(np.round(x)-x) <= 0.01 for x in res])
        if is_possible:
            # assert((res<=100).all())
            tokens = 3*np.round(res[0]) + np.round(res[1])
            p1 += int(tokens)
            # print(res, tokens)
    return p1

def own_solve(E, p2):
    """
    solves linear equation with two unknown variables
    we solve by eliminating one variable and inserting into the equation
    """
    p1 = 0
    for system in E:
        eq, r = system[0], system[1]
        x1, x2 = eq[0]
        y1, y2 = eq[1]
        xp, yp = r
        if p2:
            xp += 10000000000000
            yp += 10000000000000
        # print(x1, x2, y1, y2, xp, yp)
        A = (xp*y2 - yp*x2) / (x1*y2 - y1*x2)
        B = (yp - A*y1) / y2
        
        if A%1==0 and B%1==0:
            tokens = 3*int(A)+int(B)
            p1 += tokens

    return p1

p2 = [False, True]

for p in p2:
    print(solve_linalg(E, p))
    print(own_solve(E, p))