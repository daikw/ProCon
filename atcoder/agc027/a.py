import sys
import bisect
import itertools as it
def LI(): return [int(x) for x in sys.stdin.readline().split()]


n, x = LI()
a = LI()
a.sort()
if x == sum(a):
    print(n)
elif x > sum(a):
    print(n-1)
else:
    i = bisect.bisect_right([y for y in it.accumulate(a)], x)
    print(i)
