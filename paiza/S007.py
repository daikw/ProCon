# coding: utf-8
import re

if __name__ == "__main__":
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	numeral = '0123456789'
	result = {k:0 for k in alphabet}
	s = input()

	for letter in s:
		times = [1]
		num_flg = 0
		if letter in alphabet:
			result[letter] += 1 * times[-1]
		if letter in numeral:
			num_flg = 1
			temp += letter
		if letter == '\(':
			times.append(times[-1]*num)
		if letter == '\)':
			del times[-1]




	x = re.finditer(r'[0-9]+', s)
	for i in x:
		s[i.start():i.end()]

	'([0-9]+)|([0-9]+.+¥(.+¥))'


	s = 'abcdefg10h12(ij2(3k))l9mnop4(3(2(6(qq)r)s5tu)7v5w)x15(yz)'
	x = re.finditer('[0-9]+|\(|\)', s)
	splitter = []
	for match in x:
		splitter.append(match.start())
		splitter.append(match.end())
	sp = [s[l:r] for l, r in zip(splitter[:-1], splitter[1:])]