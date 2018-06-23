import math, string, fractions, heapq, re, array, bisect, sys, random, time, copy
import itertools as it
import collections as cl
import functools as ft


def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

import numpy as np

n, d = LI()
x = np.array(LI())
diffs = x[1:] - x[:-1]
count = 0

for i in range(1, n-1):
    ld, rd = diffs[i-1], diffs[i]
    lc, rc = 0, 0
    for li in reversed(range(0, i+1)):
        if ld > d:
            break
        else:
            lc += 1
            ld += diffs[li]
    for ri in range(i, n):
        if rd > d:
            break
        else:
            rc += 1
            rd += diffs[ri]
    print(i, rc, lc)
    count += rc * lc

print(count)




