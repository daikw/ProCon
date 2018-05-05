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

n, m = LI()
result = {
    (1, 1): 1,
    (1, 2): 0, (2, 1): 0,
    (2, 2): 0
}

if (n, m) in result.keys():
    print(result[(n, m)])
elif n==1 or m==1:
    print(max(n, m)-2)
elif n==2 or m==2:
    print(0)
else:
    print((n-2)*(m-2))