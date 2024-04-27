a, b, c, d, e, f = map(int, input().split())
x, y = 0, 0

fl = False
for n in range(-999, 1000):
    for m in range(-999, 1000):
        if a * n + b * m == c and d * n + e * m == f:
            x, y = n, m
            fl = True

    if fl:
        break

print(x, y)