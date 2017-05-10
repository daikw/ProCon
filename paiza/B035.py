# coding: utf-8
from operator import itemgetter


if __name__ == "__main__":
	# input
	n, m, t = map(int, input().split())

	before = dict()
	for _ in range(n):
		a, p = input().split()
		before[a] = int(p)
	before = sorted(list(before.items()), key = itemgetter(0), reverse=False)
	before = sorted(before, key = itemgetter(1), reverse=True)

	after = dict()
	for j in range(m):
		a, d, x = input().split()
		after.setdefault(d, 0)
		after[d] += int(x)
	after = sorted(list(after.items()), key = itemgetter(0), reverse=False)
	after = sorted(after, key = itemgetter(1), reverse=True)

	# rank
	before_rank = {name: (dist, rank) for (name, dist), rank in zip(before, range(t))}
	after_rank  = {name: (dist, rank) for (name, dist), rank in zip(after,  range(t))}
	if len(after_rank) < t:
		for key, dist in before:
			after_rank.setdefault(key, (0, 999))

	top_t = []
	for name, (a_dist, a_rank) in after_rank.items():
		status = ''
		if name not in before_rank.keys():
			status = 'new'
		elif before_rank[name][1] < a_rank:
			status = 'down'
		elif before_rank[name][1] > a_rank:
			status = 'up'
		else:
			status = 'same'

		top_t.append([name, a_dist, status])
	top_t = sorted(top_t, key = itemgetter(0), reverse=False)
	top_t = sorted(top_t, key = itemgetter(1), reverse=True)

	for i in range(t):
		print(' '.join(map(str,top_t[i])))