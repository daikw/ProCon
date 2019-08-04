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

# print(abc)

S = [
    [0, 1],
    [0, 2],
    [1, 0],
    [1, 2],
    [2, 0],
    [2, 1],
]

T = [
    [[1, 1], [2, 2]],
    [[0, 0], [2, 2]],
    [[0, 0], [1, 1]]
]

def solve(abc):
    dp = np.zeros((N, 3), dtype='int32')  # [[Ai, Bi, Ci]...]

    for j in range(3):
        dp[0][j] = abc[0][j]
    if N == 1:
        return dp

    for j in range(3):
        dp[1][j] = max(abc[0]) + abc[1][j]
    if N == 2:
        return dp

    for i in range(N-2):
        for j in range(3):
            pattern = S + T[j]
            next = [dp[i][j] + abc[i+1][j_] for j, j_ in pattern]
            # print(i, j, next)
            dp[i+2][j] = max(next) + abc[i+2][j]

    return dp

# print(abc)
print(max(solve(abc)[N-1]))


"""
https://atcoder.jp/contests/dp/submissions/6666864

WAが消えないけど、多分テストケースが間違っている。
TLEはループをなんとかするか、ステップを半分にすれば解決しそう


--------------->> 問題を勘違いしてた……
"""
