## abc032 / C

def LI(): return list(map(int, input().split()))


def solve(s, k):
    # 初期化
    n = len(s)
    maxlen, p  = 0, 1
    l, r = 0, 0
    while l < n:

        # 可能な範囲で、右端を右にスライド
        while r < n and p * s[r] <= k:
            p *= s[r]
            r += 1
            # print(maxlen, p, l, r, s[l:r])
        maxlen = max(maxlen, r - l)

        if l < r:
            # 左端を一つずらす
            p //= s[l]
            l += 1
        else:
            r = l = r + 1

        # print('----------------------------------end')
        # print(maxlen, p, l, r, s[l:r])
        # print('----------------------------------start')

    return maxlen


if __name__ == '__main__':
    n, k = LI()
    s = []
    has_zero = False

    for _ in range(n):
        _s = int(input())
        has_zero = has_zero or _s == 0
        s.append(_s)

    if has_zero:
        print(n)
    else:
        print(solve(s, k))
