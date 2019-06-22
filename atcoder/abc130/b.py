def LI(): return list(map(int, input().split()))

n, x = LI()
l = LI()

s = [sum(l[0:i]) for i in range(n+1)]
count = sum([x >= i for i in s])

print(count)
