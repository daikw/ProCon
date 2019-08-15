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


a, b, c, x, y = LI()


if 2*c <= a + b:
    if x > y:
        if a <= 2 * c:
            result = a * (x - y) + 2 * c * y
        else:
            result = 2 * c * max(x, y)
    elif x < y:
        if b <= 2 * c:
            result = b * (y - x) + 2 * c * x
        else:
            result = 2 * c * max(x, y)
    else:
        result = 2 * c * max(x, y)
else:
    result = a * x + b * y

print(result)