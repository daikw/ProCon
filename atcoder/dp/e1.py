import numpy as np
N, W = map(int, input().split())
ndp = np.full(1000*100+1, 10**11, dtype=np.int64)
ndp[0] = 0

for _ in range(N):
    w, v = map(int,input().split())

    np.minimum(ndp[:-v] + w, ndp[v:], out = ndp[v:])

print(np.max(np.where(ndp<=W)))

"""
https://atcoder.jp/contests/dp/submissions/6646897
から失敬

貪欲法はこの手の書き方で表現できるっぽい。
価値テープのなかで同価値のindexでは、より少ない重量の物品で済む方を残していく。
したがってテープの初期化は擬似infで行い、価値0の部分は重さも0で始める。

"""
