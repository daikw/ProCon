# coding: utf-8


if __name__ == "__main__":
	a, b, n = map(int, input().split())
	pins_ = input().split()
	pins = []
	for pin in pins_:
		if pin == 'G':
			pins.append(0)
		else:
			pins.append(int(pin))

	# get frame type
	frame = ['']*len(pins)
	before = -1
	for i, pin in enumerate(pins):
		if pin == b:
			if before == 0:
				frame[i] = 'spare'
			else:
				frame[i] = 'strike'
			before = -1
#			print(i, before)
		elif before + pin == b:
			frame[i] = 'spare'
			before = -1
#			print(i, before)
		else:
			if before != -1:
				frame[i] = 'open'
				before = -1
#				print(i, before)
			else:
				before = pin
#				print(i, before)

	# calculate
	score = 0
	for i, pin in enumerate(pins):
		if frame[i] == '':
			if i == len(pins)-1:
				score += pin
			else:
				continue
		elif frame[i] == 'open':
			score += pins[i-1]+pins[i]
#			print(score, i)
		elif frame[i] == 'spare':
			if i in range(1, len(frame)-1):
				score += b + pins[i+1]
#				print(score, i)
			else:
				score += b
#				print(score, i)
		elif frame[i] == 'strike':
			if i in range(len(frame) - 2):
				score += b + pins[i+1] + pins[i+2]
#				print(score, i)
			elif i in range(len(frame) - 1):
				score += b + pins[i+1]
#				print(score, i)
			else:
				score += b
#				print(score, i)

	print(score)
