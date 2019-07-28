def LI(): return list(map(int, input().split()))
inf = float('inf')

n, k = LI()
h = LI()

# init
dp = [inf] * k + [0] * n
d = [[inf] * j + [abs(h[i+j] - h[i]) for i in range(n-j)] for j in range(1, k+1)]
# print(d)

# calc
for i in range(1, n):
    d_i = []
    for j in range(1, k+1):
        d_i_j = dp[i-j+k] + d[j-1][i]
        # print(i, j, d_i_j, i-j+k, dp[i-j+k], j-1, d[j-1][i])

        d_i.append(d_i_j)

    # print(i, d_i)

    dp[i+k] = min(d_i)
# print(dp)

print(dp[-1])


"""
TLE
"""
