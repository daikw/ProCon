import math, sys
import functools as ft


def LI(): return [int(x) for x in sys.stdin.readline().split()]


def lcm_base(x, y):
    return int((x * y) / math.gcd(x, y))


def lcm_list(numbers):
    return ft.reduce(lcm_base, numbers, 1)


def calc_f(n, ms):
    s = 0
    for m in ms:
        s += n % m

    return s


n = int(input())
a = LI()

print(calc_f(lcm_list(a)-1, a))
