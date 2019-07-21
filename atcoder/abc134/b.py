import math


def LI(): return list(map(int, input().split()))


n, d = LI()
a = n // (2*d + 1)
b = (n % (2*d + 1)) / (2*d + 1)

print(a + math.ceil(b))
