MOD = 10**9 + 7

s = input()
n = len(s)

s = [-1 if s[i] == '?' else int(s[i]) for i in range(n)]
dp = [[0] * 13 for _ in range(n+1)]

dp[0][0] = 1
for i in range(n):
    c = s[i] 
    for dk in range(130): # digit_kisu, digit = dk % 10, kisu = dk // 10
        if not (c == -1 or c == dk % 10): continue
        dp[i+1][dk % 13] += dp[i][dk // 10]

    for kisu in range(13):
        dp[i+1][kisu] %= MOD

print(dp[n][5])
