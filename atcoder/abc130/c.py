def LI(): return list(map(int, input().split()))


w, h, x, y = LI()

is_multiple = int(w == 2*x and h == 2*y)

print(w*h/2, is_multiple)