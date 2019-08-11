n_ = input()
n = int(n_)

levels = [9, 0, 900, 0, 90000, 0]

if n == 10**5:
    print(sum(levels))
if len(n_) == 5:
    print(sum(levels[:4]) + n - 100 + 1)
if len(n_) == 4:
    print(sum(levels[:3]))
if len(n_) == 3:
    print(sum(levels[:2]) + n - 10 + 1)
if len(n_) == 2:
    print(sum(levels[:1]))
if len(n_) == 1:
    print(n)
