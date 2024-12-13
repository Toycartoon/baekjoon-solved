n, m, t = map(int, input().split())
h = []

x = t // min(n, m)
ht = x * min(n, m)
h.append((x, t - ht))

for i in range(x-1, -1, -1):
    ht = i * min(n, m)
    i += (t - ht) // max(n, m)
    ht += max(n, m) * ((t - ht) // max(n, m))
    h.append((i, t - ht))


h.sort(key=lambda x: (x[1], -x[0]))
print(*h[0])
