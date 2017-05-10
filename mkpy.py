# coding: utf-8

# make XyyyyZ.py files for AtCoder contest.

import subprocess as sp
import sys

text = """
# coding: utf-8
import numpy as np

if __name__ == "__main__":
	n, k = map(int, input().split())
"""


if __name__ == "__main__":
	name = sys.argv[1]
	num = sys.argv[2]
	if len(sys.argv) >= 3:
		args = sys.argv[2:]

	filename = name + num.rjust(3, '0') + ''.join(map(str, args)) + '.py'
	f = open(filename, 'a')
	f.write(text)
	sp.Popen(['open', filename])
	f.close()
