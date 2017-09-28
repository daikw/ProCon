# coding: utf-8
import numpy as np

if __name__ == "__main__":
	n, w = map(int, input().split())
	ws, vs = [], []
	for _ in range(n):
		w_, v_ = map(int, input().split())
		ws.append(w_)
		vs.append(v_)

	# memo: ある価値における最小の重さ / jは価値
	def rec(i, j, memo = [[-1 for _ in range(sum(vs)+1)] for _ in range(n+1)]):

		if memo[i][j] != -1:
			return memo[i][j]

		result = 0
		if i == n:
			result = 0

		elif j < vs[i]:
			result = rec(i+1, j)

		else:
			result = min(
				rec(i+1, j),
				rec(i+1, j-ws[i]) + ws[i]
				)

		memo[i][j] = result

		print(np.array(memo))
		print('--------------------------')

		return memo[i][j]

	print(rec(0, w))
