import sys

def LI(): return [int(x) for x in sys.stdin.readline().split()]

if __name__ == "__main__":
    n, i = LI()
    print(n-i+1)