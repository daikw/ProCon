# coding: utf-8

if __name__ == "__main__":
	a, b, c = map(int, input().split())

	resids = []
	for i in range(b):
		resids.append(i*a%b)

	if c in resids:
		print("YES")
	else:
		print("NO")
