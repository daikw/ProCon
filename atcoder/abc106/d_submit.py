def LI(): return list(map(int, input().split()))
def LI_(): return list(map(lambda x: int(x) - 1, input().split()))


if __name__ == "__main__":
    N, M, Q = LI()
    LR = [[0]*(N+1) for _ in range(N+1)]
    for i in range(M):
        l, r = LI()
        LR[l][r] += 1

    # 二次元累積和
    for i in range(1, N+1):
        for j in range(1, N+1):
            LR[i][j] += LR[i][j-1]
            LR[i][j] += LR[i-1][j]
            LR[i][j] -= LR[i-1][j-1]

    for _ in range(Q):
        p, q = LI()
        p -= 1
        result = LR[q][q] - LR[p][q] - LR[q][p] + LR[p][p]
        print(result)
