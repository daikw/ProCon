n, k, *x = map(int, open(0).read().split())

print(min(min(abs(x[i]), abs(x[i+k-1])) + x[i+k-1] - x[i] for i in range(n-k+1)))
