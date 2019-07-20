def LI(): return list(map(int, input().split()))

n, l = LI()
apples = []
for i in range(n):
    apples.append(l + i)

minabs = min([abs(a) for a in apples])

if minabs in apples:
    print(sum(apples) - minabs)
else:
    print(sum(apples) + minabs)
