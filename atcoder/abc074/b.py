import sys

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())


def main():
    n = I()
    k = I()
    xs = LI()

    r = 0
    for x in xs:
        r += 2*min(k-x, x)

    return r


print(main())
