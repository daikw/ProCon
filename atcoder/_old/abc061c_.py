
# coding: utf-8

if __name__ == "__main__":
	n, k = map(int, input().split())
	num = [0]*10**5

	for _ in range(n):
		a, b = map(int, input().split())
		num[a-1] += b

	for i in range(10**5):
		k -= num[i]
		if k <= 0:
			print(i)
			break


