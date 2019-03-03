import itertools as it


def LI(): return list(map(int, input().split()))


class Piece:
    def __init__(self, i, h, w, r, c):
        self.h = h
        self.w = w
        self.r = r
        self.c = c
        self.area = h * w
        self.i = i

    def __lt__(self, other):
        return (self.area, self.r, self.c) < (other.area, other.r, other.c)


class Board:
    def __init__(self, _h, _w):
        self.h, self.w = _h, _w
        self.state = [[0] * _w for _ in range(_h)]
        self.corners = []

    def print_board(self):
        for row in self.state:
            print(' '.join(map(str, row)))

    def set_piece(self, piece, coordinate):
        row0, col0 = coordinate
        row1, col1 = row0+piece.h, col0+piece.w

        if row1 > self.h or col1 > self.w:
            return None

        for row in range(piece.h):
            self.state[row0+row][col0:col1] = [piece.i]*piece.w

        corners = [(row0, col1 + 1), (row1 + 1, col0)]
        return corners

    def calc_score(self):
        return sum(list(map(bool, it.chain.from_iterable(self.state))))


if __name__ == "__main__":
    h, w, n = LI()
    board = Board(h, w)

    pieces = []
    for i in range(n):
        h, w, r, c = LI()
        pieces.append(Piece(i+1, h, w, r, c))

    pieces.sort()

    coordinates = [(0, 0)]
    while bool(coordinates) and bool(pieces):
        corners = board.set_piece(pieces.pop(), coordinates.pop())
        if corners:
            coordinates.extend(corners)

    board.print_board()


if False:
    b = Board(5, 7)
    p = Piece(1, 3, 5, 1, 3)

    print(b.calc_score())
    b.set_piece(p, 0, 0)
    print(b.calc_score())

    b.print_board()
