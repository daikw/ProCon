import math, string, fractions, heapq, re, array, bisect, sys, random, time, copy
import itertools as it
import collections as cl
import functools as ft

def LI(): return list(map(int, input().split()))
def LI_(): return list(map(lambda x: int(x) - 1, input().split()))
def LF(): return list(map(float, input().split()))
def LS(): return input().split()
def I(): return int(input())
def F(): return float(input())
def S(): return input()


class Piece:
    def __init__(self, i, h, w, r, c):
        self.h = h
        self.w = w
        self.r = r
        self.c = c
        self.area = h * w
        self.i = i


class Board:
    def __init__(self, _h, _w):
        self.h, self.w = _h, _w
        self.state = [[0] * _w for _ in range(_h)]

    def print_board(self):
        for row in range(self.h):
            print(' '.join(str(self.state[row])))

    def set_piece(self, piece, row0, col0):
        for row in range(piece.h):
            self.state[row0 + row][col0:col0+piece.w] = [piece.i]*piece.w

    def calc_score(self):
        return sum(list(map(bool, it.chain.from_iterable(self.state))))


if __name__ == "__main__":
    h, w, n = LI()

    pieces = []
    for i in range(n):
        h, w, r, c = LI()
        pieces.append([h, w, r, c, h*w, i])

    pieces.sort(key=lambda x: x[4], reverse=True)

    print(pieces)


if True:
    b = Board(5, 7)
    p = Piece(1, 3, 5, 1, 3)

    print(b.calc_score())
    b.set_piece(p, 0, 0)
    print(b.calc_score())

    b.print_board()
