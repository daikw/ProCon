import sys
def LI(): return [int(x) for x in sys.stdin.readline().split()]


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_(list):
    result = list[0]
    for el in list[1:]:
        result = gcd(result, el)
    return result


n, x = LI()
X = LI()

X.append(x)
X.sort()

X_ = [post - pre for pre, post in zip(X[:-1], X[1:])]

print(gcd_(X_))
