
# coding: utf-8

if __name__ == "__main__":

	h, w = map(int, input().split())
	a = []
	a.append('#'*(w+2))
	for _ in range(h):
		a.append('#' + input() + '#')
	a.append('#'*(w+2))

	for i in range(h+2):
		print(a[i])
