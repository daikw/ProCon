import itertools as it
from heapq import heappop, heappush


# 2次元配列で定義された有向グラフgraphにおいて、ノード(s, g)間の最短距離を返す
def dijkstra1(s, g, graph):
    q, seen = [(0, s, ())], set()
    while q:
        (cost, load, v1, path) = heappop(q)
        if (v1, load) not in seen:
            seen.add((v1, load))
            path += (v1,)
            if v1 == t and load:
                return path
            y, x = v1


# s: start / g: goal



# 全ノードを通過する場合の最短距離を返す
def dijkstra2(graph):
    pass


n, m, r = map(int, input().split())
ri = list(map(int, input().split()))


# 有向グラフを無向グラフへ
graph = [[0]*n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    graph[a][b] = c
    graph[b][a] = c

# グラフを縮約
graph2 = [[0]*r for _ in range(r)]
for i, j in it.combinations(ri, 2):
    i, j = i-1, j-1
    ij_dist = dijkstra(i, j, graph)
    graph2[i][j] = ij_dist
    graph2[j][i] = ij_dist

print(dijkstra2(graph2))
