# coding: utf-8
def opposite(pb, pa, dice):
	flg = True
	flg = flg and (pb in dice[:2] and pa in dice[:2])
	flg = flg or (pb in dice[2:4] and pa in dice[2:4])
	flg = flg or (pb in dice[4:] and pa in dice[4:])
	return flg

if __name__ == "__main__":
	tbudlr = list(map(int, input().split()))
	n = int(input())
	pn = []
	for _ in range(n):
		pn.append(int(input()))

	count = 0
	for pb, pa in zip(pn[:-1], pn[1:]):
		if pb == pa:
			continue
		elif opposite(pb, pa, tbudlr):
			count += 2
		else:
			count += 1

	print(count)