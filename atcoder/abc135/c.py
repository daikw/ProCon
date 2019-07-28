def LI(): return list(map(int, input().split()))

n = int(input())
a = LI()
b = LI() + [0]

count = 0
for i in range(n):
    diff1 = min(b[i], a[i])
    b[i] -= diff1
    count += diff1

    diff2 = min(b[i], a[i+1])
    a[i+1] -= diff2
    count += diff2

print(count)
