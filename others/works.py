# coding: utf-8
def main(argv):
	for v in argv:
		tr_by_rot13(v)


def tr_by_rot13(word):
	lower = 'abcdefghijklmnopqrstuvwxyz'
	upper = lower.upper()
	rot13 = ''
	for l in word:
		if l in lower:
			rot13 += lower[(lower.index(l)+13)%26]
		elif l in upper:
			rot13 += upper[(upper.index(l)+13)%26]
		else:
			rot13 += l

	print(rot13)


if __name__ == "__main__":
	import sys
	main(sys.argv[1:])
