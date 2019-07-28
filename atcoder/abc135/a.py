def LI(): return list(map(int, input().split()))
a, b = LI()
a, b = min(a, b), max(a, b)

d = b - a
if d % 2 == 0:
  print(a + d // 2)
else:
  print('IMPOSSIBLE')
