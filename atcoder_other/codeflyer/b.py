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

a, b, n = LI()
x = S()

for letter in x:
    if a < 0 and b < 0:
        break
    elif letter == 'S':
        a -= 1
    elif letter == 'C':
        b -= 1
    else:
        if a >= b:
            a -= 1
        else:
            b -= 1

a = max(a, 0)
b = max(b, 0)

print(a)
print(b)

