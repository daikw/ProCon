
# coding: utf-8
import numpy as np

if __name__ == "__main__":
	n, m = map(int, input().split())

	mat = [[0]*n for _ in range(n)]
	for _ in range(m):
		a, b = map(int, input().split())
		a -= 1; b -= 1
		mat[a][b] += 1
		mat[b][a] += 1

	for i in range(n):
		print(sum(mat[i]))
