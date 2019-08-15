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


for n in range(1, 10000):
    if str(n)[1:] == '9'*(len(str(n))-1):
        sn = sum(map(int, str(n)))
        print(n, sn, round(n/sn, 3))


k = int(input())
sunuke = []
for digit in range(k//9+1):
    sunuke.extend([int(str(i)+'9'*digit) for i in range(1, 10)])

for i in range(k):
    print(sunuke[i])
