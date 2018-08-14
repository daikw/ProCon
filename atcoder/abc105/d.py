import math, string, fractions, heapq, re, array, bisect, sys, random, time, copy
import itertools as it
import collections as cl
import functools as ft
import numpy as np

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def count_lr(n, m, a):
    count = 0
    for l in range(n):
        for r in range(l, n):
            if not sum(a[l:r+1]) % m:
                count += 1
    return count


if __name__ == "__main__":
    n, m = LI()
    a = LI()

    print(count_lr(n, m, a))
