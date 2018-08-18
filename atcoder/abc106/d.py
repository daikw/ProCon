import math, string, fractions, heapq, re, array, bisect, sys, random, time, copy
import itertools as it
import operator as op
import collections as cl
import functools as ft
import pandas as pd
import numpy as np

def LI(): return list(map(int, input().split()))
def LI_(): return list(map(lambda x: int(x) - 1, input().split()))
def LF(): return list(map(float, input().split()))
def LS(): return input().split()
def I(): return int(input())
def F(): return float(input())
def S(): return input()


if __name__ != "__main__":
    N, M, Q = LI()
    LR = np.ndarray((M, 3), dtype='uint32')

    for i in range(M):
        LR[i][0], LR[i][1] = LI()
        LR[i][2] = i

    L = pd.DataFrame(LR).sort_values(0)
    R = pd.DataFrame(LR).sort_values(1)

    for _ in range(Q):
        l = L.copy()


if __name__ == "__main__":
    N, M, Q = LI()
    LR = np.ndarray((4, M), dtype='uint32')

    for i in range(M):
        LR[0][i], LR[1][i] = LI()

    for _ in range(Q):
        p, q = LI()
        LR[2] = p <= LR[0]
        LR[3] = LR[1] <= q
        print(sum(LR[2]*LR[3]))
