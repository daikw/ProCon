# coding: utf-8
import numpy as np

if __name__ == "__main__":
	n, k = map(int, input().split())
	image = []
	for _ in range(n):
		image.append(list(map(int, input().split())))

	image = np.array(image).T

	comp1 = []
	comp2 = []
	for i in range(n//k):
		comp1.append(image[i*k:(i+1)*k].mean(axis = 0))
	comp1 = np.array(comp1).T

	for j in range(n//k):
		comp2.append(comp1[j*k:(j+1)*k].mean(axis = 0))
	comp2 = np.array(comp2, dtype = int)

	result = np.array(comp2, dtype = str).tolist()

	for i in range(n//k):
		print(' '.join(result[i]))
