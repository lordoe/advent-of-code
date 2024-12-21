# [(0,0), (0,1), (0,2), (0,3) ...]
# [(1,0), (1,1), (1,2), (1,3) ...]
# [(2,0), (2,1), (2,2), (2,3)...]
# [(3,0), (3,1), (3,2), (3,3)...]

import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

M = [list(line.strip()) for line in lines]
#assert len(M) == len(M[0])

start_next = None

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None
        self.count = 0
        self.last_set = "S"
    
    # vert pip extends/reduces x coord, y has to be the same
    def vert_pipe(self, n_pos):
        xn, yn = n_pos
        if self.y != yn:
            return None
        # set direction of this position in the matrix
        # to later determine if inside or outside the loop
        if self.x > xn:
            to_set = "U"    # U = up
        else:
            to_set = "D"    # D = down
        M[xn][yn] = to_set
        self.last_set = to_set

        self.next = (xn + (xn - self.x), self.y)
        self.x, self.y = xn, yn
        return (self.x, self.y)

    # hor pip extends/reduces y coord, x has to be the same
    def hor_pipe(self, n_pos):
        xn, yn = n_pos
        if self.x != xn:
            return None
        M[xn][yn] = self.last_set
        self.next = (self.x, yn + (yn - self.y))
        self.x, self.y = xn, yn
        return (self.x, self.y)

    # 90 deg bend connects north and east 
    # to apply it must: (x < xn and y == y) or (x == xn and y > yn)
    def bend_ne(self, n_pos):
        xn, yn = n_pos
        if not ((self.x < xn and self.y == yn) or (self.x == xn and self.y > yn)):
            return None
        if self.y > yn:
            to_set = "U"
        else:
            to_set = "D"
        M[xn][yn] = to_set
        self.last_set = to_set

        self.next = (xn + (yn - self.y), yn + (xn - self.x))
        self.x, self.y = xn, yn
        return (self.x, self.y)
    
    # 90 deg bend connects north and west
    # to apply it must: (x < xn and y == y) or (x == xn and y < yn)
    def bend_nw(self, n_pos):
        xn, yn = n_pos
        if not ((self.x < xn and self.y == yn) or (self.x == xn and self.y < yn)):
            return None
        if self.y < yn:
            to_set = "U"
        else:
            to_set = "D"
        M[xn][yn] = to_set
        self.last_set = to_set

        self.next = (xn - (yn - self.y), yn - (xn - self.x))
        self.x, self.y = xn, yn
        return (self.x, self.y)

    # 90 deg bend connects south and west
    # to apply it must: (x == xn and y < yn) or (x > xn and y == yn)
    def bend_sw(self, n_pos):
        xn, yn = n_pos
        if not ((self.x == xn and self.y < yn) or (self.x > xn and self.y == yn)):
            return None
        if self.x > xn:
            to_set = "U"
        else:
            to_set = "D"
        M[xn][yn] = to_set
        self.last_set = to_set

        self.next = (xn + (yn - self.y), yn + (xn - self.x))
        self.x, self.y = xn, yn
        return (self.x, self.y)
    
    # 90 deg bend connects south and east
    # to apply it must: (x == xn and y > yn) or (x > xn and y == yn)
    def bend_se(self, n_pos):
        xn, yn = n_pos
        if not ((self.x == xn and self.y > yn) or (self.x > xn and self.y == yn)):
            print("hier")
            return None
        if self.x > xn:
            to_set = "U"
        else:
            to_set = "D"
        M[xn][yn] = to_set
        self.last_set = to_set

        self.next = (xn - (yn - self.y), yn - (xn - self.x))
        self.x, self.y = xn, yn
        return (self.x, self.y)

    def __getitem__(self, i):
        if i == 0:
            return self.x
        elif i == 1:
            return self.y
        else:
            raise IndexError("Index out of range")
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

    def apply(self, next_pos, first=False):
        x, y = next_pos
        pipe = M[x][y]

        if pipe == "S":
            return "S"
        
        elif pipe not in ["|", "-", "L", "J", "7", "F"]:
            return None

        if pipe == "|":
            ret = self.vert_pipe(next_pos)
        elif pipe == "-":
            ret = self.hor_pipe(next_pos)
        elif pipe == "L":
            ret = self.bend_ne(next_pos)
        elif pipe == "J":
            ret = self.bend_nw(next_pos)
        elif pipe == "7":
            ret = self.bend_sw(next_pos)
        elif pipe == "F":
            ret = self.bend_se(next_pos)

        if ret != None:
            self.count += 1

        if first:
            global start_next
            start_next = ret

        return ret
        
    def apply_dir(self, dir):
        return self.apply((self.x + dir[0], self.y + dir[1]), True)
    
    def apply_next(self):
        if self.next is None:
            print(f"error: next is NONE")
            exit(1)
        return self.apply(self.next)

s: Pos = None
s_line = None
s_col = None

for i, l in enumerate(M):
    if "S" in l:
        s_line = i
        s_col = l.index("S")
        s = Pos(s_line, s_col)

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for d in dirs:
    if s.apply_dir(d) is not None:
        break

# print(f"pos: {(s.x, s.y)} \t {M[s.x][s.y]}")

while s.apply_next() != "S":
    start_prev = (s.x, s.y)
    #print(f"pos: {(s.x, s.y)} \t {M[s.x][s.y]}")
    pass
    #print(f"next: {s.next} \t {M[s.next[0]][s.next[1]]}\n")

print(start_prev, start_next)

# set start direction after completing the loop
M[s_line][s_col] = "D" if start_prev[0] < start_next[0] else "U"

for m in M:
    print(m)
    
counter = 0

for m in M:
    open = False
    last_key = None
    for f in m:
        if f in ["U", "D"] and f != last_key:
            open = not open
            last_key = f    
        elif f not in ["S", "U", "D"] and open: # count all elements inside the loop
            counter += 1


print(counter)
