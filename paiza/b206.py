n = int(input())
n1, d1 = input().split()
n2, d2 = input().split()
n1 = int(n1)
n2 = int(n2)

g1, g2 = 'NS', 'WE'
res = 0

if d1 == d2:
    res = abs(n1 - n2)
elif d1+d2 in ['NS', 'SN', 'WE', 'EW']:
    res = n1 + n2
else:
    res = abs(n1 - n2) + 3.1415926535 * min(n1, n2) / 2

print(res * 100)