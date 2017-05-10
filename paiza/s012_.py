
# coding: utf-8

def b_search(num, L):
	# list should be sorted.
	# returns left index
	li, ri = 0, len(L)
	if num < L[0]:
		return li
	if L[-1] < num:
		return ri

	while li < ri:
		r_ = (ri-li)//2 + li
		if L[li] <= num < L[r_]:
			ri = r_

		else:
			li, ri = r_ + 1, li

	return li


if __name__ == "__main__":
	l, n = map(int, input().split())
	lis, ris = [], []

	for _ in range(n):
		a, b = map(int, input().split())
		li = b_search(a, lis)
		ri = b_search(b, lis)

		if 1 == L[a] == L[b] and sum(L[a:b+1]) == b-a+1:
			L[a:b+1] = [0]*(b-a+1)
			#print(L)
		else:
			L[a:b+1] = [1]*(b-a+1)
			#print(L)


	print(sum(L))

