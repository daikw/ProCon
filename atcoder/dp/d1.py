import os, sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")
 
sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10**18
MOD = 10**9 + 7

def N(): return int(sys.stdin.readline())
def li(): return list(map(int, sys.stdin.readline().split()))
def bulk_li(): return list(map(lambda s: list(map(int, s.split())), sys.stdin.readlines()))

n, w = li()
wv = bulk_li()

# print(wv)
table = dict()

# 以下の条件で最大の価値の総和を返す
# i番目以降(i+1..n)の品物 / 残重量jのナップサック
def dp(i, j):
    if i == n:
        return 0
    if (i, j) in table:
        return table.get((i, j))

    w, v = wv[i]
    if w > j:
        return dp(i+1, j)

    table[(i, j)] = max(v + dp(i+1, j-w), dp(i+1, j))
    return table[(i, j)]

print(dp(0, w))


"""
TLE
https://atcoder.jp/contests/dp/submissions/6675353

recursionでやると遅い。
"""
