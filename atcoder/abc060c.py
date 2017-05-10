# coding: utf-8
import numpy as np

if __name__ == "__main__":
	n, t = map(int, input().split())
	tn = list(map(int, input().split()))

	clusters = [[0, 0]]
	for i in range(0, len(tn)-1):
		if tn[i+1] - tn[i] <= t:
			clusters[-1][1] = i+1
		else:
			clusters.append([i+1, i+1])

	tsum = 0
	for s, e in clusters:
		tsum += tn[e] - tn[s] + t

	print(tsum)
