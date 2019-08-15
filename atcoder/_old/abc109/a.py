import sys
def LI(): return [int(x) for x in sys.stdin.readline().split()]


a, b = LI()

if a % 2 == b % 2 == 1:
    print('yes')
else:
    print('no')
