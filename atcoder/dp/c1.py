import os, sys
import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")
 
sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10**18
MOD = 10**9 + 7

def n(): return int(sys.stdin.readline())
def li(): return list(map(int, sys.stdin.readline().split()))
def bulk_li(): return list(map(lambda s: list(map(int, s.split())), sys.stdin.readlines()))

N = n()
abc = bulk_li()  # [[a_i, b_i, c_i]...]

dp = np.zeros((N, 3), dtype='int32')  # [[Ai, Bi, Ci]...]
fl = np.zeros((N, 3), dtype='int32')  # [[fl_ai, fl_bi, fl_ci]...]
choice = np.ones((3,3)) - np.diag([1]*3)

for j in range(3):
    dp[0][j] = abc[0][j]

for i in range(1, N):
    for j in range(3):
        candid = dp[i-1]
        if fl[i-1][j] == 1:
            candid *= choice[j]
        if i == 1:
            print('choiced', i-1, j, fl[i-1])
            print('dp', np.max(candid), abc[i][j])

        dp[i][j] = np.max(candid) + abc[i][j]
        fl[i][np.argmax(candid)] = 1

print(abc)
print(fl)
print(dp)
print(max(dp[N-1]))


"""
WA
candidの抽出のあたりがまだおかしい
"""
