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
"""
7
6 7 8
8 8 3
2 5 2
7 8 6
4 6 8
2 3 4
7 5 1

--> 46
"""

# print(abc)
pattern = 'CABBCCA'
translate = {'A': 0, 'B': 1, 'C': 2}

s = sum([
  abc[i][j] for i, j in zip(
    range(N),
    [translate[letter] for letter in pattern]
	)
])
print(s) # 48

"""
"""
