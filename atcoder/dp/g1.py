import sys

sys.setrecursionlimit(2147483647)

n, m = list(map(int, input().split()))

def solve(n, m):
    graph = dict()
    table = [None]*n

    for _ in range(m):
        x, y = map(int, input().split())
        graph.setdefault(x-1, [])
        graph[x-1].append(y-1)

    # print(graph)

    # 頂点iからの先のグラフの、最大pathの大きさを返す
    def dp(i):
        # print('b', i, table)
        if table[i]:
            return table[i]

        childs = graph.get(i)
        if not childs:
            table[i] = 0
        else:
            table[i] = max([dp(y) for y in childs]) + 1

        # print('a', i, table)
        return table[i]

    for i in range(n):
        dp(i)

    return max(filter(lambda x: x, table))

print(solve(n, m))

"""
AC 962 ms
https://atcoder.jp/contests/dp/submissions/6893109

10**5程度の組み合わせなら、dictで十分ぽい
"""
