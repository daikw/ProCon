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


def main(d, g, p, c):
    counts = []
    for choice in it.product(*[[0, 1]]*10):
        count = sum([p_ * flg for p_, flg in zip(p, choice)])
        total = sum([p_ * (100*i) for p_, i in zip(p, range(1, d+1))])
        if total >= g:
            counts.append(count)
        elif choice != [1] * d:
            i = d - choice[::-1].index
            part_count = (g - total) // (100 * i) + 1
            if part_count > 0:
                counts.append(count + part_count)

    return min(counts)


if __name__ == "__main__":
    d, g = LI()
    p = []
    c = []
    for _ in range(d):
        p_, c_ = LI()
        p.append(p_)
        c.append(c_)

    # print(main(d, g, p, c))
    counts = []
    for choice in it.product(*[[0, 1]]*d):
        count = sum([p_ * flg for p_, flg in zip(p, choice)])
        total = sum([(p_ * 100*i + c_) * flg for p_, i, flg, c_ in zip(p, range(1, d+1), choice, c)])
        # print(choice, count, total)
        if total >= g:
            counts.append(count)
        elif choice != [1] * d:
            i = d - choice[::-1].index(0)
            # print(choice, i)
            part_count = int((g - total) / (100*i))
            if part_count < p[i-1]:
                counts.append(count + part_count)
    print(min(counts))
