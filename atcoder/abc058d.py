# coding: utf-8


if __name__ == "__main__":
	n, m = map(int, input().split())
	x = list(map(int, input().split()))
	y = list(map(int, input().split()))
	mod = 10**9+7

	area = ((x[-1] - x[0])%mod) * ((y[-1] - y[0])%mod) %mod
	area = area * (n-1) * (m-1) % mod
	print(area)
