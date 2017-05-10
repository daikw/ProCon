# coding: utf-8


if __name__ == "__main__":
	t = input()
	MM = t[0:2]
	dd = int(t[3:5])
	hh = int(t[6:8])
	mm = t[9:11]

	dd = dd + hh//24
	hh = hh%24
	t_ = MM + '/' + str(dd).zfill(2) + ' ' + str(hh).zfill(2) + ':' + mm

	print(t_)