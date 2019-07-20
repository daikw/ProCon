import itertools as it
def LI(): return list(map(int, input().split()))

def explain(n, k):
    l = (n-1) * (n-2) // 2 - k
    print(n-1 + l) # M

    # loop
    for i in range(2, n+1):
        print(1, i)

    # lessen 2 distance pairs
    count = 0
    for i, j in it.combinations(range(2, n+1), 2):
        if count >= l:
            break
        print(i, j)
        count += 1


n, k = LI()

if k > (n-1) * (n-2) // 2:
    print(-1)
else:
    explain(n, k)
