n = input()
f = sum([int(el) for el in n])

if int(n)%f == 0:
    print('Yes')
else:
    print('No')