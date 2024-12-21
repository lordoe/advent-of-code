
#!/bin/python3

from itertools import groupby
import bisect

def read_input(file_path):
    with open(file_path) as f:
        seeds = [int(s) for s in next(f).split()[1:]]
        maps = {}
        for key, group in groupby(f, lambda x: x.strip() == ''):
            if not key:
                data = list(group)
                n = data[0].split()[0].split('-')
                src_name, dest_name = n[0], n[-1]
                m = [list(map(int, x.split())) for x in data[1:]]
                m.sort(key=lambda x: x[0])
                first_elements = [x[0] for x in m]
                maps[dest_name] = {
                    'src': src_name,
                    'map': m,
                    'first_elements': first_elements
                }
    return seeds, maps

seeds, maps = read_input('input.in')

seed_pairs = list(zip(seeds[:-1:2], seeds[1::2]))

x = 0

def translate(x):
    state = 'location'
    while state != 'seed':
        first_elements = maps[state]['first_elements']
        # find inner list where x >= list[0] and x < list[0] + list[2]
        # find efficient using bisect
        index = bisect.bisect_right(first_elements, x) - 1
        # print(f'bisect.bisect_right({first_elements}, {x}) -1 = {bisect.bisect_right(first_elements, x) -1}')
        # print(x, state)
        # print(index, len(first_elements))
        # print(first_elements, maps[state]['map'])
        # print()
        if index > -1 and index < len(first_elements):
            if x < maps[state]['map'][index][0] + maps[state]['map'][index][2]:
                x = maps[state]['map'][index][1] + (x - maps[state]['map'][index][0])

        state = maps[state]['src']
    return x

# print(translate(x))
while True:
    t = translate(x)
    for p in seed_pairs:
        if t in range(p[0], p[0]+p[1]):
            print(x)
            exit()  
    x += 1