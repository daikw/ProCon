# coding: utf-8
import itertools as it

def judge_cross(line_v, line_h):
	(x, y1), (x, y2) = line_v
	(x1, y), (x2, y) = line_h

	if x1 >= x2: x1, x2 = x2, x1
	if y1 >= y2: y1, y2 = y2, y1

	x_in = x1 <= x <= x2
	y_in = y1 <= y <= y2

	return x_in and y_in

if __name__ == "__main__":
	n = int(input())
	s = int(input())
	x, y, a, b = [], [], [], []
	for _ in range(n):
		t = list(map(int, input().split()))
		x.append(t[0])
		y.append(t[1])
		a.append(t[2])
		b.append(t[3])

	relations = {i:set([i]) for i in range(n)}
	for i, j in it.combinations(range(n), 2):
		lvi = (((x[i], y[i]), (x[i], b[i])), ((a[i], y[i]), (a[i], b[i])))
		lvj = (((x[j], y[j]), (x[j], b[j])), ((a[j], y[j]), (a[j], b[j])))
		lhi = (((x[i], y[i]), (a[i], y[i])), ((x[i], b[i]), (a[i], b[i])))
		lhj = (((x[j], y[j]), (a[j], y[j])), ((x[j], b[j]), (a[j], b[j])))
		judge = False
		for k in [0, 1]:
			for l in [0, 1]:
				judge |= judge_cross(lvi[k], lhj[l])
				judge |= judge_cross(lvj[k], lhi[l])

		if judge:
			relations[i].add(j)
			relations[j].add(i)


	relations_ = None
	while relations_ != relations:
		relations_ = relations.copy()
		for i in range(n):
			for j in relations[i]:
				relations[i] = relations[i].union(relations[j])

	puddles = sorted([x+1 for x in relations[s-1]])

	for puddle in puddles:
		print(puddle)