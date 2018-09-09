n = int(input())
w = []
for _ in range(n):
    w.append(input())

judge = len(w) == len(set(w))

for pre, post in zip(w[:-1], w[1:]):
    judge &= pre[-1] == post[0]

if judge:
    print('Yes')
else:
    print('No')
