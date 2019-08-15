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


N, T = LI()
C = []
for _ in range(N):
    c, t = LI()
    if t <= T:
        C.append(c)

if C:
    print(min(C))
else:
    print('TLE')
