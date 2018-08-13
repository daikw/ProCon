n = int(input())

flg = False
neg, i = 0, 0
while neg < n:
    neg = i * 4
    if (n - neg) % 7 == 0:
        flg = True

    i += 1

if flg:
    print('Yes')
else:
    print('No')
