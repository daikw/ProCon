import sys

def LI(): return [int(x) for x in sys.stdin.readline().split()]


x = LI()

print(1728 * x[0] + 144 * x[1] + 12 * x[2] + x[3])