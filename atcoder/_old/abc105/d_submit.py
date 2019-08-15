n, m = map(int, input().split())
a = map(int, input().split())

b_acm = 0
mod_m_counts = {}
for ai in a:
    b_acm = (b_acm + ai) % m
    mod_m_counts.setdefault(b_acm, 0)
    mod_m_counts[b_acm] += 1

count = 0
for k, v in mod_m_counts.items():
    count += v * (v - 1) // 2
    if k == 0:
        count += v

print(count)
