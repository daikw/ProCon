def LI(): return list(map(int, input().split()))

n = int(input())
pair = []
for _ in range(n):
    _a, _b = LI()
    pair.append((_b, _a))

pair.sort()

acc = 0
last_b = 0
for b, a in pair:
    acc += (b - last_b) - a
    last_b = b

    if acc < 0:
        print('No')
        break
else:
    print('Yes')
