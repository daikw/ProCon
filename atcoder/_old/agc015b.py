
# coding: utf-8
if __name__ == '__main__':
	ud = input()
	n = len(ud)
	result = 2*n**2 - 2*n
	for i, letter in enumerate(ud):
		if ud[i] == 'U':
			result -= n-i-1
		else:
			result -= i
	print(result)

"""
if __name__ == '__main__':
	ud = input()
	n = len(ud)
	mat = [[2]*n for _ in range(n)]
	for i, letter in enumerate(ud):
		if ud[i] == 'U':
			for j in range(i+1, n):
				mat[i][j] = 1
		else:
			for j in range(i):
				mat[i][j] = 1

	print(sum(map(sum, mat)) - 2*n)
"""