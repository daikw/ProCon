n = int(input())
a, b, c = list(map(int, input().split()))

if n > 1:
    for _ in range(n-1):
        a_, b_, c_ = list(map(int, input().split()))
        a_ += max(b, c)
        b_ += max(a, c)
        c_ += max(a, b)
        a, b, c = a_, b_, c_

print(max(a, b, c))
"""
ちゃんと解いたVer

値を保持しておく必要がない。dpテーブルは必要ない。
"""
