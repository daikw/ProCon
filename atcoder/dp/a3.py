def LI(): return list(map(int, input().split()))

n = int(input())
h = LI()
h1 = [abs(h[i+1] - h[i]) for i in range(n-1)]
h2 = [abs(h[i+2] - h[i]) for i in range(n-2)]

dp = [0] * n
dp[0], dp[1] = 0, abs(h[1] - h[0])
for i in range(n-2):
    dp[i+2] = min(
        dp[i+1] + h1[i+1],
        dp[i] + h2[i],
    )

print(dp[-1])


"""
148 ms	19064 KB

hの差分計算はなんどもやってないので、それを作るのとdpの計算をするのを別にすると、
余計にコストがかかってしまう
"""
