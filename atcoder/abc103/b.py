s = input()
t = input()

S = []
for i in range(len(s)):
    S.append(s[i:] + s[:i])

if t in S:
    print('Yes')
else:
    print('No')
