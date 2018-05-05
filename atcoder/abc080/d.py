import sys
import numpy as np
import itertools as it

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


N, C = LI()
s, t, c = [], [], []
for _ in range(N):
    s_, t_, c_ = LI()
    s.append(s_*2 - 1)
    t.append(t_*2)
    c.append(c_)

left = min(s)
right = max(t)
length = right - left + 1

tape = np.zeros(length)

for i in range(N):
    row = np.array([0]*(s[i]-left) + [1]*(t[i]-s[i]+1) + [0]*(right-t[i]))
    tape += np.array(row)

print(int(max(tape)))
