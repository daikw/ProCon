n, m = map(int, input().split())

state = ''
result = []
for _ in range(m):
    d_, p_ = input().split()
    if '#' in d_:
        if state != '#_':
            if d_.replace('#', '+') == p_:
                state = '#'
            else:
                state = '#_'
    else:
        if state == '#':
            result.append(1)
            state = ''
        elif state == '#_':
            result.append(0)
            state = ''
        if d_ == p_:
            result.append(1)
        else:
            result.append(0)


import re
correct = re.sub(r'0+', '0', ''.join(map(str, result)))
print(max(map(len, correct.split('0'))))

