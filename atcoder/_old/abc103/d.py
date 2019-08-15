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


n, m = LI()
ab = []
weight = np.zeros((1, n))

for i in range(m):
    a, b = LI()
    weight[0][a:b] += 1
    ab.append((a, b))

# print(weight)
count = 0
checked = []
while np.sum(weight) > 0:
    max_index = np.argmax(weight)
    # print('max_index: ', max_index)
    # print('--------------')
    for i, (a, b) in enumerate(ab):
        if (a <= max_index < b) and i not in checked:
            checked.append(i)
            weight[0][a:b] -= 1
            # print(weight)
    count += 1

print(count)
