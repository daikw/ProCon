import os, sys
import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")
 
sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10**18
MOD = 10**9 + 7

def N(): return int(sys.stdin.readline())
def li(): return list(map(int, sys.stdin.readline().split()))
def bulk_li(): return list(map(lambda s: list(map(int, s.split())), sys.stdin.readlines()))

a, b, c = li()

print(max(0, c - (a - b)))
