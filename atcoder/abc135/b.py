def LI(): return list(map(int, input().split()))
n = int(input())
p = LI()
q = [i for i in range(1, n+1)]

diff = 0
for i in range(n):
    if p[i] != q[i]:
        diff += 1

if diff == 2 or diff == 0:
    print('YES')
else:
    print('NO')
