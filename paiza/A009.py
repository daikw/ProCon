# coding: utf-8


if __name__ == "__main__":
	h, w = map(int, input().split())
	boxes = []
	for _ in range(h):
		boxes.append(input())

	x, y, di = 0, 0, (1, 0)
	distance = 0
	while x in range(w) and y in range(h):
		if boxes[y][x] == '\\':
			di = (di[1], di[0])
		elif boxes[y][x] == '/':
			di = (-di[1], -di[0])

		x, y = x + di[0], y + di[1]
		#print(x, y, di)

		distance += 1

	print(distance)