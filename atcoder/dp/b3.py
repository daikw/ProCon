import numpy as np
def LI(): return list(map(int, input().split()))


N, K = LI()
h = np.array(LI(), dtype='int32')
dp = np.zeros(N, dtype='int32')
 
for i in range(1, N):
  start = 0 if i < K else i-K
  dp[i] = np.min(dp[start:i] + np.abs(h[i]-h[start:i]))
 
print(dp[-1])


"""
https://atcoder.jp/contests/dp/submissions/5878626
をほぼコピペ。n<k, i<=kのケースもまとめて扱うのかしこぃ……
"""
