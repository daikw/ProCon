import sys
def LI(): return [int(x) for x in sys.stdin.readline().split()]

n, a, b = LI()
print(min(n*a, b))