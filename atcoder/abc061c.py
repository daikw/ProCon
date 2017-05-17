
# coding: utf-8

if __name__ == "__main__":
	n, k = map(int, input().split())
	preserve = None

	for _ in range(n):
		a, b = map(int, input().split())
		k -= b
		if preserve is None and k <= 0:
			preserve = a

	if preserve:
		print(preserve)
	else:
		print(a)
