import collections as col


n = int(input())
ary = []
for _ in range(n):
    ary.append(input())

ary = col.Counter(ary)

print(len([v for v in ary.values() if v%2 != 0]))
