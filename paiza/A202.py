import sys
import re
def I(): return int(sys.stdin.readline())
def LI(): return [int(x) for x in sys.stdin.readline().split()]


n = I()
schedule = LI()

days_per_week = 7
week_satisfies =\
    [int(sum(schedule[i:i + days_per_week]) <= 5)
        for i in range(n - days_per_week + 1)]

week_satisfies = ''.join(map(str, week_satisfies))
zero_dumped = re.sub(r'0+', '0', week_satisfies)

max_len = max(map(len, zero_dumped.split('0')))
if max_len == n - 6:
    print(n)
elif max_len:
    print(days_per_week + max_len)
else:
    print(0)
