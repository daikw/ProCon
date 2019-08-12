s = input()
t = input()
ls = len(s)
lt = len(t)

dp = [[None]*lt for _ in range(ls)]

# init
index_t = t.find(s[0]) + 1 if t[0] in t else 0
for j in range(lt):
    if j >= index_t:
        dp[0][j] = 1
    else:
        dp[0][j] = 0

index_s = s.find(t[0]) if t[0] in s else 0
for i in range(ls):
    if i >= index_s:
        dp[i][0] = 1
    else:
        dp[i][0] = 0

# print(dp)

# solve
for i in range(1, ls):
    for j in range(1, lt):
        if s[i] == t[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


# restore
l = dp[-1][-1]
res = ''
i, j = ls-1, lt-1
while l > 0 and (i > 0 or j > 0):
    if i > 0 and dp[i-1][j] == l:
        i -= 1
        # print('i')
    elif j > 0 and dp[i][j-1] == l:
        j -= 1
        # print('j')
    elif dp[i-1][j-1] == l-1:
        res += s[i]
        i, j, l = i-1, j-1, l-1
        # print(i, j, l)

## upper left corner
if l == 1:
    res += s[0]

print(res[::-1])

"""
TLE, WA
エッジケースでWA?
"""
