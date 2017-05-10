# coding: utf-8

def getwords(table, i, j):
	n = len(table)
	count = 0
	words = set()
	directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
	for dx, dy in directions:



if __name__ == "__main__":
	n = int(input())
	table = []
	for _ in range(n):
		table.append(input())
	m = int(input())
	p = []
	for _ in range(m):
		p.append(input())

	words = set()
	for i in range(n):
		for j in range(n):
			words.update(getwords(table, i, j))
