from sys import argv

S = open(argv[1]).read().split('\n')
S.pop()
S = [[s.split()[0], tuple(map(int, s.split()[1].split(',')))] for  s in S]
P2 = [['?'.join([springs]*5), tuples*5] for springs, tuples in S]

DP = {}
def calc(springs: str, blocks: tuple):
    # print(springs, blocks)
    # input()
    if len(blocks) == 0:
        if '#' not in springs:
            # print('if1-return 1')
            return 1
        else:
            # print('if1-return 0')
            return 0
    if len(springs) == 0 and len(blocks) > 0:
        # print('if2-return 0')
        return 0

    if (springs, blocks) in DP:
        return DP[(springs, blocks)]
    
    result = 0

    if springs[0] in '.?':
        result += calc(springs[1:], blocks)

    if '.' not in springs[:blocks[0]] and (len(springs) == blocks[0] or (len(springs) > blocks[0] and springs[blocks[0]] != '#')):
        result += calc(springs[blocks[0]+1:], blocks[1:])

    DP[(springs, blocks)] = result
    return result

print(sum(calc(s, b) for s, b in S))
print(sum(calc(s, b) for s, b in P2))


# print(calc('?###????????', (3,2,1)))