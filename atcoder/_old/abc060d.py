# coding: utf-8
import numpy as np

if __name__ == "__main__":
	n, w = map(int, input().split())
	ws, vs = [], []
	for _ in range(n):
		w_, v_ = map(int, input().split())
		ws.append(w_)
		vs.append(v_)

	# memo: ある重さにおける最大の価値 / jは重さ
	def rec(i, j, memo = [[-1 for _ in range(w+1)] for _ in range(n+1)]):

		if memo[i][j] != -1:
			return memo[i][j]

		result = 0
		if i == n:
			result = 0

		elif j < ws[i]:
			result = rec(i+1, j)

		else:
			result = max(
				rec(i+1, j),
				rec(i+1, j-ws[i]) + vs[i]
				)

		memo[i][j] = result

		print(np.array(memo))
		print('--------------------------')

		return memo[i][j]

	print(rec(0, w))
