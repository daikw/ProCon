n = int(input())
a = {}
for i in range(n):
    a[i] = int(input())

max_i, MAX = max(a.items(), key=lambda x: x[1])
del a[max_i]

SECOND = max(a.values())


for i in range(n):
    if i == max_i:
        print(SECOND)
    else:
        print(MAX)
