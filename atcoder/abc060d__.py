# coding: utf-8

if __name__ == "__main__":
	n, w = map(int, input().split())
	vs, ws = [], []

	for i in range(n):
		w_, v_ = map(int, input().split())
		ws.append(w_)
		vs.append(v_)

	nap_memo = {}
	def nap(i, j):
		key = str(i)+':'+str(j)

		if key in nap_memo:
			return nap_memo[key]

		r = 0
		if i == n:
			r = 0
		elif j < ws[i]:
			r = nap(i+1, j)
		else:
			r = max(nap(i+1, j),
					nap(i+1, j-ws[i]) + vs[i])

		nap_memo[key] = r
		return r

	print(nap(0, w))
