#!/bin/python3

from itertools import groupby

with open('input.in') as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]

seeds = [int(s) for s in lines.pop(0).split()[1:]]

maplist = [list(group) for k, group in groupby(lines, lambda x: x == '') if not k]
maps = {}

for m in maplist:
    n = m.pop(0).split()[0].split('-')
    src_name, dest_name = n[0], n[-1]
    m = [list(map(int,x.split())) for x in m]          # convert to list of lists of ints
    m.sort(key=lambda x: x[1])                         # sort by middle element (source range start)
    maps[src_name] = {'dest': dest_name, 'map': m, 'max_el': m[-1][1]+m[-1][2]-1, 'min_el': m[0][1]}

for m in maps:
    print(m, maps[m])
    print()

# map is a list of lists of ints
# sorted by src_range_start
# [[dest_range_start, src_range_start, range_length], [...], ...] ]
def lookup_in_map(seed, map, max_el, min_el):
    if seed > max_el or seed < min_el:
        return seed                     # mapped to it self
    i = 0
    wanted_map = map[i]
    while wanted_map[1] + wanted_map[2] <= seed:
        i += 1
        wanted_map = map[i]
    # assert(wanted_map[1] <= seed and wanted_map[1] + wanted_map[2] > seed)

    diff = seed - wanted_map[1]
    return wanted_map[0] + diff

def convert(src_name, dest_name, seed):
    d = maps[src_name]['dest']
    m = maps[src_name]['map']
    while d != dest_name:
        seed = lookup_in_map(seed, m, maps[src_name]['max_el'], maps[src_name]['min_el'])
        src_name = d
        d = maps[src_name]['dest']
        m = maps[src_name]['map']
    
    seed = lookup_in_map(seed, m, maps[src_name]['max_el'], maps[src_name]['min_el'])
    
    return seed

o = []
for i in seeds:
    o.append(convert('seed', 'location', i))
    
print(min(o))