import sys
def LI(): return [int(x) for x in sys.stdin.readline().split()]


n, k = LI()

print((n//k)**3 + (1-k%2)*((n - k//2)//k+1)**3)