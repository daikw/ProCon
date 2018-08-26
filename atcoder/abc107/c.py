import sys

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


if __name__ == "__main__":
    n, k = LI()
    X = LI()
    l_count = sum((x <= 0 for x in X))
    r_count = n - l_count

    if l_count == 0:
        print(X[k-1])
    elif r_count == 0:
        print(abs(X[-k]))
    else:
        times = []
        for i in range(l_count):
            try:
                left = X[l_count - i - 1]
                right = X[l_count + k - i - 2]
                times.append(abs(2 * left) + abs(right))
                times.append(abs(left) + abs(2 * right))
            except:
                continue
        print(min(times))
