import sys

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()



if __name__ == "__main__":
    n = I()
    a = sorted(LI())

    if len(a) % 2 != 0:
        print(a[n // 2 + 1])
    else:
        print(a[n // 2])
