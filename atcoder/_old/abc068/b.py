# coding: utf-8

if __name__ == "__main__":
    n = int(input())
    r = 0
    while 2**r <= n:
        r += 1

    r -= 1

    print(2**r)

