# coding: utf-8

import json
import sys


if __name__ == "__main__":

	contestname = sys.argv[1]

	with open('config.json', 'r') as json_r:
		conf = json.load(json_r)
		conf['contestname'] = contestname + '/'

	with open('config.json', 'w') as json_w:
		json.dump(conf, json_w)
