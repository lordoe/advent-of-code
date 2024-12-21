
import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

lines = [list(line.strip()) for line in lines]

empt_rows = []
for i, line in enumerate(lines):
    if not '#' in line:
        empt_rows.append(i)

empt_cols = []
for i in range(len(lines[0])):
    for j in range(len(lines)):
        if lines[j][i] == '#':
            break
    else:
        empt_cols.append(i)

for i in reversed(empt_rows):
    lines.insert(i, ['.'] * len(lines[0]))

for i in reversed(empt_cols):
    for j in range(len(lines)):
        lines[j].insert(i, '.')
        
G = []
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == '#':
            G.append((i, j))

G_pairs = []
for i, g in enumerate(G):
    for g2 in G[i+1:]:
        G_pairs.append((g, g2))

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def get_neighbours(pos):
    x, y = pos
    return [(x + dx, y + dy) for dx, dy in dirs]

def eukl_dist(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def next_pos(g1, g2):
    g1_neighbours = get_neighbours(g1)
    g1_neighbours.sort(key=lambda x: eukl_dist(x, g2))
    return g1_neighbours[0]

def shortest_path_len(g1, g2):
    count = 0
    while g1 != g2:
        g1 = next_pos(g1, g2)
        count += 1
    return count

short_paths = [shortest_path_len(g1, g2) for g1, g2 in G_pairs]
print(sum(short_paths))