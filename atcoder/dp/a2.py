def LI(): return list(map(int, input().split()))

n = int(input())
h = LI()

dp = [0] * n
dp[0], dp[1] = 0, abs(h[1] - h[0])
for i in range(n-2):
    dp[i+2] = min(
        dp[i+1] + abs(h[i+2] - h[i+1]),
        dp[i] + abs(h[i+2] - h[i])
    )
    # print('i', i, '1step', abs(h[i+1] - h[i]), 'dp1', dp[i+1], '2step', abs(h[i+2] - h[i]), 'dp', dp[i], 'dp2', dp[i+2])

print(dp[-1])
# print(dp)


"""
132 ms	13928 KB
添字に注意。a1と比べて起点が違うので、absの中身の左側が同じやつを使う。
"""
