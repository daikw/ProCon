s = [ord(c) - 97 for c in input()]
t = [ord(c) - 97 for c in input()]
sl = len(s)
tl = len(t)
rr = [[0] * (tl) for _ in range(sl)]
t0 = t[0]

# init
for i in range(sl):
    if s[i] == t0:
        for k in range(i,sl):
            rr[k][0] = 1
        break

rr0 = rr[0]
s0 = s[0]
for j in range(tl):
    if s0 == t[j]:
        for k in range(j,tl):
            rr0[k] = 1
        break

# solve
ta = [(i,t[i]) for i in range(1, tl)]
for i in range(1, sl):
    rri = rr[i]
    rri1 = rr[i-1]
    si = s[i]
    for j, tj in ta:
        if si == tj:
            rri[j] = rri1[j-1] + 1
        else:
            rri[j] = rri1[j]
            if rri[j] < rri[j-1]:
                rri[j] = rri[j-1]

# restore
i = sl-1
j = tl-1
r = []
while i >= 0 and j >= 0:
    if s[i] == t[j]:
        r.append(s[i] + 97)
        i -= 1
        j -= 1
        continue
    if rr[i][j] == 0:
        break
    if i > 0 and rr[i-1][j] == rr[i][j]:
        i -= 1
    else:
        j -= 1

print(''.join(map(chr,r[::-1])))

"""
TLE

mainないと遅いのなんで…？
"""
