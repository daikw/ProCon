def LI(): return list(map(int, input().split()))
inf = float('inf')

n, k = LI()
h = LI()

# init
dp = [inf] * k + [0] * n
d = [[inf] * j + [abs(h[i+j] - h[i]) for i in range(n-j)] for j in range(1, k+1)]

# calc
for i in range(1, n):
    d_i = [dp[i-j+k] + d[j-1][i] for j in range(1, k+1)]
    dp[i+k] = min(d_i)

print(dp[-1])


"""
TLE
他の人のを読むと、これの2倍くらい高速にしないと通らないっぽい。
infが絡む計算が結構重そう…？
"""
