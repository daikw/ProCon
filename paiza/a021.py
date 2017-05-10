
# coding: utf-8
import itertools as it


def calc_area(island):
	return len(island)


def calc_track(island):
	track = 0
	dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

	for x, y in island:
		count = 0
		for dx, dy in dirs:
			x_, y_ = x+dx, y+dy
			if (x_, y_) in island:
				count += 1

		track += 4 - count

	return track


if __name__ == "__main__":
	h, w = map(int, input().split())
	field = []
	for _ in range(h):
		field.append(input())

	islands = []
	check = set()

	dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

	# search islands
	for x, y in it.product(range(w), range(h)):
		if (x, y) in check:
			continue

		if field[y][x] == '#':
			stack = [(x, y)]
			new = {(x, y)}
			while stack:
				x_, y_ = stack.pop()
				check.add((x_, y_))
				for dx, dy in dirs:
					x__, y__ = x_+dx, y_+dy
					if not (0 <= x__ <= w-1 and 0 <= y__ <= h-1):
						continue
					if (x__, y__) in check:
						continue
					if field[y__][x__] == '#':
						new.add((x__, y__))
						stack.append((x__, y__))
					check.add((x__, y__))

			islands.append(new)


	# calc and print results
	result = []
	for island in islands:
		area = calc_area(island)
		track = calc_track(island)

		result.append([area, track])

	for area, track in sorted(result, reverse = True):
		print(area, track)

