def LI(): return list(map(int, input().split()))

n = int(input())
h = LI()

dp = [0] * n
dp[0], dp[1] = 0, abs(h[1] - h[0])
for i in range(2, n):
    dp[i] = min(
        dp[i-1] + abs(h[i] - h[i-1]),
        dp[i-2] + abs(h[i] - h[i-2])
    )

print(dp[-1])


"""
137 ms	13928 KB
割と簡単なDPだが、添字には注意。
"""
