import math, string, fractions, heapq, re, array, bisect, sys, random, time, copy
import itertools as it
import collections as cl
import functools as ft

def LI(): return list(map(int, input().split()))
def LI_(): return list(map(lambda x: int(x) - 1, input().split()))
def LF(): return list(map(float, input().split()))
def LS(): return input().split()
def I(): return int(input())
def F(): return float(input())
def S(): return input()


n = I()
X, Y, H = [], [], []

for _ in range(n):
    X_, Y_, H_ = LI()
    X.append(X_)
    Y.append(Y_)
    H.append(H_)


for x, y in it.permutations(range(100), 2):
    h = max(H[0] - abs(x - X[0]) - abs(y - Y[0]), 0)
    for i in range(1, n):
        h_ = max(H[1] - abs(x - X[1]) - abs(y - Y[1]), 0)
        if h == 0 == h_:
            continue
        elif h == h_:
            break

    if h != 0:
        break