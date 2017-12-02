import math, string, fractions, heapq, re, array, bisect, sys, random, time, copy
import itertools as it
import collections as cl
import functools as ft


sys.setrecursionlimit(10**7)
inf = 10**20
gosa = 1.0 / 10**10
mod = 10**9+7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def main():
    n, c = LI()
    l = []
    for _ in range(n):
        l.append(I())

    l.sort()

    count = 0
    while l:
        lmax = l[-1]

        le, ri = 0, len(l)-2

        if l[le] > c - lmax:
            count += 1
            l.pop()
            continue

        while le <= ri:
            mid = (le + ri) // 2
            if
            elif l[mid] < c - lmax:
                le = mid + 1
            else:
                ri = mid - 1

        l.pop(mid)
        l.pop()

        count += 1

    return count

print(main())



