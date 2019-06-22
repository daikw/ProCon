import numpy as np


def LI(): return list(map(int, input().split()))
comparator = lambda x: x >= k

n, k = LI()
a = LI()

sums = np.array([sum(a[0:i]) for i in range(n+1)])
print(sums)

count, i = 0, 0
while i <= n:
    c = sum(np.apply_along_axis(comparator, 0, sums))
    sums -= sums[c]
    i += c
    print(sums)


print(count)
