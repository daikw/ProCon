n = int(input())
s, p = [], []
for _ in range(n):
    s_, p_ = input().split()
    s.append(s_)
    p.append(100 - int(p_))

max_len = max([len(e) for e in s])
s = [e.ljust(max_len, '0') for e in s]
p = [str(e).rjust(3, '0') for e in p]
m = [str(e).rjust(3, '0') for e in range(1, n+1)]

merged = [s[i]+p[i]+m[i] for i in range(n)]

merged.sort()

for i in range(n):
    print(int(merged[i][-3:]))
