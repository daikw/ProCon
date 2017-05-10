
# coding: utf-8
import numpy as np

if __name__ == "__main__":
	m, n = map(int, input().split())
	matrix = []
	for _ in range(n):
		matrix.append(input().replace(' ', ''))

	for i in range(n):
		try:
			sx, sy = matrix[i].index('s'), i
		except:
			continue

	dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

	que = [(sx, sy)]
	mpath = {(sx, sy): 1}
	result = None

	while que:
		x, y = que.pop(0)
		for dx, dy in dxy:
			x_, y_ = x+dx, y+dy

			if 0 <= x_ < m and 0 <= y_ < n:
				if matrix[y_][x_] == 'g':
					#print(y_, x_, 'take g')
					result = mpath[(x, y)] + 1
					que = None
					break

				if matrix[y_][x_] == '1':
					#print(y_, x_, 'take1')
					continue

				if not mpath.setdefault((x_, y_), 0):
					mpath[(x_, y_)] = mpath[(x, y)] + 1
					que.append((x_, y_))
					#print(x_, y_,':', mpath[(x_, y_)])


	if result:
		print(result-1)
	else:
		print('Fail')
