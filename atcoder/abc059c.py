# coding: utf-8
import math


if __name__ == "__main__":
	n = int(input())
	nums = list(map(int, input().split()))
	acm_ = [num[0]]
	acm = []
	if acm_[0] != 0:
		acm.append(acm_[0])
	else:
		acm.append(1)
	counts = []


	for i, num in enumerate(nums[1:]):
		if acm_[i]

	print(counts)