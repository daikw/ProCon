# coding: utf-8

# make XyyyyZ.py files for AtCoder contest.

import json
import os
import subprocess as sp
import sys

text = """
# coding: utf-8
import numpy as np

if __name__ == "__main__":
	n, k = map(int, input().split())
"""


if __name__ == "__main__":

	# get arguments
	name = sys.argv[1]
	num = sys.argv[2]
	if len(sys.argv) >= 3:
		args = sys.argv[3:]

	# get configure information
	json_handler = open('config.json', 'r')
	config = json.load(json_handler)
	contestname = config['contestname']
	json_handler.close()

	filename = contestname + name + num.rjust(3, '0') + ''.join(map(str, args)) + '.py'
	if os.path.exists(filename):
		raise Exception('this file name is already exists')

	f = open(filename, 'a')
	f.write(text)
	sp.Popen(['open', filename])
	f.close()
