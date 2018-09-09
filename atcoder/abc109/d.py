import sys
def LI(): return [int(x) for x in sys.stdin.readline().split()]


h, w = LI()
a = []
for _ in range(h):
    a.append([x%2 for x in LI()])

operations = []
for i in range(h):
    for j in range(w-1):
        if not a[i][j]:
            continue
        else:
            a[i][j+1] ^= 1
            operations.append(' '.join(map(str, [i+1, j+1, i+1, j+2])))

for i in range(h-1):
    if not a[i][-1]:
        continue
    else:
        a[i+1][-1] ^= 1
        operations.append(' '.join(map(str, [i+1, w, i+2, w])))

print(len(operations))
for row in operations:
    print(row)
