od = input()
ev = input().ljust(len(od), '0')

pw = ''
for i, j in zip(od, ev):
	pw += i+j

if pw[-1] == '0':
	pw = pw[0:-1]

print(pw)