n, k = map(int, input().split())

h, m, s = 0, 0, 0
ans = 0
while h <= n:
    if str(k) in str(h).zfill(2) + str(m).zfill(2) + str(s).zfill(2):
        ans += 1

    s += 1
    if s > 59:
        s = 0
        m += 1

    if m > 59:
        m = 0
        h += 1

print(ans)
