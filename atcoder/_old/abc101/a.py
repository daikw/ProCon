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

s = input()
res = 0
for el in s:
    if el == '+':
        res += 1
    else:
        res -= 1

print(res)