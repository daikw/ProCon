L = int(input())

n = len(bin(L)) - 2

dag = []
for i in range(n)[::-1]:
    dag.append(' '.join(map(str, [i, i+1, 2**i])))
    dag.append(' '.join(map(str, [i, i+1, 0])))

m = 2*(n-1)
' '.join(map(str, [n, m]))

print('\n'.join(dag))
