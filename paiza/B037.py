# coding: utf-8
import itertools as it


def compare(la, lb):
	if len(la) != len(lb):
		return False
	for la_ in it.permutations(la, len(la)):
		if list(la_) == lb:
			return True
	else: return False


if __name__ == "__main__":
	# input
	n, d = input().split()
	n = n.rjust(2, '0')
	d = d.rjust(2, '0')
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	m = list(map(int, input().split()))

	today = list(map(int, [n[0], n[1], d[0], d[1]]))
	# calculate the pseudo random series
	w = [0, 0, 0, 0]
	for i in range(1, 10001):
		for j in range(4):
			w[j] = (a[j]*w[j]+b[j]) % m[j]
		if compare(today, list(map(lambda x: x%10, w))):
			print(i)
			break
