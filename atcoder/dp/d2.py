import numpy as np
N, W = map(int, input().split())
ndp = np.zeros(W+1, dtype= np.int64)
for _ in range(N):
    w, v = map(int,input().split())

    # 離散より連続で扱った方が問題が簡単になる。
    np.maximum(ndp[:-w] + v, ndp[w:], out = ndp[w:])
print(ndp[-1])


"""
https://atcoder.jp/contests/dp/submissions/6657472
より失敬。
W ~ 10^5 なので、空間計算量もセーフ: 172 ms / 14612 KB

めっちゃスマートな解法。

- なるべくlistやarrayのscanをする回数を減らすべき
- 実行順に関わらず結果が同じになるアルゴリズムを考えると、実装も簡単で処理も早い
- 離散的でなく連続的に捉えると、問題が簡単になることがある
"""
