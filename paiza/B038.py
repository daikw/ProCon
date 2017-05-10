# coding: utf-8
import math

if __name__ == "__main__":
	a, b, c, d = map(int, input().split())

	# x == y
	if 0 in [a, b]:
		print('miss')

	elif c == d == 0:
		print('miss')

	elif c == d:
		if a/c == b == 2:
			print(1, 1)
		else:
			print('miss')

	elif (a-d*b)%(c-d) != 0:
		print('miss')

	else:
		x = (a-d*b)//(c-d)
		y = b - x
		if x < 1 or y < 1:
			print('miss')
		else:
			print(x, y)

#	cx + dy = a
#	 x +  y = b
