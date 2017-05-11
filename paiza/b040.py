
# coding: utf-8
import numpy as np

if __name__ == "__main__":
	n, t = input().split()
	n = int(n)
	s = input()

	t = t + ' '
	alp = 'abcdefghijklmnopqrstuvwxyz '

	decoder = {k: v for k, v in zip(t, alp)}

	decoded = s
	for _ in range(n):
		temp = ''
		for letter in decoded:
			temp += decoder[letter]
		decoded = temp

	print(decoded)
