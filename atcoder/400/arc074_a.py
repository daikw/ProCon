import math
c, f = math.ceil, math.floor

def diff(arr):
    return max(arr) - min(arr)


def solve(h, w):
    if h%3 == 0 or w%3 == 0:
        return 0

    ps = [
        [h*c(w/3), c(h/2)*(w-c(w/3)), (h-c(h/2))*(w-c(w/3))],
        [h*c(w/3), f(h/2)*(w-c(w/3)), (h-f(h/2))*(w-c(w/3))],
        [h*f(w/3), c(h/2)*(w-f(w/3)), (h-c(h/2))*(w-f(w/3))],
        [h*f(w/3), f(h/2)*(w-f(w/3)), (h-f(h/2))*(w-f(w/3))],
        [w*c(h/3), c(w/2)*(h-c(h/3)), (w-c(w/2))*(h-c(h/3))],
        [w*c(h/3), f(w/2)*(h-c(h/3)), (w-f(w/2))*(h-c(h/3))],
        [w*f(h/3), c(w/2)*(h-f(h/3)), (w-c(w/2))*(h-f(h/3))],
        [w*f(h/3), f(w/2)*(h-f(h/3)), (w-f(w/2))*(h-f(h/3))],
        [h*c(w/3), h*c(w/3), h*(w-2*c(w/3))],
        [h*c(w/3), h*f(w/3), h*(w-c(w/3)-f(w/3))],
        [h*f(w/3), h*f(w/3), h*(w-2*f(w/3))],
        [w*c(h/3), w*c(h/3), w*(h-2*c(h/3))],
        [w*c(h/3), w*f(h/3), w*(h-c(h/3)-f(h/3))],
        [w*f(h/3), w*f(h/3), w*(h-2*f(h/3))],
    ]
    values = [diff(p) for p in ps]
    return min(values)

h, w = list(map(int, input().split()))
print(solve(h, w))

"""
"""
