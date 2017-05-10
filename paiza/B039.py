# coding: utf-8
import itertools as it

def judge_vtx_in_area(vtx, area):
	x_in = area[0][0] <= vtx[0] <= area[1][0]
	y_in = area[0][1] <= vtx[1] <= area[1][1]
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
	for i, j in it.permutations(range(n), 2):
		vtxs = [(x[i], y[i]),
				(x[i], b[i]),
				(a[i], y[i]),
				(a[i], b[i])]
		area = ((x[j], y[j]), (a[j], b[j]))
		judge = False
		for vtx in vtxs:
			judge |= judge_vtx_in_area(vtx, area)

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