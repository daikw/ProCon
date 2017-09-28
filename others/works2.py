# coding: utf-8
def main(argv):
	for v in argv:
		sanbaka(v)


def sanbaka(word):
	try:
		integer = int(word)

	except:
		print('invalid')
		return None

	baka1 = (integer % 3 == 0)
	baka2 = '3' in word

	if baka1 and baka2:
		print('dumb')

	elif baka1:
		print('idiot')

	elif baka2:
		print('stupid')

	else:
		print('smart')


if __name__ == "__main__":
	import sys
	main(sys.argv[1:])
