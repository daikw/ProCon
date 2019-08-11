import re

s = input()

p = re.compile('R+L+')
p2 = re.compile('RL')
flagments = re.findall(p, s)

result = []
for el in flagments:
    length = len(el)
    il, _ = p2.search(el).span()

    r = l = length // 2
    if length % 2 == 0:
        pass
    elif il % 2 == 0:
        r += 1
    else:
        l += 1
    
    result.extend([0]*il + [r, l] + [0]*(length - il - 2))

print(' '.join(map(str, result)))
