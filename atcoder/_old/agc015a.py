
# coding: utf-8

if __name__ == "__main__":
	n, a, b = map(int, input().split())
	if n < b-a+1 or b < a:
		print(0)
	elif n == 1 or n == 2 or a == b:
		print(1)
	else:
		print( (n-2)*(b-a)+1 )