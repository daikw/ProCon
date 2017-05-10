
# coding: utf-8


if __name__ == "__main__":
	l, n = map(int, input().split())

	L = [0]*l
	for _ in range(n):
		a, b = map(int, input().split())
		a -= 1; b -= 1
		if 1 == L[a] == L[b] and sum(L[a:b+1]) == b-a+1:
			L[a:b+1] = [0]*(b-a+1)
			#print(L)
		else:
			L[a:b+1] = [1]*(b-a+1)
			#print(L)


	print(sum(L))

