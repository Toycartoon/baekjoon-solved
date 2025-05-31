n, m = map(int, input().split())

ans = 0
px, py = 0, 0

g = []
for i in range(n):
    x, y = map(int, input().split())
    g.append((x, y))

for i in range(m):
    d = 0
    x, y = 0, 0
    for v in g:
        a = ((v[0]-px) ** 2 + abs(v[1]-py) ** 2)
        if max(d, a) == a:
            d = a
            x, y = v

    px, py = x, y
    ans += d
    g.remove((x, y))

    g.append(tuple(map(int, input().split())))

print(ans)
