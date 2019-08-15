mod = 10**9 + 7
h, w = list(map(int, input().split()))

def solve(h, w):
    prev = [None, 1] + [0]*(w-1)

    for _ in range(h):
        line = input()
        # print('line: ', line)
        next = [0] + [None]*w
        for j in range(w):
            if line[j] == '.':
                next[j+1] = (prev[j+1] + next[j]) % mod
            else:
                next[j+1] = 0
        prev = next

        # print(_, next)
    return next[-1]

print(solve(h, w))

"""
AC 283 ms 3064 KB

10^6 (10^3*10^3)だからしんどいかなと思っていたが、案外早かった。
行ごとに破壊的変更をするので、メモリも最低限。

もう一桁上がると無理なので、C++にするしかなさそうっぽい。
np.ufuncのaccumulateをhackすれば行けるかもしれない。。？

"""
