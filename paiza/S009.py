# coding: utf-8
import itertools as it
perm = it.permutations


class Tree:
	def __init__(self, value, position):
		self.value = value
		self.position = position
		self.child = []

	def set_connection(self, connection):
		self.connection.append(connection)

	def set_value(self, value):
		self.connection = value

	def get_value(self, position):
		return self.value

	def get_position(self):
		return self


def substitution(s, p):
	sub = [0]*len(s)
	for i, index in enumerate(p):
		sub[index-1] = s[i]
	return sub

if __name__ == "__main__":
	n = int(input())
	s = list(map(int, input().split()))
	m = int(input())
	p = []
	for _ in range(m):
		p.append(list(map(int, input().split())))

	# make applying orders
	orders = []
	for x in perm(range(m)):
		for i in range(m):
			orders.extend(list(perm(x[i:])))
	orders = list(set(orders))

	# generate the substituted
	substituted = []
	for order in orders:
		temp = s
		for i in order:
			temp = substitution(temp, p[i])
		substituted.append(temp)

	substituted.sort()
	print(' '.join(map(str, substituted[0])))
