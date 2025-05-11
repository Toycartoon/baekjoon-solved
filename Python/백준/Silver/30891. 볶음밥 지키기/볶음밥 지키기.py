n, r = map(int, input().split())
a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append((x, y))

ans = (-101, -101)
mx = 0
for y in range(-100, 101):
    for x in range(-100, 101):
        v = 0
        for rx, ry in a:
            if ((y - ry) ** 2 + (x - rx) ** 2) ** 0.5 <= r:
                v += 1

        if max(mx, v) == v:
            mx = v
            ans = (x, y)

print(*ans)
