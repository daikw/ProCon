from itertools import accumulate as acc
import sys


def main():
    s = sys.stdin.readlines()
    N, M, Q = map(int, s[0].split())
    LR = [[0]*N for _ in [0]*N]
    for l, r in (map(int, e.split()) for e in s[1:M + 1]):
        LR[l - 1][r - 1] += 1

    S = [tuple(acc(reversed(s))) for s in zip(*(acc(x) for x in LR))]
    print('\n'.join(map(str, (S[q - 1][N - p] for p, q in (map(int, e.split()) for e in s[M + 1:])))))


if __name__ == "__main__":
    main()
