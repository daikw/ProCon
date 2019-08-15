n = int(input())
s1 = input()
s2 = input()

if s1[0] == s2[0]:
    res = 3
    state = 'v'
else:
    res = 6
    state = 'h1'


for i in range(1, n):
    if s1[i] == s2[i]: # if vertical
        if state == 'v':
            res = 2 * res % 1000000007
        else:
            pass

        state = 'v'

    else: # if horizontal
        if state == 'h1':
            state = 'h2'

        elif state == 'h2':
            res = 3 * res % 1000000007
            state = 'h1'

        elif state == 'v':
            res = 2 * res % 1000000007
            state = 'h1'

print(res)