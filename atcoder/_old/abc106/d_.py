import numpy as np


def LI(): return list(map(int, input().split()))
def LI_(): return list(map(lambda x: int(x) - 1, input().split()))


def cumulative_sum_ref(d1_array):
    for i in range(1, len(d1_array)):
        d1_array[i] += d1_array[i-1]


def cumulative_sum_val(d1_array):
    tmp = d1_array.copy()
    for i in range(1, len(tmp)):
        tmp[i] += tmp[i-1]
    return tmp


# 累積和の計算方法が遅すぎるっぽい。
if __name__ != "__main__":
    N, M, Q = LI()
    LR = np.zeros((N+1, N+1), dtype='uint32')
    for i in range(M):
        l, r = LI()
        LR[l][r] += 1

    # 二次元累積和
    for i in range(1, N+1):
        for j in range(2, N+1):
            LR[i][j] += LR[i][j-1]
    for i in range(1, N+1):
        for j in range(2, N+1):
            LR[j][i] += LR[j-1][i]

    for _ in range(Q):
        p, q = LI()
        p -= 1
        result = LR[q][q] - LR[p][q] - LR[q][p] + LR[p][p]
        print(result)


if __name__ == "__main__":
    N, M, Q = LI()
    LR = np.zeros((N+1, N+1), dtype='uint32')
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
