# coding: utf-8
import math

def get_tree_range(circle):
	x, y, r = circle
	if abs(y) > r:
		return None

	chord = math.sqrt(r**2 - y**2)
	l = x - chord
	r = x + chord
	return (l, r)

if __name__ == "__main__":
	n = int(input())
	circles = []
	for _ in range(n):
		circles.append(list(map(int, input().split())))

	breaks = list()
	broken_line = set()
	for i in range(n):
		tree_range = get_tree_range(circles[i])
		if not tree_range: continue

		l, r = tree_range
		breaks.append((l, r))
		broken_line.add(l); broken_line.add(r)

	broken_line = sorted(list(broken_line))
	circle_counts = [0]*(len(broken_line)*2 - 1)

	for l, r in breaks:
		left = broken_line.index(l)
		right = broken_line.index(r)
		for i in range(left*2, right*2+1):
			circle_counts[i] += 1

	print(max(circle_counts))