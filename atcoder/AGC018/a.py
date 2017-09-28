# coding: utf-8

if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse = True)

    if k >= max(a):
        print('IMPOSSIBLE')

    elif k in a:
        print('POSSIBLE')

    else:
        s = set([ai - aj for ai, aj in zip(a[:-1], a[1:])])
        while True:
            if 1 in s or k in s:
                print('POSSIBLE')
                break
            else:
                if k >= max(s)
                s = set([si - sj for si, sj in zip(s[:-1], s[1:])])

