import sys
def LI(): return [int(x) for x in sys.stdin.readline().split()]


x1, y1, x2, y2 = LI()
res = map(str, [y1-y2+x2, x2-x1+y2, y1-y2+x1, x2-x1+y1])

print(' '.join(res))